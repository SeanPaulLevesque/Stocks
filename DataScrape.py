import requests
import os
from datetime import date, timedelta
import json
import jsonpickle

start_date = date(2019, 1, 1)
end_date = date(2019, 1, 19)
delta = timedelta(days=1)

WeekNum = []
Fridays = []
WeekDays = []

# build week list
for Week in range(1, 53, 1): WeekNum.append(Week)

# build fridays list
while start_date <= end_date:
    if start_date.weekday() == 4:
        Fridays.append(start_date)
    start_date += delta


# # build calendar
# # $WeekNum - $WeekDay - $Expiration1 - $Expiration2
# start_date = date(2019, 1, 1)
# end_date = date(2020, 1, 1)
# delta = timedelta(days=1)
#
# i=1
#
# while start_date <= end_date:
#     Calendar = [WeekNum[i], start_date, Fridays[i], Fridays[i+1]]
#     if start_date.weekday() == 0:
#         i = i + 1
#     if start_date.weekday() > 4:
#         start_date += delta
#         continue
#     start_date += delta

strike_obj = []
test = start_date.strftime("%Y-%m-%d")
# if Data file doesn't exist
if os.path.exists('Data/Strikes.txt'):
    with open('Data/Strikes.txt') as json_file:
        data = json.load(json_file)

    strike_obj = jsonpickle.decode(data)

else:
    response = requests.get('https://sandbox.tradier.com/v1/markets/history',
        params={'symbol': 'VXX', 'interval': 'daily', 'start': '2019-05-07', 'end': '2019-05-09'},
        headers={'Authorization': 'Bearer VlksdK7wWMGTOuDtr51sLS2FXBOo', 'Accept': 'application/json'}
    )

    # build object
    response = str(response.content).split('{')
    for line in response:
        line = line.replace('"','').replace('}','')
        if line.startswith('date'):
            line = line.split(',')
            new_line = {}
            for tokens in line:
                if tokens != '':
                    tokens = tokens.split(':')
                    new_line[tokens[0]] = tokens[1]
            strike_obj.append(new_line)

    # save object as json
    with open('Data\Strikes.txt', 'w') as outfile:
        json.dump(jsonpickle.encode(strike_obj), outfile)


import plotly.graph_objects as go

Price = go.Figure()
j=[i['open'] for i in strike_obj]
k=[i['close'] for i in strike_obj]

import itertools
for item in j:
    test = item

for i in j:
    l.append(i)
    l.append

Price.add_trace(go.Scatter(y=j, mode='lines'))
Price.show()


UnderlyingPrice = round(float(strike_obj[0].get('open')) + float(strike_obj[0].get('close'))) / 2
#Build symbol`
symbol = 'VXX' + str(Fridays[2].year) + str(Fridays[2].month) + str(Fridays[2].day) + 'C' + UnderlyingPrice


start_date = date(2019, 1, 7)
end_date = date(2019, 1, 18)
delta = timedelta(days=1)

while start_date <= end_date:
    start_date += delta

response = requests.get('https://sandbox.tradier.com/v1/markets/history',
    params={'symbol': 'VXX190517P00025000', 'interval': 'daily', 'start': '2019-05-07', 'end': '2019-05-09'},
    headers={'Authorization': 'Bearer VlksdK7wWMGTOuDtr51sLS2FXBOo', 'Accept': 'application/json'}
)
json_response = response.json()
print(response.status_code)
print(json_response)