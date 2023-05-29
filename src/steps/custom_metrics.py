from typing import Dict

from pandas import DataFrame
from sklearn.metrics import mean_squared_error


def rounded_root_mean_squared_error(
    eval_df: DataFrame,
    builtin_metrics: Dict[str, float],  # pylint: disable=unused-argument
) -> float:
    """
    Compute the mean squared error once the predicitons have been rounded to the nearest integer.

    :param eval_df: A Pandas DataFrame containing the following columns:

                    - ``"prediction"``: Predictions produced by submitting input data to the model.
                    - ``"target"``: Ground truth values corresponding to the input data.

    :param builtin_metrics: A dictionary containing the built-in metrics that are calculated
                            automatically during model evaluation. The keys are the names of the
                            metrics and the values are the scalar values of the metrics. For more
                            information, see
                            https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.evaluate.
    :return: The rounded mean square error.
    """
    return mean_squared_error(
        y_pred=eval_df["prediction"].round(),
        y_true=eval_df["target"],
        squared=False,
    )