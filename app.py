import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load models
model = pickle.load(open("best_model.pkl", "rb"))


st.title('Car Details')

st.subheader('Information about Car')

# Sidebar options for model selection
options = st.sidebar.selectbox('Select ML Model', ['model'])

# Input sliders and selectors
year = st.slider('Year', 1992, 2020, step=1)
selling_price = st.slider('Selling Price', 20000, 8900000, step=1000)
km_driven = st.slider('Kilometers Driven', 1000, 806599, step=100)
fuel = st.selectbox('Fuel', ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owner = st.selectbox('Owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])

# Prediction button
if st.button('Predict'):
    # Encoding categorical variables
    if fuel == "Petrol":
        fuel = 0
    elif fuel == "Diesel":
        fuel = 1
    else:
        fuel = 2

    if seller_type == "Individual":
        seller_type = 0
    elif seller_type == "Dealer":
        seller_type = 1
    else:
        seller_type = 2

    if transmission == "Manual":
        transmission = 0
    else:
        transmission = 1

    if owner == "First Owner":
        owner = 0
    elif owner == "Second Owner":
        owner = 1
    elif owner == "Third Owner":
        owner = 2
    elif owner == "Fourth & Above Owner":
        owner = 3
    else:
        owner = 4

    # Create the test array
    test = np.array([year, selling_price, km_driven, fuel, seller_type, transmission, owner])
    test = test.reshape(1, -1)

    # Model prediction
   prediction = model.predict(test)[0]

    # Display the result
    st.success(f'Predicted Price: {prediction}')
