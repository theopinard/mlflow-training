from src.steps.transform import transformer_fn
from sklearn.pipeline import Pipeline


def test_transformer_fn():
    """It returns a sklearn transformer"""
    transformer = transformer_fn()
    assert isinstance(transformer, Pipeline)