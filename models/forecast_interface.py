from abc import ABC, abstractmethod

from schemas.forecast_data import ForecastData


class ForecastInterface(ABC):
    """
    Для добавления новой модели нужно создать файл с классом модели,
    который будет наследоваться от этого интерфейса.

    Далее реализовать все его методы: preprocess, fit и predict

    Для примера есть catboost_forecast.py
    """

    @abstractmethod
    def preprocess(self) -> "ForecastInterface":
        """
        Предобработка данных перед обучением.

        Добавление переменных с лагом, приведение даты к datetime и прочее

        Возвращает self
        """
        ...

    @abstractmethod
    def fit(self) -> "ForecastInterface":
        """
        Обучение модели

        Возвращает self
        """
        ...

    @abstractmethod
    def predict(self) -> ForecastData:
        """
        Предсказание модели на Train и Test выборке

        Возвращает ForecastData
        """
        ...
