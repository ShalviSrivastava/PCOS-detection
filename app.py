import streamlit as st
import pickle
import numpy as np

# Load model, scaler, feature names
model = pickle.load(open('pcos_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
feature_names = pickle.load(open('feature_names.pkl', 'rb'))

# Page config
st.set_page_config(page_title="PCOS Detection", page_icon="🩺", layout="centered")

st.title("🩺 PCOS Detection Tool")
st.markdown("Enter the details below to check PCOS risk.")

# Input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (yrs)", 18, 50, 25)
    weight = st.number_input("Weight (Kg)", 30, 150, 60)
    height = st.number_input("Height (Cm)", 130, 200, 160)
    bmi = st.number_input("BMI", 10.0, 50.0, 22.0)
    hb = st.number_input("Hb (g/dl)", 5.0, 20.0, 12.0)
    cycle = st.selectbox("Cycle (R/I)", [1, 2], format_func=lambda x: "Regular" if x==1 else "Irregular")
    cycle_length = st.number_input("Cycle Length (days)", 2, 10, 5)
    marriage_yrs = st.number_input("Marriage Status (Yrs)", 0, 30, 3)
    pregnant = st.selectbox("Pregnant (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    abortions = st.number_input("No. of Abortions", 0, 10, 0)
    fsh = st.number_input("FSH (mIU/mL)", 0.0, 50.0, 5.0)
    lh = st.number_input("LH (mIU/mL)", 0.0, 50.0, 5.0)

with col2:
    fsh_lh = st.number_input("FSH/LH", 0.0, 10.0, 1.0)
    hip = st.number_input("Hip (inch)", 20, 60, 36)
    waist = st.number_input("Waist (inch)", 20, 60, 30)
    waist_hip = st.number_input("Waist:Hip Ratio", 0.0, 2.0, 0.8)
    tsh = st.number_input("TSH (mIU/L)", 0.0, 10.0, 2.0)
    amh = st.number_input("AMH (ng/mL)", 0.0, 20.0, 3.0)
    prl = st.number_input("PRL (ng/mL)", 0.0, 50.0, 15.0)
    vit_d3 = st.number_input("Vit D3 (ng/mL)", 0.0, 100.0, 30.0)
    prg = st.number_input("PRG (ng/mL)", 0.0, 20.0, 5.0)
    rbs = st.number_input("RBS (mg/dl)", 50.0, 300.0, 100.0)
    weight_gain = st.selectbox("Weight Gain (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    hair_growth = st.selectbox("Hair Growth (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")

col3, col4 = st.columns(2)
with col3:
    skin_darkening = st.selectbox("Skin Darkening (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    hair_loss = st.selectbox("Hair Loss (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    pimples = st.selectbox("Pimples (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    fast_food = st.selectbox("Fast Food (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
    reg_exercise = st.selectbox("Regular Exercise (Y/N)", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")

with col4:
    bp_systolic = st.number_input("BP Systolic (mmHg)", 60, 180, 120)
    bp_diastolic = st.number_input("BP Diastolic (mmHg)", 40, 120, 80)
    follicle_l = st.number_input("Follicle No. (L)", 0, 30, 5)
    follicle_r = st.number_input("Follicle No. (R)", 0, 30, 5)
    avg_f_size_l = st.number_input("Avg. F size (L) (mm)", 0.0, 30.0, 10.0)
    avg_f_size_r = st.number_input("Avg. F size (R) (mm)", 0.0, 30.0, 10.0)
    endometrium = st.number_input("Endometrium (mm)", 0.0, 20.0, 8.0)

# Predict button
if st.button("🔍 Predict"):
    input_data = np.array([[age, weight, height, bmi, hb, cycle, cycle_length,
                            marriage_yrs, pregnant, abortions, fsh, lh, fsh_lh,
                            hip, waist, waist_hip, tsh, amh, prl, vit_d3, prg,
                            rbs, weight_gain, hair_growth, skin_darkening, 
                            hair_loss, pimples, fast_food, reg_exercise,
                            bp_systolic, bp_diastolic, follicle_l, follicle_r,
                            avg_f_size_l, avg_f_size_r, endometrium]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1] * 100

    st.markdown("---")
    if prediction[0] == 1:
        st.error(f"⚠️ High PCOS Risk Detected! ({probability:.1f}% probability)")
        st.markdown("Please consult a gynecologist for proper diagnosis.")
    else:
        st.success(f"✅ Low PCOS Risk ({probability:.1f}% probability)")
        st.markdown("Keep maintaining a healthy lifestyle!")