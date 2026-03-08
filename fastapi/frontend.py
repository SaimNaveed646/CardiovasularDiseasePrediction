import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Cardio Risk Predictor", page_icon="❤️", layout="centered")
st.title("💓 Cardiovascular Risk Prediction")
st.markdown("Fill in your details below to predict your cardiovascular risk:")

# ---- User Inputs ----
name = st.text_input("Full Name *")
age = st.number_input("Age", min_value=1, max_value=119, value=30)
gender = st.selectbox("Gender", ["male", "female"])
height = st.number_input("Height (meters)", 0.5, 2.5, 1.7)
weight = st.number_input("Weight (kg)", 1.0, 300.0, 70.0)
ap_hi = st.number_input("Systolic Blood Pressure (ap_hi)", 50, 300, 120)
ap_lo = st.number_input("Diastolic Blood Pressure (ap_lo)", 30, 200, 80)
cholesterol = st.selectbox("Cholesterol Level", [1,2,3], format_func=lambda x: {1:"Normal",2:"Above Normal",3:"Well Above Normal"}[x])
gluc = st.selectbox("Glucose Level", [1,2,3], format_func=lambda x: {1:"Normal",2:"Above Normal",3:"Well Above Normal"}[x])
smoke = st.selectbox("Do you smoke?", [True, False])
alco = st.selectbox("Do you drink alcohol?", [True, False])
active = st.selectbox("Are you physically active?", [True, False])

# ---- Submit ----
if st.button("Predict Risk"):

    if not name.strip():
        st.error("❌ Name is required!")
    else:
        input_data = {
            "name": name,
            "age": age,
            "gender": gender,
            "weight": weight,
            "height": height,
            "ap_hi": ap_hi,
            "ap_lo": ap_lo,
            "cholesterol": cholesterol,
            "gluc": gluc,
            "smoke": smoke,
            "alco": alco,
            "active": active
        }

        try:
            response = requests.post(API_URL, json=input_data)
            result = response.json()

            if response.status_code == 200:
                pred = result["predicted_category"]
                color = "green" if pred == 0 else "red"
                st.markdown(f"**Prediction Result for {name}:** <span style='color:{color}; font-size:24px;'>{pred}</span>", unsafe_allow_html=True)
            else:
                st.error(f"API Error: {response.status_code}")
                st.write(result)

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")