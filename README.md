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

If you use the dev container you are already done ;) 

If you want to do it in a moe manual way you will need to create a new environemnent with python 3.10 installed (you will need to change some path on the top of the notebook).

Then you can install the requirements using pip

```bash
pip install -r requirements.txt
```

## Test your environement

To make sure everything is running you can run the pipeline end to end.

```bash
python src/scripts/run_all.py local
```

Then you should be able to start the mlflow UI by running:
```bash
mlflow server \
    --backend-store-uri sqlite:///src/metadata/mlflow/mlruns.db \
    --default-artifact-root ./src/metadata/mlflow/mlartifacts \
    --host 0.0.0.0 \
    --port 5000
```
You should be able to see the mlflow ui by going to http://localhost:5000/ or http://0.0.0.0:5000/ .

You can also save your MLlfow model into [databricks community edition](https://community.cloud.databricks.com).

To do so you will need to save as env variable the following credential to make it work:
```bash
export MLFLOW_TRACKING_URI="databricks"
export DATABRICKS_USERNAME="..."
export DATABRICKS_PASSWORD="..."
```

You can then run 
```bash
mlflow experiments create -n /Shared/wine_score_recipe
python src/scripts/run_all.py databricks
```

## ToDo

- add notebook with training
- add custom metrics to evaluation
- add deployment script / doc