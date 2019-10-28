import os
import pandas as pd
import json
import jsonpickle
from Utilities import IV, create_option_symbol, weeks
from datetime import date, timedelta, datetime
import plotly.graph_objects as go

start_date = date(2019, 5, 8)
end_date = date(2019, 10, 25)

Fridays = []
delta = timedelta(days=1)
while start_date <= end_date:
    if start_date.weekday() == 4:
        Fridays.append(start_date)
    start_date += delta

# pull in stock price
with open('Data/Quotes/VXX.txt') as json_file:
    data = json.load(json_file)
stock_price_obj = jsonpickle.decode(data)

dt_list = []
# grab stock price
for dt in stock_price_obj:
    for i in stock_price_obj[dt]:
        stock_price_obj[dt][i] = float(stock_price_obj[dt][i].replace(']', '').replace('\'', ''))
    dti_list = {}
    dt_str = dt.split('-')
    dti_list['date'] = date(int(dt_str[0]), int(dt_str[1]), int(dt_str[2]))
    dti_list.update(stock_price_obj[dt])
    dt_list.append(dti_list)
# save to dataframe
stock_df = pd.DataFrame(dt_list)

# set index to pandas datetime format
stock_df.set_index(pd.to_datetime(stock_df['date']), inplace=True)
# add a prefix so things makes sense after a merge
stock_df = stock_df.add_prefix('Underlying_')

year = 2019
month = 10
day = 18

option_exp = date(year, month, day)

for option_exp in Fridays:
    save_df = stock_df
    for strike in range(40, 60, 1):
        strike = strike/2
        ticker = create_option_symbol(strike, option_exp, 'P')

        # pull in an option data
        with open('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt') as json_file:
            data = json.load(json_file)
        call_obj = jsonpickle.decode(data)

        # sanitize data and convert to list of dicts
        dt_list = []
        for dt in call_obj:
            for i in call_obj[dt]:
                call_obj[dt][i] = float(call_obj[dt][i].replace(']', '').replace('\'', ''))
            dti_list = {}
            dt_str = dt.split('-')
            dti_list['date'] = date(int(dt_str[0]), int(dt_str[1]), int(dt_str[2]))
            dti_list.update(call_obj[dt])
            dt_list.append(dti_list)

        if len(dt_list) == 0:
            continue
        # save as dataframe
        df = pd.DataFrame(dt_list)
        df.set_index(pd.to_datetime(df['date']), inplace=True)
        df = df.drop('date', axis=1)
        df = df.add_prefix(str(strike) + '_')

        save_df = pd.merge(save_df, df, how='outer', left_index=True, right_index=True)

    save_df.to_csv(r'Pandas/Quotes/' + str(ticker[0:9]) + 'P.txt', index=True)



program='done'