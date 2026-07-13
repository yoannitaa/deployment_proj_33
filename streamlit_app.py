import streamlit as st
import pandas as pd
from app.utils import model_helper

st.header("Claim Fraud Predictor")

file = st.file_uploader("Upload data yang ingin diprediksi (csv)", type=".csv")
if file:    
    df_file = pd.read_csv(file)
    st.dataframe(df_file)
    predict = st.button("PRedict !")
    if predict:
        result = model_helper.predict(df_file)
        predict_proba = result["prob"]
        predict_class = result["class"]
        
        result_df = pd.DataFrame({
            "claim_number": df_file["claim_number"],
            "prediction": predict_class,
            "probability" : predict_proba
        })
        st.success("Horay Prediksi Berhasil")
        st.dataframe(result_df)