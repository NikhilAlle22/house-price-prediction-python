import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("house_price_model.pkl")

# Page config
st.set_page_config(page_title="House Price Prediction", page_icon="🏡", layout="centered")

# Title
st.title("🏡 House Price Prediction App")
st.markdown("### Enter the details below to predict the house price")
st.divider()

# Two-column layout for inputs
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("🛏️ Bedrooms", min_value=0, value=3, step=1)
    bathrooms = st.number_input("🛁 Bathrooms", min_value=0, value=2, step=1)
    condition = st.slider("🏠 Condition (1 = Poor, 5 = Excellent)", min_value=1, max_value=5, value=3)

with col2:
    living_area = st.number_input("📐 Living Area (sqft)", min_value=200, value=2000, step=50)
    schools_nearby = st.number_input("🎓 Schools Nearby", min_value=0, value=2, step=1)

st.divider()

# Predict button
if st.button("🔮 Predict Price", use_container_width=True):
    st.balloons()
    X = [[bedrooms, bathrooms, living_area, condition, schools_nearby]]
    X_array = np.array(X)

    price = model.predict(X_array)

    # Styled output
    st.success(f"💰 The predicted price of the house is: **₹{price[0]:,.2f}**")

else:
    st.info("👆 Please fill the details and click **Predict Price** to get the result.")
