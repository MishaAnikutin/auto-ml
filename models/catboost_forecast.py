from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
import pandas as pd

from .forecast_interface import ForecastInterface
from schemas.forecast_data import ForecastData, TimeSeries


class CatBoostForecast(ForecastInterface):
    def __init__(
            self,
            df: pd.DataFrame,
            iterations: int,
            learning_rate: int,
            depth: int,
            lookback: int,
            test_size: float
    ):
        self.df = df
        self.lookback = lookback
        self.model = CatBoostRegressor(iterations=iterations, learning_rate=learning_rate, depth=depth)
        self.test_size = test_size

    def preprocess(self):
        # Приводим даты к типу datetime
        self.df['date'] = pd.to_datetime(self.df['date'])

        # Сортируем по дате, чтобы прогноз осуществлялся по предыдущим (а не будущим) значеням
        self.df = self.df.sort_values('date')

        # Добавляем переменные с лагом
        for i in range(1, self.lookback + 1):
            self.df[f'target_lag_{i}'] = self.df['target'].shift(i)

        # Удаляем все пустые значения
        self.df = self.df.dropna()

        # Разделяем на обучающую и тестовую выборку
        X = self.df.drop(columns=['date', 'target', 'dataset'])
        y = self.df[['target']]

        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(X, y, shuffle=False, test_size=self.test_size)

        return self

    def fit(self):
        self.model.fit(X=self.x_train, y=self.y_train)

        return self

    def predict(self) -> ForecastData:
        train_predict = self.model.predict(self.x_train)
        train_date = self.df['date'][:train_predict.shape[0]]

        test_predict = self.model.predict(self.x_test)
        test_date = self.df['date'][train_predict.shape[0]:]

        return ForecastData(
            train_predict=TimeSeries(value=list(train_predict), date=list(train_date)),
            test_predict=TimeSeries(value=list(test_predict), date=list(test_date))
        )
