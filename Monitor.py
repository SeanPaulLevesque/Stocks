import requests
from Utilities import parse_option_JSON
from apscheduler.schedulers.blocking import BlockingScheduler
import json
import jsonpickle
from datetime import datetime

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour='9-17', minute=10)
def scheduled_job():

    response = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
                            params={'symbol': 'VXX', 'expiration': '2019-11-1', 'greeks': 'true'},
                            headers={'Authorization': 'Bearer VlksdK7wWMGTOuDtr51sLS2FXBOo',
                                     'Accept': 'application/json'}
                            )
    json_response = response.json()


    curr_time = datetime.now()
    quote_obj = parse_option_JSON(response, curr_time.hour)
    print(str(curr_time))
    # save object as json
    with open('Data/Quotes/Current/' + str(curr_time.hour) + '.txt', 'w') as outfile:
        json.dump(jsonpickle.encode(quote_obj), outfile)

sched.start()