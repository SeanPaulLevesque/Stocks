import requests
import os
from datetime import date, timedelta, datetime
from Utilities import IV, create_option_symbol
import json
import jsonpickle
import plotly.graph_objects as go
from plotly.subplots import make_subplots

start_date = date(2019, 10, 7)
end_date = date(2019, 10, 18)

symbol = 'VXX'
delta = timedelta(days=1)

Price = make_subplots(specs=[[{"secondary_y": True}]])
#Price = go.Figure()


# pull in stock price
if os.path.exists('Data/Quotes/' + symbol + '.txt'):
    with open('Data/Quotes/' + symbol + '.txt') as json_file:
        data = json.load(json_file)
    stock_price_obj = jsonpickle.decode(data)


# Date 2 fridays out
option_exp = date(2019, 10, 25)
curr_date = date(2019, 10, 15)

# average of date's open and close price
UnderlyingPrice = round(float(stock_price_obj[curr_date.strftime("%Y-%m-%d")]['open'])+float(stock_price_obj[curr_date.strftime("%Y-%m-%d")]['close']))/2

ticker = create_option_symbol(UnderlyingPrice, option_exp)

# pull in option price
if os.path.exists('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt'):
    with open('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt') as json_file:
        data = json.load(json_file)
    quote_obj = jsonpickle.decode(data)



# open and close price per day
k = []
j = []
l = []
# date range
x = []

# collate open and close price
while start_date <= end_date:
    if start_date.weekday() < 6:
        x.append(start_date)
        j.append(stock_price_obj[start_date.strftime("%Y-%m-%d")]['open'])
        #j.append(stock_price_obj[start_date.strftime("%Y-%m-%d")]['close'])
        k.append(quote_obj[start_date.strftime("%Y-%m-%d")]['open'])
        #k.append(quote_obj[start_date.strftime("%Y-%m-%d")]['close'])
        l.append(IV(stock_price_obj[start_date.strftime("%Y-%m-%d")]['open'], UnderlyingPrice, quote_obj[start_date.strftime("%Y-%m-%d")]['open'], 0.0159, option_exp, start_date))
        #l.append(IV(stock_price_obj[start_date.strftime("%Y-%m-%d")]['close'], UnderlyingPrice, quote_obj[start_date.strftime("%Y-%m-%d")]['close'], 0.0159, option_exp, start_date))
    start_date += delta

Price.add_trace(go.Scatter(x=x,y=l, mode='lines', name="Volatility"), secondary_y=False)
Price.add_trace(go.Scatter(x=x,y=k, mode='lines', name="Option Price"), secondary_y=True)

start_date = datetime(2019, 10, 14)
end_date = datetime(2019, 10, 18)
Price.update_layout(xaxis_range=[start_date, end_date])
Price.show()

program = 'done'
