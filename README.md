# mlflow-training

The purpose of the tutorial is to give a taste of the ML development process with MLflow. It is intended in providing a breadth rather than depth introduction but will give the audience a hands-on experience allowing them to dive into the specific submodules.

## Requirements for the tutorial

You will need a linux OS or a macOS with [docker](https://www.docker.com/) and [visual studio code](https://code.visualstudio.com/) installed. I have not tried this setup on windows.
If you are using windows the recommended way is to use [github codespaces](https://github.com/features/codespaces). 

Please come to the tutorial already with a running repository. Setting up the environment can take some time and we would like to spend the time in the tutorial coding. 

## Installation

[
    ![Open in Remote - Containers](
        https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode
    )
](
    https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/theopinard/mlflow-training
)

If you use the dev container you are already done ;) 

If you want to do it manually you will need to create a new environemnent with python 3.10 installed (you will need to change some path on the top of the notebook).

Then you can install the requirements using pip

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

You would also need to have java and pyenv installed to run the predict step

## Test your environement

To make sure everything is running you can run the pipeline end to end.

```bash
python src/scripts/run_all.py local
```

## Who to use this repository

We will have 2 git branch you can switch between:
* `main` branch which will contain the code with the solution
* `solution` branch which contains the code with the ToDo to implements

You can switch between from main to solution by running:
```bash
git checkout solution
```

If you are stuck you can check the solution by going to the main branch. 

The tutorial consists of 2 jupyter notebooks which can be found in `src/notebook`. 
You can start the jupyter server by running:
```bash
jupyter lab
```
