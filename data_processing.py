import pandas as pd

global months_num
global months_short

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

def process_date(data_1):
    for i in data_1.index:
        for key, value in months_short.items():
            if key in data_1["date"][i].lower():
                print(f"key: {key.title()}")
                print(f"corresponding text to change: {data_1['date'][i].lower()}")
                new_date_data = data_1['date'][i].replace(key.title(), value)
                print(new_date_data)
                data_1['date'][i] = new_date_data
        
        if "/" in data_1['date'][i]:
            date_text_list = data_1['date'][i].split("/")
            date_text = date_text_list[1]
            year_text = date_text_list[2].split("-")[0]
            for n in range(12):
                if n == int(date_text_list[0].split(",")[1]):
                    new_date_data = months_num[n-1]
                    data_1['date'][i] = new_date_data + " " + date_text + "," + year_text

    return data_1

def remove_header(data_1):
    for i in data_1.index:
        if i == 0:
            pass
        else:
            if "title" in data_1["title"][i]:
                print(data_1["title"][i])
                data_1.drop(["title"], inplace = True)


# for file in row_data_files:
#     data = pd.read_csv(file)
#     new_date_data = process_date(data)
#     new_date_data = remove_header(new_date_data)
#     new_date_data.to_csv("clean_data.csv")





