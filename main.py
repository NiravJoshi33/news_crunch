files = ["coinedition.csv","thedailyhold.csv", "finbold.csv", "utoday.csv", "newsbtc.csv"]

# Delete the csv files at the start of code
# import os
# from os.path import exists

# for file in files:
#     if exists(file):
#         os.remove(file)

# Run Spiders
# import news_scrapper.spiders.all_news_spider

# Data Cleaning
from data_processing import process_date, remove_header
import pandas as pd

for file in files:
    print(f"Now processing file: {file}")
    data = pd.read_csv(file)
    new_data = process_date(data)
    print(new_data)
    new_data.to_csv(f"clean_{file}")

# Combining Files
# clean_files = ["clean_coinedition.csv", "clean_finbold.csv", "clean_newsbtc.csv", "clean_thedailyhold.csv", "clean_utoday.csv"]

# clean_data = pd.read_csv(clean_files[0])
# for n in range(len(clean_files)-1):
#     clean_data = pd.concat([clean_data, clean_files[n+1]])
# clean_data.to_csv("cleaned_data.csv",mode="w")


# Run Streamlit App
import sys
import streamlit.web.cli as stdcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "news_display.py"]
    sys.exit(stdcli.main())
