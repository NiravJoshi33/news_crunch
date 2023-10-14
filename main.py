files = ["coinedition.csv","thedailyhodl.csv", "finbold.csv", "newsbtc.csv", "utoday"]

# Delete previous files
import os
from os.path import exists

def delete_files():
    for file in files:
        if exists(file):
            os.remove(file)

# Run Spiders
from news_scrapper.spiders.all_news_spider import run_all_spiders
run_all_spiders()

# Data Cleaning
from data_processing import process_date
import pandas as pd

#-----------------------------------------
# Clean the data before saving it to the final file
for file in files:
    print(f"Now processing file: {file}")
    data = pd.read_csv(file)
    new_data = process_date(data).drop_duplicates(subset="title",keep="first", inplace=True) # Removes duplicate rows from dataframe
    print(new_data)
    new_data.to_csv(f"clean_{file}")

#-----------------------------------------
# Source file: news_display.py
# Run Streamlit App
import sys
import streamlit.web.cli as stdcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "news_display.py"]
    sys.exit(stdcli.main())
