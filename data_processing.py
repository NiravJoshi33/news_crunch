import pandas as pd
import datetime as dt

global months_num
global months_short
today_datetime = dt.datetime.now()

months_short = {
    "jan ": "January ",
    "feb ": "February ",
    "mar ": "March ",
    "apr ": "April ",
    "may ": "May ",
    "jun ": "June ",
    "jul ": "July ",
    "aug ": "August ",
    "sep ": "September ",
    "oct ": "October ",
    "nov ": "November ",
    "dec ": "Decemeber ",
}

months_num = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

row_data_files = ["coinedition.csv", "finbold.csv", "newsbtc.csv", "utoday.csv"]

def process_date(data):

    for n in data.index:
        title_data = data['title'][n]
        date_data = data['date'][n]
        thumb_data = data['thumb'][n]

        if type(data) is None:
            continue
        else:
            # remove leading whitespaces in text    
            data['title'] = data.title.str.lstrip()
            data['author'] = data.author.str.lstrip()

            # Converting data like '2 hours ago' to datetime object 
            if "ago" in date_data:
                # print(f"This condition is entered")
                value, unit, ago_str = date_data.split()
                value = int(value)
                if "hour" in unit:
                    diff = dt.timedelta(hours=value)
                if "day" in unit:
                    diff = dt.timedelta(days=value)
                if "minute" in unit:
                    diff = dt.timedelta(minutes=value)
                
                article_datetime = today_datetime - diff
                # print(article_datetime)
                data["date"][n] = article_datetime

    
    # print(data)

    # Sorting data by time & date
    # data.sort_values(by=['date'], ascending=False, inplace=True)
    # print(data)
    # data['display_date'] = data["date"].dt.strftime('%B %d %Y')
                
    return data



# data = pd.read_csv("data_files/thedailyhodl.csv")
# new_data = process_date(data)
# new_data.to_csv("data_files/test_file.csv")


# for file in row_data_files:
#     data = pd.read_csv(file)
#     new_date_data = process_date(data)
#     new_date_data = remove_header(new_date_data)
#     new_date_data.to_csv("clean_data.csv")





