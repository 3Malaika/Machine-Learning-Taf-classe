import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv('bank.csv')
st.set_page_config(page_title='Real Time Scence Dashboard', page_icon='+',layout='wide')

# dashboard title 

st.title('Real Time Data Analytics')

# filtre sur les jobs 
job_filter = st.selectbox('Select a job', pd.unique(df['job']))
df = df[df['job']== job_filter]