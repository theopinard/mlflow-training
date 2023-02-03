import os
from mlflow.recipes import Recipe
from pathlib import Path

os.chdir(Path(__file__).parents[1])
r = Recipe(profile="local")

r.run("ingest")

r.run("split")

r.run("transform")

r.run("train")

r.run("evaluate")

r.run("register")

r.inspect("train")