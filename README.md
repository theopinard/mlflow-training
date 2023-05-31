# mlflow-training

The purpose of the tutorial is to give a taste of the ML development process with MLflow. It is intended in providing a breadth rather than depth introduction but will give the audience a hands-on experience allowing them to dive into the specific submodules.

## Requirements for the tutorial

You will need a linux OS or a macOS with [docker](https://www.docker.com/) and [visual studio code](https://code.visualstudio.com/) installed. I have not tried this setup on windows.
If you are using windows the recommended way is to use [github codespaces](https://github.com/features/codespaces). 

Please come to the tutorial already with a running repository. Setting up the environment can take some time and we would like to spend the time in the tutorial coding. 

## Installation

### Use vscode with dev container: 
[
    ![Open in Remote - Containers](
        https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode
    )
](
    https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/theopinard/mlflow-training/
)

If you already have VS Code and Docker installed, you can click the badge above. Clicking these links will cause VS Code to automatically install the Dev Containers extension if needed, clone the source code into a container volume, and spin up a dev container for use.

### Use vscode on github (codespace)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/theopinard/mlflow-training?quickstart=1)

If you are using windows or do not want to install vscode on your machine, you can click on the badge above to spin up a codespace environment. 

### Use your IDE with a manual environemnt

If you want to do it manually you will need to create a new environemnent with python 3.10 installed (you will need to change some path on the top of the notebook).

Then you can install the requirements using pip

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

You would also need to have java and pyenv installed to run the predict step in the second notebook.

To make sure your environement was set up correctly you can finally run the pipeline end to end.

```bash
python src/scripts/run_all.py local
```

## How to use this repository

We will have 2 git branchs you can switch between:
* `main` branch which will contain the code with the solution
* `tutorial` branch which contains the code with the ToDo to implement.

If you got the code from clicking on the vscode or codespace link you are already in the `tutorial` branch. 

You can switch between from main to solution by running:
```bash
git checkout tutorial
```

If you are stuck you can check the solution by going to the main branch. 

The tutorial consists of 2 jupyter notebooks which can be found in `src/notebook`. 

You can start the jupyter server by running `jupyter lab` or use your IDE directly (pycharm pro, vscode and codespace supports jupyter notebooks).

The presentation for the workshop can be found [here](https://docs.google.com/presentation/d/1EbprRo1zkZazqYy5o7cddSlozUBO2mpnKqF8x0c0EXA/edit?usp=sharing).

## Credits

This repository was only possible thanks to others repository that as used. In particular I would like to call out:
* [python-devcontainer-template](https://github.com/godatadriven/python-devcontainer-template)
* [recipes-examples](https://github.com/mlflow/recipes-examples)
