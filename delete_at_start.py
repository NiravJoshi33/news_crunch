# files = ["coinedition.csv","thedailyhold.csv", "finbold.csv", "utoday.csv", "newsbtc.csv"]

from main import files

# Delete the csv files at the start of code
import os
from os.path import exists

for file in files:
    if exists(file):
        os.remove(file)
