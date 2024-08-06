from schemas.models_enum import ModelsEnum
from .catboostConfigure import configureCatBoostComponent


def configureModel(df, model_choice, test_size):
    model = None

    if model_choice == ModelsEnum.cat_boost:
        model = configureCatBoostComponent(df=df, test_size=test_size)

    return model
