from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class TimeSeries:
    date: list[datetime | date]
    value: list[float]


@dataclass
class ForecastData:
    # Прогноз на Train
    train_predict: TimeSeries

    # Прогноз на Test
    test_predict: TimeSeries
