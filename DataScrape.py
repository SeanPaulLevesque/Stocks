import requests
import os
from datetime import date, timedelta, datetime
from Utilities import parse_JSON, create_option_symbol
import json
import jsonpickle

start_date = date(2019, 10, 14)
end_date = date(2019, 10, 18)
symbol = 'VXX'
delta = timedelta(days=1)

strike_obj = []

# if data file exists pull it in to reduce API calls
if os.path.exists('Data/Quotes/' + symbol + '.txt'):
    with open('Data/Quotes/' + symbol + '.txt') as json_file:
        data = json.load(json_file)
    strike_obj = jsonpickle.decode(data)

# if data file doesn't exist, make request, parse it into JSON and save it
else:
    response = requests.get('https://sandbox.tradier.com/v1/markets/history',
        params={'symbol': symbol, 'interval': 'daily', 'start': start_date.strftime("%Y-%m-%d"), 'end': end_date.strftime("%Y-%m-%d")},
        headers={'Authorization': 'Bearer VlksdK7wWMGTOuDtr51sLS2FXBOo', 'Accept': 'application/json'}
    )

    # build object
    strike_obj = parse_JSON(response)

    # save object as json
    with open('Data/Quotes/' + symbol + '.txt', 'w') as outfile:
        json.dump(jsonpickle.encode(strike_obj), outfile)

# Date 2 fridays out
option_date = date(2019, 10, 25)

# average of date's open and close price
UnderlyingPrice = round(float(strike_obj[start_date.strftime("%Y-%m-%d")]['open'])+float(strike_obj[start_date.strftime("%Y-%m-%d")]['close']))/2

#Build symbol`
ticker = create_option_symbol(UnderlyingPrice, option_date)

# if data file exists pull it in to reduce API calls
if os.path.exists('Data/Quotes/' + ticker + '.txt'):
    with open('Data/Quotes/' + ticker + '.txt') as json_file:
        data = json.load(json_file)
    quote_obj = jsonpickle.decode(data)

# if data file doesn't exist, make request, parse it into JSON and save it
else:
    response = requests.get('https://sandbox.tradier.com/v1/markets/history',
        params={'symbol': ticker, 'interval': 'daily', 'start': start_date.strftime("%Y-%m-%d"),'end': end_date.strftime("%Y-%m-%d")},
        headers={'Authorization': 'Bearer VlksdK7wWMGTOuDtr51sLS2FXBOo', 'Accept': 'application/json'}
    )

    # build object
    quote_obj = parse_JSON(response)

    # save object as json
    with open('Data/Quotes/' + ticker + '.txt', 'w') as outfile:
        json.dump(jsonpickle.encode(quote_obj), outfile)


import plotly.graph_objects as go
from plotly.subplots import make_subplots

Price = make_subplots(specs=[[{"secondary_y": True}]])
#Price = go.Figure()

start_date = date(2019, 10, 14)
end_date = date(2019, 10, 18)

j=[]
while start_date <= end_date:
    if start_date.weekday() < 6:
        j.append(strike_obj[start_date.strftime("%Y-%m-%d")]['open'])
        j.append(strike_obj[start_date.strftime("%Y-%m-%d")]['close'])
    start_date += delta

k=[]
start_date = date(2019, 10, 14)
end_date = date(2019, 10, 18)
x=[]

while start_date <= end_date:
    if start_date.weekday() < 6:
        x.append(start_date)
        k.append(quote_obj[start_date.strftime("%Y-%m-%d")]['open'])
        k.append(quote_obj[start_date.strftime("%Y-%m-%d")]['close'])
    start_date += delta

Price.add_trace(go.Scatter(x=x,y=j, mode='lines', name="Stock Price"), secondary_y=False)
Price.add_trace(go.Scatter(x=x,y=k, mode='lines', name="Option Price"), secondary_y=True)

start_date = datetime(2019, 10, 14)
end_date = datetime(2019, 10, 18)
Price.update_layout(xaxis_range=[start_date, end_date])
Price.show()

program = 'done'