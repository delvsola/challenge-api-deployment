from joblib import load
import pandas as pd


def predict(data: pd.DataFrame) -> float:
    if data.iloc[0].type == "HOUSE":
        return predict_house(data.drop(columns=["type"]))
    else:
        return predict_apartment(data.drop(columns=["type"]))


def predict_house(data: pd.DataFrame) -> float:
    model = load("model/houseregressor.joblib")
    return model.predict(data)[0]


def predict_apartment(data: pd.DataFrame) -> float:
    model = load("model/apartmentregressor.joblib")
    return model.predict(data)[0]
