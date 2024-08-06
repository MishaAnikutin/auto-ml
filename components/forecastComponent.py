import streamlit as st
from matplotlib import pyplot as plt

from schemas.forecast_data import ForecastData


def visualizeForecast(df, model, test_size):
    st.subheader("Прогнозирование")

    if st.button("Сделать прогноз"):
        train_size = int(df.shape[0] * (1 - test_size))

        forecast: ForecastData = (model
                                  .preprocess()
                                  .fit()
                                  .predict())

        fig = build_plot(train=df[:train_size], test=df[train_size:], forecast=forecast)
        st.pyplot(fig)


def build_plot(train, test, forecast: ForecastData):
    fig, ax = plt.subplots(dpi=150)

    ax.plot(train['date'], train['target'], label='Train')
    ax.plot(test['date'], test['target'], label='Test')
    ax.plot(forecast.train_predict.date, forecast.train_predict.value, label='Train Forecast')
    ax.plot(forecast.test_predict.date, forecast.test_predict.value, label='Test Forecast')
    ax.legend()

    return fig
