import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# =========================
# LOAD MODEL
# =========================
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Water Quality Dashboard", layout="wide")

# =========================
# HEADER
# =========================
st.title("💧 Water Quality Prediction Dashboard")
st.markdown("Hybrid System: CPCB Rules + Machine Learning")

# =========================
# SIDEBAR INPUTS
# =========================
st.sidebar.header("Enter Water Parameters")

temp = st.sidebar.number_input("Temperature (°C)", value=25.0)
do = st.sidebar.number_input("DO (mg/L)", value=7.0)
ph = st.sidebar.number_input("pH", value=7.0)
cond = st.sidebar.number_input("Conductivity", value=500.0)
bod = st.sidebar.number_input("BOD", value=4.0)
nit = st.sidebar.number_input("Nitrate", value=1.0)
fc = st.sidebar.number_input("Fecal Coliform", value=100.0)

# =========================
# CPCB RULE
# =========================
def cpcb_rule(do, bod, fc, ph):
    if do >= 6 and bod <= 2 and fc <= 50 and 6.5 <= ph <= 8.5:
        return 4
    elif do >= 5 and bod <= 3 and fc <= 500 and 6.5 <= ph <= 8.5:
        return 3
    elif do >= 4 and bod <= 3 and fc <= 5000 and 6.0 <= ph <= 9.0:
        return 2
    elif do >= 4:
        return 1
    else:
        return 0

# =========================
# LABELS
# =========================
labels = {
    4: "💧 Class A – Drinking Water",
    3: "🟢 Class B – Bathing",
    2: "🟡 Class C – Treatment Needed",
    1: "🟠 Class D – Fisheries",
    0: "🔴 Class E – Irrigation"
}

# =========================
# CREATE FEATURES (FIXED)
# =========================
def create_features(rule_pred):
    return pd.DataFrame([{
        "Temperature": temp,
        "DO": do,
        "pH": ph,
        "Conductivity": cond,
        "BOD": bod,
        "Nitrate": nit,
        "Fecal_Coliform": fc,
        "DO_BOD_ratio": do/(bod+1),
        "Pollution_Index": bod + nit + fc*0.001,
        "pH_deviation": abs(ph-7),
        "Conductivity_log": np.log1p(cond),
        "Rule_Label_Feature": rule_pred
    }])

# =========================
# MAIN
# =========================
if st.button("Predict Water Quality"):

    # Rule prediction
    rule_pred = cpcb_rule(do, bod, fc, ph)

    # Create input
    data = create_features(rule_pred)

    # Scale + Predict
    data_scaled = scaler.transform(data)
    ml_pred = model.predict(data_scaled)[0]

    # =========================
    # RESULTS (CARD STYLE)
    # =========================
    st.subheader("📊 Results Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📏 Rule-Based")
        st.info(labels[rule_pred])

    with col2:
        st.markdown("### 🤖 ML Prediction")

        if ml_pred >= 3:
            st.success(labels[ml_pred])
        elif ml_pred == 2:
            st.warning(labels[ml_pred])
        else:
            st.error(labels[ml_pred])

    # =========================
    # CONFIDENCE
    # =========================
    proba = model.predict_proba(data_scaled)[0]
    confidence = max(proba)

    st.subheader("📊 Prediction Confidence")
    st.progress(float(confidence))
    st.write(f"Confidence: {confidence*100:.2f}%")

    # =========================
    # COMPARISON
    # =========================
    st.subheader("⚖️ Comparison")

    if ml_pred == rule_pred:
        st.success("✅ High Confidence: ML agrees with CPCB")
    else:
        st.warning("⚠️ ML detected deeper pattern than rule")

    # =========================
    # INSIGHTS
    # =========================
    st.subheader("📌 Water Quality Insights")

    if ml_pred >= 3:
        st.success("✔ Water is safe for use")
    elif ml_pred == 2:
        st.warning("⚠ Needs treatment before use")
    else:
        st.error("❌ Unsafe water")

    # =========================
    # KEY FACTORS
    # =========================
    st.subheader("🔍 Key Factors Affecting Quality")

    if bod > 3:
        st.write("⚠ High BOD → organic pollution")
    if do < 4:
        st.write("⚠ Low DO → harmful for aquatic life")
    if fc > 500:
        st.write("⚠ High Fecal Coliform → contamination")
    if ph < 6.5 or ph > 8.5:
        st.write("⚠ pH out of safe range")

    # =========================
    # FEATURE IMPORTANCE
    # =========================
    st.subheader("📊 Feature Importance")

    importances = model.feature_importances_
    feature_names = [
        "Temperature", "DO", "pH", "Conductivity",
        "BOD", "Nitrate", "Fecal_Coliform",
        "DO/BOD", "Pollution", "pH Dev",
        "Cond Log", "Rule"
    ]

    fig, ax = plt.subplots(figsize=(6,4))
    ax.barh(feature_names, importances)
    ax.set_title("Most Influential Factors")
    plt.tight_layout()
    st.pyplot(fig)