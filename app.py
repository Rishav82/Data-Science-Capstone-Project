import streamlit as st
import joblib
import numpy as np
import pandas
model = joblib.load(open("best_model.joblib", "rb"))
st.title('Selling Price Prediction App')
st.header('Fill the details to generate the Selling Price')

year = st.slider('year', 1992, 2017)
km_driven = st.slider('km_driven', 1.000000, 806599.000000)
fuel = st.selectbox('fuel', ['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox('seller_type', ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission = st.selectbox('transmission', ['Manual', 'Automatic'])
owner = st.selectbox('owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])

if st.button('Predict'):
    if fuel == 'Diesel':
        fuel = 1
    elif fuel == 'Petrol':
        fuel = 4
    elif fuel == 'CNG':
        fuel = 0
    elif fuel == 'LPG':
        fuel = 3
    else:
        fuel = 2
    
    if seller_type == 'Individual':
        seller_type = 1
    elif seller_type == 'Dealer':
        seller_type = 0
    else:
        seller_type = 2
    
    if transmission == 'Manual':
        transmission = 1
    else:
        transmission = 0

    if owner == 'First Owner':
        owner = 0
    elif owner == 'Second Owner':
        owner = 2
    elif owner == 'Third Owner':
        owner = 4
    elif owner == 'Fourth & Above Owner':
        owner = 1
    else:
        owner = 3
        
    test = np.array([year, km_driven, fuel, seller_type, transmission, owner])
    test = test.reshape(1, 6)
    
    
        st.success(model.predict(test)[0])
