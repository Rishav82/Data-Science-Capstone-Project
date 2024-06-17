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
transmission = st.transmission('transmission', ['Manual', 'Automatic'])
owner = st.owner('owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])

if st.button('Predict'):
    if sex == 'Male':
        sex = 1
    else:
        sex = 0
    if smoker == 'Yes':
        smoker = 1
    else:
        smoker = 0
    if region == 'NWest':
        region = 1
    elif region == 'NEast':
        region = 0
    elif region == 'SEast':
        region = 2
    else:
        region = 3
        
    test = np.array([year, km_driven, fuel, seller_type, transmission, owner])
    test = test.reshape(1, 6)
    
    
        st.success(model.predict(test)[0])
