# Version 3.6.1
import requests
import datetime

today = datetime.datetime.now()

today_fmt = str(today.year) + "-" + str(today.month) + "-" + str(today.day)
today_fmt = str(today.year) + "-" + str(today.month) + "-" + str(18)
response = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
    params={'symbol': 'VXX', 'expiration': today_fmt},
    headers={'Authorization': 'Bearer VlksdK7wWMGTOuDtr51sLS2FXBOo', 'Accept': 'application/json'}
)
json_response = response.json()

json_response = json_response.split(',')
for i in json_response:
    print(i)
