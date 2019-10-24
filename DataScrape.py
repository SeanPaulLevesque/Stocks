import requests
import os
from datetime import date, timedelta, datetime
from Utilities import parse_JSON, create_option_symbol
import json
import jsonpickle

start_date = date(2019, 5, 6)
end_date = date(2019, 10, 25)
symbol = 'VXX'
delta = timedelta(days=1)

Fridays=[]
while start_date <= end_date:
    if start_date.weekday() == 4:
        Fridays.append(start_date)
    start_date += delta

start_date = date(2019, 5, 6)
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


for option_exp in Fridays:
    for UnderlyingPrice in range(40, 60, 1):
        UnderlyingPrice = UnderlyingPrice/2
        # Build symbol
        ticker = create_option_symbol(UnderlyingPrice, option_exp)

        # if folder doesn't exist, make
        if not os.path.exists('Data/Quotes/' + str(ticker[0:9]) + '/'):
            os.mkdir('Data/Quotes/' + str(ticker[0:9]))

        # if data file exists pull it in to reduce API calls
        if os.path.exists('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt'):
            with open('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt') as json_file:
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
            with open('Data/Quotes/' + str(ticker[0:9]) + '/' + ticker + '.txt', 'w') as outfile:
                json.dump(jsonpickle.encode(quote_obj), outfile)
