import streamlit as st
import pickle
import numpy as np

# Load model, scaler, feature names
model = pickle.load(open('pcos_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
feature_names = pickle.load(open('feature_names.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="HerDiagnose — PCOS Risk Prediction",
    page_icon="🌸",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #0e0e0e; }
    .stApp { background: linear-gradient(135deg, #1a0a2e 0%, #16213e 50%, #0f3460 100%); }
    h1 { color: #e91e8c !important; font-size: 2.5rem !important; }
    h3 { color: #f48fb1 !important; }
    .info-box {
        background: rgba(233, 30, 140, 0.1);
        border-left: 4px solid #e91e8c;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        color: white;
    }
    .result-high {
        background: linear-gradient(135deg, #ff416c, #ff4b2b);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        margin: 20px 0;
    }
    .result-low {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        margin: 20px 0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #e91e8c, #9c27b0);
        color: white;
        border: none;
        padding: 12px 40px;
        font-size: 1.1rem;
        border-radius: 25px;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #9c27b0, #e91e8c);
        transform: scale(1.02);
    }
    label { color: #f48fb1 !important; font-weight: 500 !important; }
    .stSelectbox label, .stNumberInput label { color: #f48fb1 !important; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🌸 HerDiagnose")
st.markdown("### PCOS Risk Prediction System")
st.markdown("---")

# Info section
with st.expander("ℹ️ What is PCOS?"):
    st.markdown("""
    **Polycystic Ovary Syndrome (PCOS)** is a hormonal disorder common among women of reproductive age.
    
    **Common Symptoms:**
    - Irregular or missed periods
    - Excess androgen (male hormones)
    - Polycystic ovaries
    - Weight gain, acne, hair loss
    
    **This tool uses a Machine Learning model trained on clinical data of 541 patients 
    to assess PCOS risk based on hormonal, physical, and lifestyle indicators.**
    
    ⚠️ *This is a screening tool only — always consult a gynecologist for proper diagnosis.*
    """)

st.markdown("### 📋 Enter Patient Details")
st.markdown("")

# Input sections
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🩺 Physical Measurements**")
    age = st.number_input("Age (yrs)", 18, 50, 25)
    weight = st.number_input("Weight (Kg)", 30, 150, 60)
    height = st.number_input("Height (Cm)", 130, 200, 160)
    bmi = st.number_input("BMI", 10.0, 50.0, 22.0)
    hip = st.number_input("Hip (inch)", 20, 60, 36)
    waist = st.number_input("Waist (inch)", 20, 60, 30)
    waist_hip = st.number_input("Waist:Hip Ratio", 0.0, 2.0, 0.8)
    bp_systolic = st.number_input("BP Systolic (mmHg)", 60, 180, 120)
    bp_diastolic = st.number_input("BP Diastolic (mmHg)", 40, 120, 80)

with col2:
    st.markdown("**🔬 Hormonal & Lab Values**")
    hb = st.number_input("Hb (g/dl)", 5.0, 20.0, 12.0)
    fsh = st.number_input("FSH (mIU/mL)", 0.0, 50.0, 5.0)
    lh = st.number_input("LH (mIU/mL)", 0.0, 50.0, 5.0)
    fsh_lh = st.number_input("FSH/LH Ratio", 0.0, 10.0, 1.0)
    tsh = st.number_input("TSH (mIU/L)", 0.0, 10.0, 2.0)
    amh = st.number_input("AMH (ng/mL)", 0.0, 20.0, 3.0)
    prl = st.number_input("PRL (ng/mL)", 0.0, 50.0, 15.0)
    vit_d3 = st.number_input("Vit D3 (ng/mL)", 0.0, 100.0, 30.0)
    prg = st.number_input("PRG (ng/mL)", 0.0, 20.0, 5.0)
    rbs = st.number_input("RBS (mg/dl)", 50.0, 300.0, 100.0)

with col3:
    st.markdown("**💊 Clinical & Lifestyle**")
    cycle = st.selectbox("Cycle (R/I)", [1, 2], format_func=lambda x: "Regular" if x==1 else "Irregular")
    cycle_length = st.number_input("Cycle Length (days)", 2, 10, 5)
    pregnant = st.selectbox("Pregnant", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    abortions = st.number_input("No. of Abortions", 0, 10, 0)
    weight_gain = st.selectbox("Weight Gain", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    hair_growth = st.selectbox("Excess Hair Growth", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    skin_darkening = st.selectbox("Skin Darkening", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    hair_loss = st.selectbox("Hair Loss", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    pimples = st.selectbox("Pimples", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    fast_food = st.selectbox("Fast Food (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    reg_exercise = st.selectbox("Regular Exercise", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    follicle_l = st.number_input("Follicle No. (L)", 0, 30, 5)
    follicle_r = st.number_input("Follicle No. (R)", 0, 30, 5)
    avg_f_size_l = st.number_input("Avg. F size (L) mm", 0.0, 30.0, 10.0)
    avg_f_size_r = st.number_input("Avg. F size (R) mm", 0.0, 30.0, 10.0)
    endometrium = st.number_input("Endometrium (mm)", 0.0, 20.0, 8.0)

st.markdown("---")

# Predict button
col_btn1, col_btn2, col_btn3 = st.columns([1,1,1])
with col_btn2:
    predict = st.button("🔍 Predict PCOS Risk")

if predict:
    input_data = np.array([[age, weight, height, bmi, hb, cycle, cycle_length,
                            abortions, 0, 0, fsh, lh, fsh_lh,
                            hip, waist, waist_hip, tsh, amh, prl, vit_d3, prg,
                            rbs, weight_gain, hair_growth, skin_darkening,
                            hair_loss, pimples, fast_food, reg_exercise,
                            bp_systolic, bp_diastolic, follicle_l, follicle_r,
                            avg_f_size_l, avg_f_size_r, endometrium]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1] * 100

    st.markdown("### 📊 Results")

    # Progress bar
    st.markdown("**Risk Probability:**")
    st.progress(int(probability))
    st.markdown(f"**{probability:.1f}%** PCOS probability")

    st.markdown("")

    if prediction[0] == 1:
        st.markdown(f"""
        <div class="result-high">
            ⚠️ High PCOS Risk Detected<br>
            <span style="font-size:0.9rem; font-weight:normal">
            Probability: {probability:.1f}% — Please consult a gynecologist
            </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Recommended next steps:**")
        st.markdown("""
        - 🏥 Consult a gynecologist or endocrinologist
        - 🩸 Get hormonal blood tests done
        - 🥗 Consider dietary and lifestyle changes
        - 💊 Discuss treatment options with your doctor
        """)
    else:
        st.markdown(f"""
        <div class="result-low">
            ✅ Low PCOS Risk<br>
            <span style="font-size:0.9rem; font-weight:normal">
            Probability: {probability:.1f}% — Keep maintaining a healthy lifestyle!
            </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Preventive tips:**")
        st.markdown("""
        - 🏃 Maintain regular exercise routine
        - 🥗 Follow a balanced diet
        - 😴 Get adequate sleep
        - 📅 Track your menstrual cycle regularly
        """)

    st.markdown("---")
    st.caption("⚠️ Disclaimer: This tool is for screening purposes only. Always consult a qualified medical professional for diagnosis and treatment.")
