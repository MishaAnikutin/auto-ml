import streamlit as st

# Компоненты
from components.csvLoader import loadData
from components.modelSelection import selectModel
from components.modelSettings import configureModel
from components.forecastComponent import visualizeForecast


st.title("Auto-ML: Прогнозирование временных рядов")
st.write("Загрузите csv файл с 2 столбцами: date и target")
st.sidebar.title("Настройки модели")

df = loadData()

if df is not None:
    model_choice, test_size = selectModel()
    model = configureModel(df, model_choice, test_size)

    if model:
        visualizeForecast(df, model, test_size)
