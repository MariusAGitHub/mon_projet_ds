import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Prédiction du marché boursier")

uploaded_file = st.file_uploader("Uploader un fichier CSV", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :", data.head())
    st.line_chart(data['Close'] if 'Close' in data.columns else data.iloc[:,1])
