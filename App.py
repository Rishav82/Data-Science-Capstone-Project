import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the model
model_path = '/mnt/data/best_model.joblib'
loaded_model = joblib.load(model_path)

# Feature names used during model training
model_columns = loaded_model.feature_names_in_

# Streamlit app
st.title("Car Price Prediction")

st.write("""
### Enter the car details to predict the selling price
""")

# Input fields
fuel = st.selectbox('Fuel', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owner = st.selectbox('Owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
km_driven = st.number_input('Kilometers Driven', value=0)
year = st.number_input('Year', value=2000)

# Preprocess input
input_data = pd.DataFrame({
    'year': [year],
    'km_driven': [km_driven],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'transmission': [transmission],
    'owner': [owner]
})

# One-hot encode the input data
input_data = pd.get_dummies(input_data, columns=['fuel', 'seller_type', 'transmission', 'owner'])

# Add missing columns
for col in model_columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Ensure the columns are in the same order
input_data = input_data[model_columns]

# Predict the price
if st.button('Predict'):
    prediction = loaded_model.predict(input_data)
    st.write(f'The predicted selling price is: ₹{prediction[0]:.2f}')

# Upload a file and predict
st.write("""
### Or upload a CSV file with car details to predict the prices
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    uploaded_data = pd.read_csv(uploaded_file)
    st.write(uploaded_data.head())

    # Preprocess the uploaded data
    uploaded_data = pd.get_dummies(uploaded_data, columns=['fuel', 'seller_type', 'transmission', 'owner'])
    
    for col in model_columns:
        if col not in uploaded_data.columns:
            uploaded_data[col] = 0
    
    uploaded_data = uploaded_data[model_columns]
    
    predictions = loaded_model.predict(uploaded_data)
    uploaded_data['predicted_selling_price'] = predictions
    st.write(uploaded_data)
