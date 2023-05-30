from pathlib import Path

import mlflow


def setup_mlflow(experiment_name: str, mlflow_location: str = "metadata/mlflow"):
    """set mlflow experiment and mlflow artifacts location"""
    mlflow_root_path = Path.cwd().joinpath(mlflow_location)
    mlflow_root_path.mkdir(parents=True, exist_ok=True)
    # create a sqlite file if id does not exists
    sqlite_path = mlflow_root_path.joinpath("mlruns.db")
    sqlite_path.touch()

    # set the tracking to the sqlite file
    mlflow.set_tracking_uri(sqlite_path.as_uri().replace("file:", "sqlite:/"))

    # Get a list of all existing experiments
    experiments = mlflow.search_experiments()
    experiment_names = [ex.name for ex in experiments]
    # Create experiment if it does not exist
    if experiment_name not in experiment_names:
        artifact_location = mlflow_root_path.joinpath("mlartifacts")
        artifact_location.mkdir(exist_ok=True)
        mlflow.create_experiment(
            experiment_name,
            artifact_location=artifact_location.as_uri(),
        )

    mlflow.set_experiment(experiment_name)
    return True


setup_mlflow(
    experiment_name="wine_score_notebook",
)
