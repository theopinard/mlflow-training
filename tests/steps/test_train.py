from sklearn.linear_model import LinearRegression

from src.steps.train import estimator_fn


def test_estimator_fn():
    """It returns a sklearn estimator"""
    estimator = estimator_fn()
    assert isinstance(estimator, LinearRegression)