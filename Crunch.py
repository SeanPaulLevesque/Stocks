import os
from datetime import date, timedelta, datetime
from Utilities import IV, create_option_symbol, weeks
import json
import jsonpickle
import plotly.graph_objects as go
from plotly.subplots import make_subplots


symbol = 'VXX'
dt = date(2019, 8, 1)
end_date = date(2019,10,25)


# build fridays list
Fridays = []
delta = timedelta(days=1)
while dt <= end_date:
    if dt.weekday() == 4:
        Fridays.append(dt)
    dt += delta

for option_exp in Fridays:
    #option_exp = date(2019, 10, 25)
    start_date = weeks(option_exp, 4)
    end_date = weeks(option_exp, 1)



    # pull in stock price
    if os.path.exists('Data/Quotes/' + symbol + '.txt'):
        with open('Data/Quotes/' + symbol + '.txt') as json_file:
            data = json.load(json_file)
        stock_price_obj = jsonpickle.decode(data)


    # load all option chains for the given expiration
    Call_Dictionary = {}
    Put_Dictionary = {}
    for UnderlyingPrice in range(40,60,1):
        UnderlyingPrice = UnderlyingPrice/2
        ticker = create_option_symbol(UnderlyingPrice, option_exp, 'C')
        # pull in Call option price
        if os.path.exists('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt'):
            with open('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt') as json_file:
                data = json.load(json_file)
            Call_Dictionary[UnderlyingPrice] = jsonpickle.decode(data)
            # pull in option price

        ticker = create_option_symbol(UnderlyingPrice, option_exp, 'P')
        # pull in Put option price
        if os.path.exists('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt'):
            with open('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt') as json_file:
                data = json.load(json_file)
            Put_Dictionary[UnderlyingPrice] = jsonpickle.decode(data)



    # open and close price per day
    k = []
    j = []
    l = []
    m = []
    # date range
    x = []


    date = start_date
    while date <= end_date:
        if date.weekday() < 5:
            x.append(date)
            j.append(stock_price_obj[date.strftime("%Y-%m-%d")]['open'])

            UnderlyingPrice = round(float(stock_price_obj[date.strftime("%Y-%m-%d")]['open']) + float(stock_price_obj[date.strftime("%Y-%m-%d")]['close'])) / 2
            k.append(UnderlyingPrice)
            # calc with daily strike
            l.append(IV(stock_price_obj[date.strftime("%Y-%m-%d")]['open'], UnderlyingPrice, Call_Dictionary[UnderlyingPrice][date.strftime("%Y-%m-%d")]['open'], 0.0159, option_exp, date, 'C'))
            m.append(IV(stock_price_obj[date.strftime("%Y-%m-%d")]['open'], UnderlyingPrice, Put_Dictionary[UnderlyingPrice][date.strftime("%Y-%m-%d")]['open'], 0.0159, option_exp, date, 'P'))

            l.append(IV(stock_price_obj[date.strftime("%Y-%m-%d")]['close'], UnderlyingPrice, Call_Dictionary[UnderlyingPrice][date.strftime("%Y-%m-%d")]['close'], 0.0159, option_exp, date, 'C'))
            m.append(IV(stock_price_obj[date.strftime("%Y-%m-%d")]['close'], UnderlyingPrice, Put_Dictionary[UnderlyingPrice][date.strftime("%Y-%m-%d")]['close'], 0.0159, option_exp, date, 'P'))
        date += delta

    Price = make_subplots(specs=[[{"secondary_y": True}]])

    Price.add_trace(go.Scatter(x=x,y=j, mode='lines', name="Stock Price"), secondary_y=True)
    # Price.add_trace(go.Scatter(x=x,y=k, mode='lines', name="Strike Price"), secondary_y=True)
    Price.add_trace(go.Scatter(x=x,y=l, mode='lines', name="Call IV"), secondary_y=False)
    Price.add_trace(go.Scatter(x=x,y=m, mode='lines', name="Put IV"), secondary_y=False)

    Price.update_layout(xaxis_range=[start_date, end_date])

    Price.show()

program = 'done'
