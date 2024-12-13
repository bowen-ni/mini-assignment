# test_crime.py

import unittest
import pandas as pd
from validate_functions import validate_vict_sex, validate_vict_age
from stats_function import calculate_mean_age, calculate_median_age

class TestCrimeFunctions(unittest.TestCase):
    def setUp(self):
        self.valid_data = pd.DataFrame({
            "Vict sex": ["M", "F", "M"],
            "Vict age": [25, 40, 60]
        })
        self.invalid_data = pd.DataFrame({
            "Vict sex": ["M", "X", None],
            "Vict age": [25, -5, None]
        })

    def test_validate_vict_sex_valid(self):
        self.assertTrue(validate_vict_sex(self.valid_data))

    def test_validate_vict_sex_invalid(self):
        self.assertFalse(validate_vict_sex(self.invalid_data))

    def test_validate_vict_age_valid(self):
        self.assertTrue(validate_vict_age(self.valid_data))

    def test_validate_vict_age_invalid(self):
        self.assertFalse(validate_vict_age(self.invalid_data))

    def test_calculate_mean_age(self):
        self.assertEqual(calculate_mean_age(self.valid_data), 41.666666666666664)

    def test_calculate_median_age(self):
        self.assertEqual(calculate_median_age(self.valid_data), 40)

    def test_calculate_mean_age_edge(self):
        edge_data = pd.DataFrame({"Vict age": [100]})
        self.assertEqual(calculate_mean_age(edge_data), 100)

if __name__ == "__main__":
    unittest.main()

