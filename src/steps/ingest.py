import pandas as pd
from pandas import DataFrame


def load_file_as_dataframe(file_path: str, file_format: str) -> DataFrame:
    """Load a csv file as a dataframe and add a column to indicate if the wine is red or white"""
    df = pd.read_csv(file_path, sep=";")
    # ToDo1: Add a column to indicate if the wine is red or white
    ...
    return df
