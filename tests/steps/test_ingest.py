from pandas import DataFrame
from src.steps.ingest import load_dataframe


def test_load_dataframe():
    """It load a pandas dataframe successfully"""
    df = load_dataframe("", "")
    assert isinstance(df, DataFrame)
