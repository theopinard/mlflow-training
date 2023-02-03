from pandas import DataFrame
import pandas as pd
import sklearn.datasets
from sklearn.utils import Bunch

def load_dataframe(location: str, _: str) -> DataFrame:
    bunch: Bunch = sklearn.datasets.load_wine(as_frame=True)
    print(bunch["frame"])
    return bunch["frame"]

def load_file_as_dataframe(file_path: str, file_format: str) -> DataFrame:
    """
    """
    df = pd.read_csv(file_path, sep=";")
    df["is_red"] = 1 if "red" in str(file_path) else 0
    return df