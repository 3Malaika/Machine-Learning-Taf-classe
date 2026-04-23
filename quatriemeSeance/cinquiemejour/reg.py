import streamlit as st
import numpy as np
import pandas as pd
import pickle 
from sklearn.preprocessing import LabelEncoder
import time 

import os
import pickle
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


pkl_path = BASE_DIR / 'reg.pkl'

with open(pkl_path, 'rb') as file:
    model = pickle.load(file)
st.set_page_config(page_title="Predicteur de charges medicales")
st.title("Prediction de charges medicales")
st.markdown("Remplis les informations ci dessous pour predire tes charges")

col1,col2 = st.columns(2)
with col1:
    age = st.slider('Age',18,100,30)
with col2:
    sex = st.selectbox('Sexe',["male","female"])


col3,col4 = st.columns(2)
with col3:
    bmi = st.number_input("BMI (indice de masse corporelle)",10,50,25)
with col4:
    children = st.slider('Nombre d enfants',0,5,1)
    

col5,col6 = st.columns(2)
with col5:
    smoker = st.selectbox('Fumeur',["yes","no"])
with col6:
    region = st.selectbox('Region',["southwest","southeast","northwest","northeast"])

sex_encoded = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker=="yes" else 0
region_dict = {"southwest": 0.24308153,"southeast": 0.27225131,"northwest":0.24233358,"northeast":0.27225131}
region_encoded = region_dict[region]

input_data = [[age,sex_encoded,bmi,children,smoker_encoded,region_encoded]]

if st.button('Prediction des charges medicales'):
    with st.spinner('Calcul  en cours ....'):
        prediction = model.predict(input_data)[0]
        time.sleep(1)
    st.success('Prediction terminée')
    st.markdown(f"#### Charges medicales Estimées: **${prediction:,.2f}**")
    st.balloons()