from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def transformer_fn():
    """
    Returns a Pipeline object that transforms the features
    """
    columns = [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulfur dioxide",
        "total sulfur dioxide",
        "density",
        "pH",
        "sulphates",
        "alcohol",
        "is_red",
    ]
    return Pipeline(
        [
            (
                "ct",
                ColumnTransformer(
                    [
                        (
                            "minmax",
                            StandardScaler(),
                            columns,
                        ),
                    ]
                ),
            )
        ]
    )
