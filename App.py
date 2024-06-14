import streamlit as st
import joblib
import numpy as np
import pandas
model = joblib.load(open("best_model.joblib", "rb"))
st.title('Selling Price Prediction App')
st.header('Fill the details to generate the Selling Price')

year = st.slider('year', 1992, 2017)
km_driven = st.slider('km_driven', -1.455639e+00, 1.549921e+01)
fuel = st.selectbox('fuel', ['Male', 'Female'])

bmi = st.slider('BMI', 15, 53)
children = st.selectbox('Children', [0, 1, 2, 3, 4, 5])
smoker = st.selectbox('Smoker', ['Yes', 'No'])
region = st.selectbox('Region', ['NWest', 'SEast', 'SWest', 'NEast'])
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
    test = np.array([age, sex, bmi, children, smoker, region])
    test = test.reshape(1, 6)
    if options == 'Lin_Reg':
        st.success(lr1.predict(test)[0])
    elif options == 'Decision_Tree':
        st.success(dt1.predict(test)[0])
    else:
        st.success(rf1.predict(test)[0])
