import streamlit as st
import pandas as pd


def loadData():
    uploaded_file = st.file_uploader("Загрузите CSV файл", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file, sep=';')
        st.write("Загруженные данные:")
        st.write(df.head(3))
        return df

    return None
