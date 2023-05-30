## How to start the MLflow server

```bash
mlflow server \
    --backend-store-uri sqlite:///src/metadata/mlflow/mlruns.db \
    --default-artifact-root ./src/metadata/mlflow/mlartifacts \
    --host 0.0.0.0 \
    --port 5000
```
You should be able to see the mlflow ui by going to http://localhost:5000/ or http://0.0.0.0:5000/ .

## How to use MLflow databricks version

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