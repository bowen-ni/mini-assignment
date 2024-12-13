# validate_functions.py
import pandas as pd

def validate_vict_sex(data):
    if "Vict sex" not in data.columns:
        raise KeyError("Column 'Vict sex' is missing.")
    return data["Vict sex"].dropna().apply(lambda x: x in ["M", "F"]).all()

def validate_vict_age(data):
    if "Vict age" not in data.columns:
        raise KeyError("Column 'Vict age' is missing.")
    return data["Vict age"].dropna().apply(lambda x: isinstance(x, (int, float)) and 1 <= x <= 100).all()

