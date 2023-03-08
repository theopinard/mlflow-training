# mlflow-training
The purpose of the tutorial is to give a taste of the ML development process with MLflow. It is intended in providing a breadth rather than depth introduction but will give the audience a hands-on experience allowing them to dive into the specific submodules.

## Installation

you will need to have python 3.10 installed a create a new environement. 

you can then install the requirements 

To run the script to load train and 
```bash
python scripts/run_all.py
```

to start the mlflow UI: 
```sh
mlflow ui \
    --backend-store-uri sqlite:///src/metadata/mlflow/mlruns.db \
    --default-artifact-root ./src/metadata/mlflow/mlartifacts \
    --host 0.0.0.0 \
    --port 5000
```

## ToDo

* [] add notebook with training for 
* [] add devcontainer to repository
* [] add custom metrics to evaluation
* [] add deployment script / doc