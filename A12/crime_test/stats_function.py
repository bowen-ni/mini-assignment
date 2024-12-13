# stats_function.py
import pandas as pd

def calculate_mean_age(data):
    if "Vict age" not in data.columns:
        raise KeyError("Column 'Vict age' is missing.")
    return data["Vict age"].dropna().mean()

def calculate_median_age(data):
    if "Vict age" not in data.columns:
        raise KeyError("Column 'Vict age' is missing.")
    return data["Vict age"].dropna().median()

