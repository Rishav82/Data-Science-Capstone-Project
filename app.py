import streamlit as st
import pickle
import numpy as np
import pandas
model = pickle.load(open("best_model.pickle", "rb"))
st.title('Selling Price Prediction App')
st.header('Fill the details to generate the Selling Price')

year = st.slider('year', 1992, 2017)
km_driven = st.slider('km_driven', 1.000000, 806599.000000)
fuel = st.selectbox('fuel', ['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox('seller_type', ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission = st.selectbox('transmission', ['Manual', 'Automatic'])
owner = st.selectbox('owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
brand = st.selectbox('brand', ['Maruti', 'Hyundai', 'Mahindra', 'Tata', 'Ford', 'Honda', 'Toyota', 'Chevrolet', 'Renault', 'Volkswagen', 'Nissan', 'Skoda', 'Others',
                               'Fiat', 'Audi', 'Datsun', 'BMW', 'Mercedes-Benz'])

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
        
    if brand == 'Maruti':
        brand = 9.0
    elif brand == 'Hyundai':
        brand = 7.0
    elif brand == 'Mahindra':
        brand = 8.0
    elif brand == 'Tata':
        brand = 15.0
    elif brand == 'Ford':
        brand = 5.0
    elif brand == 'Honda':
        brand = 6.0
    elif brand == 'Toyota':
        brand = 16.0
    elif brand == 'Chevrolet':
        brand = 2.0
    elif brand == 'Renault':
        brand = 13.0
    elif brand == 'Volkswagen':
        brand = 17.0
    elif brand == 'Nissan':
        brand = 11.0
    elif brand == 'Skoda':
        brand = 14.0
    elif brand == 'Others':
        brand = 12.0
    elif brand == 'Fiat':
        brand = 4.0
    elif brand == 'Audi':
        brand = 0.0
    elif brand == 'Datsun':
        brand = 3.0
    elif brand == 'BMW':
        brand = 1.0
    else:
        brand = 10.0  

    test = np.array([year, km_driven, fuel, seller_type, transmission, owner, brand])
    test = test.reshape(1, -1)


    prediction = model.predict(test)[0]

    # Display the result
    st.success(f'Predicted Price: {prediction}')
