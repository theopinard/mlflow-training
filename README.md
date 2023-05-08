# mlflow-training
The purpose of the tutorial is to give a taste of the ML development process with MLflow. It is intended in providing a breadth rather than depth introduction but will give the audience a hands-on experience allowing them to dive into the specific submodules.

## Installation

[
    ![Open in Remote - Containers](
        https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode
    )
](
    https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/theopinard/mlflow-training
)

you will need to have python 3.10 installed a create a new environement. 

you can then install the requirements 

To run the script to load train and 
```bash
mlflow experiments create -n /Shared/wine-score
python src/scripts/run_all.py local
```

to start the mlflow UI: 
```bash
mlflow ui \
    --backend-store-uri sqlite:///src/metadata/mlflow/mlruns.db \
    --default-artifact-root ./src/metadata/mlflow/mlartifacts \
    --host 0.0.0.0 \
    --port 5000
```

You can also save your MLlfow model into [databricks community edition](https://community.cloud.databricks.com).
To do so you will need to save as env variable the following credential to make it work:
```bash
export MLFLOW_TRACKING_URI=databricks
export DATABRICKS_USERNAME="..."
export DATABRICKS_PASSWORD="..."
```

You can then run 
```bash
python src/scripts/run_all.py databricks
```

## ToDo

- add notebook with training
- add custom metrics to evaluation
- add deployment script / doc