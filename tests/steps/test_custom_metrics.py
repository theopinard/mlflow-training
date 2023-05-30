import pandas as pd

from src.steps.custom_metrics import rounded_root_mean_squared_error


def test_rounded_root_mean_squared_error():
    """It returns the rounded root mean squared error"""
    eval_df = pd.DataFrame({"prediction": [1.1, 2.2, 3.3], "target": [1, 2, 3]})
    builtin_metrics = {"rmse": 0.5}
    assert rounded_root_mean_squared_error(eval_df, builtin_metrics) == 0
