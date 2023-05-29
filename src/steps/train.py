from typing import Any, Dict

from sklearn.linear_model import LinearRegression


def estimator_fn(estimator_params: Dict[str, Any] = None):
    if estimator_params is None:
        estimator_params = {}
    return LinearRegression(**estimator_params)
