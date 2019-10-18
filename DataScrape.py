import requests
import datetime

from datetime import date, timedelta

start_date = date(2019, 1, 1)
end_date = date(2020, 1, 1)
delta = timedelta(days=1)
WeekDays = []
Fridays = []
while start_date <= end_date:
    if start_date.weekday() == 4:
        Fridays.append(start_date)
    if start_date.weekday() < 5:
        WeekDays.append(start_date)
    start_date += delta

#Build symbol
symbol = 'VXX' + Fridays[i].year + Fridays[i].month + Fridays[i].day + 'C' + UnderlyingPrice

response = requests.get('https://sandbox.tradier.com/v1/markets/history',
    params={'symbol': 'VXX', 'expiration': '2019-05-07'},
    headers={'Authorization': 'Bearer VlksdK7wWMGTOuDtr51sLS2FXBOo', 'Accept': 'application/json'}
)
json_response = response.json()
print(response.status_code)
print(json_response)


response = requests.get('https://sandbox.tradier.com/v1/markets/history',
    params={'symbol': 'VXX190517P00025000', 'interval': 'daily', 'start': '2019-05-07', 'end': '2019-05-09'},
    headers={'Authorization': 'Bearer VlksdK7wWMGTOuDtr51sLS2FXBOo', 'Accept': 'application/json'}
)
json_response = response.json()
print(response.status_code)
print(json_response)