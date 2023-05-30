from pandas import DataFrame

from src.steps.ingest import load_file_as_dataframe


def test_load_dataframe():
    """It load a pandas dataframe successfully"""
    df = load_file_as_dataframe(
        "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
        "",
    )
    assert isinstance(df, DataFrame)
