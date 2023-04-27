import os
from mlflow.recipes import Recipe
from pathlib import Path

os.chdir(Path(__file__).parents[1])

recipe = Recipe(profile="local")

recipe.run("ingest")

recipe.run("split")

recipe.run("transform")

recipe.run("train")

recipe.run("evaluate")

recipe.run("register")

recipe.inspect("train")
