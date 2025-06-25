import streamlit as st
import pandas as pd

st.title('Mental Health in Tech Survey Data Visualization')
st.header('Combined 2014 and 2016 Data')
df_combined = pd.read_csv('combined_mental_health_data.csv')
st.dataframe(df_combined)
