
import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

model = load_model('xgb_model_final')

st.title("XGBoost Stroke Prediction App (with SMOTE)")

uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("📄 Preview of uploaded data:")
    st.write(data.head())

    st.subheader("✅ Predictions")
    preds = predict_model(model, data=data)
    st.write(preds)
