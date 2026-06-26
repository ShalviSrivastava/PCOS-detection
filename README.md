# PCOS-detection
# 🌸 HerDiagnose — PCOS Risk Prediction System

A Machine Learning-powered web application for early PCOS (Polycystic Ovary Syndrome) risk screening based on clinical, hormonal, and lifestyle indicators.

🔗 **[Live App](https://shalvisrivastava-pcos-detection-app-xxxxx.streamlit.app/)**

---

## 📌 Overview

Polycystic Ovary Syndrome (PCOS) affects millions of women worldwide, yet a large number remain undiagnosed due to lack of accessible screening tools. **HerDiagnose** bridges this gap by providing an intelligent, easy-to-use risk assessment tool that analyzes clinical data and predicts PCOS risk in real time.

---

## 📊 Dataset

- **Source:** [Kaggle — PCOS Detection Dataset](https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos)
- **Size:** 541 patients, 45 features
- **Features include:** Hormonal levels (FSH, LH, AMH, TSH), physical measurements (BMI, waist-hip ratio), lifestyle indicators (diet, exercise), and clinical symptoms

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| ML Model | Random Forest Classifier |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Class Imbalance | SMOTE (Imbalanced-Learn) |
| Deployment | Streamlit Cloud |

---

## ⚙️ Methodology

1. **Exploratory Data Analysis** — Distribution plots, correlation heatmap, symptom analysis
2. **Data Cleaning** — Handled missing values, removed weak features
3. **Feature Selection** — Dropped features with low correlation to target
4. **Class Imbalance Handling** — Applied SMOTE on training data only
5. **Model Training** — Random Forest Classifier with StandardScaler normalization
6. **Model Persistence** — Saved using Pickle for real-time inference

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| Accuracy | 90.83% |
| F1-Score (Weighted) | 0.91 |
| Precision | 0.90 |
| Recall | 0.91 |

---

## 🚀 Run Locally

```bash
git clone https://github.com/ShalviSrivastava/pcos-detection.git
cd pcos-detection
pip install -r requirements.txt
streamlit run app.py
```

---

## ⚠️ Disclaimer

This tool is intended for **screening purposes only** and does not replace professional medical diagnosis. Always consult a qualified gynecologist or endocrinologist for proper evaluation and treatment.

---

## 👩‍💻 Author

**Shalvi Srivastava**  
B.Tech ECE, IGDTUW Delhi  
[GitHub](https://github.com/ShalviSrivastava) | [LinkedIn](your-linkedin-url)
