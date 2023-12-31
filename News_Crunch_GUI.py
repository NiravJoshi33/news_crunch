import pandas as pd
import streamlit as st
from PIL import Image
import urllib.request

df_relative_path = "data_files/"

st.set_page_config(
    page_title="News Crunch",
    page_icon="news_icon.png",
    layout="wide", 
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "https://github.com/NiravJoshi33/news_crunch",
        "Report a bug": "https://github.com/NiravJoshi33/news_crunch/issues",
    }
    )

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
    files.append(f"data_files/clean_finbold.csv")
if the_daily_hodl:
    files.append(f"data_files/clean_thedailyhodl.csv")
if coin_edition:
    files.append(f"data_files/clean_coinedition.csv")
if u_today:
    files.append(f"data_files/clean_utoday.csv")
if newsbtc:
    files.append(f"data_files/clean_newsbtc.csv")

if len(files) == 0:
    st.write("#### <span style='color:red'>No website is selected.</span>", unsafe_allow_html=True)
    st.write("#### <span style='color:red'>Select at least one website display articles</span>", unsafe_allow_html=True)
else:
    final_data = pd.read_csv(files[0])
    for a in range(len(files)-1):
        final_data = pd.concat([final_data,pd.read_csv(files[a+1])])
    
    # Sorting data by time & date
    # Converting other general date format to pandas datetime object
    final_data['date'] = pd.to_datetime(final_data['date'],format="mixed")
    print("***Data before soring***")
    print(final_data)
    final_data.sort_values(by=['date'], ascending=False, inplace=True)
    print("***Data after soring***")
    print(final_data)
    final_data['display_date'] = final_data["date"].dt.strftime('%B %d %Y')
    print(final_data)
    final_data.to_csv(f"data_files/final_news_data.csv", mode="w")



st.write("---")

#for file in files:
news_data = pd.read_csv(f"{df_relative_path}final_news_data.csv")
print(news_data)
num_pages = st.sidebar.slider("Select Number of Articles:", 5, 10, len(news_data))

# -----------------------------------------
# Main Page Display

if len(files) == 0:
    pass
else:
    for i in range(num_pages):
        if isinstance(news_data['thumb'][i], float):
            # thumb_img = Image.open("no_thumb_img.png")
            thumb_img = "no_thumb_img.png"
        else:
            if "http" not in news_data['thumb'][i]:
                # thumb_img = Image.open("no_thumb_img.png")
                thumb_img = "no_thumb_img.png"
            else:
                # img = Image.open(urllib.request.urlopen(news_data['thumb'][i]))
                # thumb_img = img
                thumb_img = news_data['thumb'][i]
         
        col1, col2 = st.columns([0.35,0.65])
        col2.write(f"#### {news_data['title'][i]}")
        col2.write(f"###### {news_data['excerpt'][i]}", unsafe_allow_html=True)
        col2.write(f"By {news_data['author'][i]}")
        col2.write(f"{news_data['display_date'][i]}")
        col2.write(f"Read more at [{news_data['website_name'][i]}]({news_data['article_url'][i]})")
        # img = Image.open(news_data['thumb'][i])
        # new_img = img.resize((300, 200))
        # col1.image(new_img)
        col1.write(" ")
        col1.image(thumb_img)
        # thumb_img.close()
        st.write("---")
