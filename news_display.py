import pandas as pd
import streamlit as st
from data_processing import remove_header

st.set_page_config(layout="wide")

st.image("nc_short_logo.png", width= 90)
st.title("News Crunch - Crypto News")

# --------------------------------------------------
# Side Bar Setup
st.sidebar.image("nc_long_logo.png", width=280)
st.sidebar.subheader("Select the websites you want to see news from:")
the_daily_hodl = st.sidebar.checkbox("The Daily Hodl",key=1,value=True)
finbold = st.sidebar.checkbox("Finbold", key=2, value=False)
# the_block = st.sidebar.checkbox("The Block", key=3, value=True)
coin_edition = st.sidebar.checkbox("Coin Edition", key=4, value=True)
u_today = st.sidebar.checkbox("U Today", key=5, value=True)
newsbtc = st.sidebar.checkbox("NEWS BTC", key=6, value=True)

files = []
if finbold:
    files.append("clean_finbold.csv")
if the_daily_hodl:
    files.append("clean_thedailyhold.csv")
if coin_edition:
    files.append("clean_coinedition.csv")
if u_today:
    files.append("clean_utoday.csv")
if newsbtc:
    files.append("clean_newsbtc.csv")

if len(files) == 0:
    st.write("#### <span style='color:red'>No website is selected.</span>", unsafe_allow_html=True)
    st.write("#### <span style='color:red'>Select at least one website display articles</span>", unsafe_allow_html=True)
else:
    final_data = pd.read_csv(files[0])
    for a in range(len(files)-1):
        final_data = pd.concat([final_data,pd.read_csv(files[a+1])])

    final_data.to_csv("final_news_data.csv", mode="w")



st.write("---")

#for file in files:
news_data = pd.read_csv("final_news_data.csv")

num_pages = st.sidebar.slider("Select Number of Articles:", 5, 10, len(news_data))

# -----------------------------------------
# Main Page Display

if len(files) == 0:
    pass
else:
    for i in range(num_pages):
        if news_data['title'][i] == 'title':
            pass
        elif "https" not in news_data['thumb'][i]:
            print("Invalid url from webpage, skipping this item") #Skipping bad data due inconsistent page structure of websites
            pass
        else:
            col1, col2 = st.columns([0.35,0.65])
            col2.write(f"#### {news_data['title'][i]}")
            col2.write(f"###### {news_data['excerpt'][i]}", unsafe_allow_html=True)
            col2.write(f"By {news_data['author'][i]}")
            col2.write(f"{news_data['date'][i]}")
            col2.write(f"Read more at [{news_data['website_name'][i]}]({news_data['article_url'][i]})")

            col1.image(news_data['thumb'][i],width=350)
            st.write("---")
