files = ["coinedition.csv","thedailyhold.csv", "finbold.csv", "utoday.csv", "newsbtc.csv"]

# Run Spiders
# import news_scrapper.spiders.all_news_spider

# Data Cleaning
from data_processing import process_date
import pandas as pd

#-----------------------------------------
# Clean the data before saving it to the final file
for file in files:
    print(f"Now processing file: {file}")
    data = pd.read_csv(file)
    new_data = process_date(data)
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
