import streamlit as st

from schemas.models_enum import ModelsEnum


def selectModel():
    model_choice = st.sidebar.selectbox("Выберите модель", ModelsEnum.toList())
    test_size = st.sidebar.number_input("Доля тестовой выборки", min_value=0.0, max_value=1.0, value=0.2)

    return model_choice, test_size
