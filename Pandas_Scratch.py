import os
import pandas as pd
import numpy as np
import json
import jsonpickle
from Utilities import IV, create_option_symbol, weeks
from datetime import date, timedelta, datetime
import plotly.graph_objects as go
import pandas as pd

# Operation	                        Syntax	        Result
# Select column	                    df[col]	        Series
# Select row by label	            df.loc[label]	Series
# Select row by integer location	df.iloc[loc]	Series
# Slice rows	                    df[5:10]	    DataFrame
# Select rows by boolean vector	    df[bool_vec]	DataFrame

option_exp = date(2019, 10, 18)

ticker = create_option_symbol(22.0, option_exp, 'C')

# pull in an option data
with open('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt') as json_file:
    data = json.load(json_file)
call_obj = jsonpickle.decode(data)

# pull in stock price
with open('Data/Quotes/VXX.txt') as json_file:
    data = json.load(json_file)
stock_price_obj = jsonpickle.decode(data)


# sanitize data and convert to list of dicts
dt_list = []
for dt in call_obj:
    for i in call_obj[dt]:
        call_obj[dt][i] = float(call_obj[dt][i].replace(']','').replace('\'',''))
    dti_list = {}
    dt_str = dt.split('-')
    dti_list['date'] = date(int(dt_str[0]), int(dt_str[1]), int(dt_str[2]))
    dti_list.update(call_obj[dt])
    dt_list.append(dti_list)

df = pd.DataFrame(dt_list)

dt_list = []
for dt in stock_price_obj:
    for i in stock_price_obj[dt]:
        stock_price_obj[dt][i] = float(stock_price_obj[dt][i].replace(']','').replace('\'',''))
    dti_list = {}
    dt_str = dt.split('-')
    dti_list['date'] = date(int(dt_str[0]),int(dt_str[1]),int(dt_str[2]))
    dti_list.update(stock_price_obj[dt])
    dt_list.append(dti_list)

df2 = pd.DataFrame(dt_list)

fig = go.Figure()

fig.add_trace(go.Scatter(x=df.date, y=df.close))
fig.add_trace(go.Scatter(x=df2.date, y=df2.close))

fig.update_layout(xaxis_range=['2019-07-25','2019-10-18'],
                  title_text="Manually Set Date Range")
fig.show()

# df.to_csv('example.csv')

print(df['date'])


program='Done'