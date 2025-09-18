import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("Enter the details of the house to predict its price:")

st.divider()
bedrooms = st.number_input("Number of Bedrooms", min_value=0, value = 0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value = 0)
living_area = st.number_input("Living Area (in sqft)", min_value=0, value = 2000)
condition = st.number_input("Condition of the House (1-5)", min_value=1, max_value=5, value = 3)
schools_nearby = st.number_input("Number of Schools Nearby", min_value=0, value = 0)

st.divider()

X = [[bedrooms, bathrooms, living_area, condition, schools_nearby]]

predictbutton = st.button("Predict Price")
if predictbutton:
  st.balloons()
  X_array = np.array(X) 
  price = model.predict(X)
  st.write(f"The predicted price of the house is: ₹{price[0]:,.2f}")
  
else:
  st.write("please use predict button to get the price")


# Order of X ['number of bedrooms', 'number of bathrooms', 'living area',
#       'condition of the house', 'Number of schools nearby']