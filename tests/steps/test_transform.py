from sklearn.pipeline import Pipeline

from src.steps.transform import transformer_fn


def test_transformer_fn():
    """It returns a sklearn transformer"""
    transformer = transformer_fn()
    assert isinstance(transformer, Pipeline)