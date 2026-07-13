import pickle
import pandas as pd

MODEL_PATH = "app/models/model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


def predict(data: pd.DataFrame):
    predict_proba = model.predict_proba(data)[:,1]
    predict_proba = predict_proba.tolist()

    predict_class = [1 if val >= 0.5 else 0 for val in predict_proba]
    return{"class": predict_class, "prob":predict_proba}