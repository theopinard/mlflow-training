import os
import sys
from pathlib import Path

from mlflow.recipes import Recipe

os.chdir(Path(__file__).parents[1])

if __name__ == "__main__":
    profile = sys.argv[1]

    recipe = Recipe(profile=profile)

    recipe.run("ingest")

    recipe.run("split")

    recipe.run("transform")

    recipe.run("train")

    recipe.run("evaluate")

    if profile != "databricks":
        # We can only register locally, not on databricks community
        recipe.run("register")

    recipe.inspect("train")
