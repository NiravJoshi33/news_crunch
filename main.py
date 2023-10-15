
df_relative_path = "data_files/"

files = ["coinedition.csv","thedailyhodl.csv", "finbold.csv", "newsbtc.csv", "utoday.csv"]
clear_files = []
for file in files:
    clear_files.append(f"clean_{file}")
all_files = files + clear_files

# Delete previous files
import os
from os.path import exists

for file in all_files:
        if exists(f"{df_relative_path}{file}"):
            os.remove(f"{df_relative_path}{file}")

# Run Spiders
from news_scrapper.spiders.all_news_spider import run_all_spiders
run_all_spiders()

# Data Cleaning
from data_processing import process_date
import pandas as pd

#-----------------------------------------
# Clean the data before saving it to the final file
for file in files:
    # print(f"Now processing file: {file}") # When error is encounted, uncomment this to check in which website the issue has originated from
    data = pd.read_csv(f"{df_relative_path}{file}", skip_blank_lines = True)
    # print(f"{file} is read")
    new_data = process_date(data) 
    # print("***/nfollowing is the data/n***")
    print(new_data)
    # print(new_data)
    if new_data is None:
         pass
    else:
        new_data.to_csv(f"{df_relative_path}clean_{file}")
        # print(f"saving clean_{file}.csv at {df_relative_path}")

#-----------------------------------------
# Source file: news_display.py
# Run Streamlit App
import sys
import streamlit.web.cli as stdcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "News_Crunch_GUI.py"]
    sys.exit(stdcli.main())