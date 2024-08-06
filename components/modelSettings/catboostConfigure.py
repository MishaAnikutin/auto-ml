import streamlit as st

from models import CatBoostForecast


def configureCatBoostComponent(df, test_size):
    iterations = st.sidebar.number_input("Количество итераций", min_value=10, max_value=1000, value=100)
    learning_rate = st.sidebar.number_input("Скорость обучения", min_value=0.000001, max_value=1.0, value=0.01)
    depth = st.sidebar.number_input("Глубина дерева", min_value=1, max_value=100, value=6)
    lookback = st.sidebar.number_input("На сколько назад смотреть для прогноза", min_value=1, max_value=100, value=6)

    model = CatBoostForecast(
        df,
        iterations,
        learning_rate,
        depth,
        lookback,
        test_size
    )

    return model