from enum import Enum


class ModelsEnum(str, Enum):
    """
    Перечисление всех доступных моделей
    """
    cat_boost = 'CatBoost'

    @classmethod
    def toList(cls):
        # Возвращает список значений строк всех полей
        return list(map(lambda c: c.value, cls))
