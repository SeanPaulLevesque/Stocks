import math
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='SeanPaulLevesque', api_key='mr74MhGpGMkdVlJuV20c')
#
# def phi(x):
#     #'Cumulative distribution function for the standard normal distribution'
#     return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
#
# #Current Stock price
# S = 281.07
# #Strike Price
# X = 282
# #Rate%
# r=0
# #Time in days
# T=3/365
# #Implied Volatility
# IV=.1608
#
# output = list(range(int(S-10),int(S+10)))
# print(output)
#
# nLog = math.log(S/X)
# d1 = (nLog + (r+((IV*IV)/2))*T) / (IV*math.sqrt(T))
# d2 = d1 - (IV*math.sqrt(T))
#
# call = (S * phi(d1)) - (X * math.exp(-r*T) * phi(d2))
# put = ((X * math.exp(-r*T) * phi(-d2)) - (S * phi(-d1)))
#
# calls = []
# puts = []
# profit = []
#
# for i in output:
#     S = i
#     nLog = math.log(S / X)
#     d1 = (nLog + (r + ((IV * IV) / 2)) * T) / (IV * math.sqrt(T))
#     d2 = d1 - (IV * math.sqrt(T))
#     calls.append(((S * phi(d1)) - (X * math.exp(-r*T) * phi(d2))) - call)
#     puts.append(((X * math.exp(-r * T) * phi(-d2)) - (S * phi(-d1))) - put)
#
# from operator import add
# profit = list(map(add,calls,puts))
#
#
#
# # Create a trace
# trace1 = go.Scatter(
#     x = output,
#     y = profit
# )
#
# T = T=2/365
#
# nLog = math.log(S/X)
# d1 = (nLog + (r+((IV*IV)/2))*T) / (IV*math.sqrt(T))
# d2 = d1 - (IV*math.sqrt(T))
#
# call = (S * phi(d1)) - (X * math.exp(-r*T) * phi(d2))
# put = ((X * math.exp(-r*T) * phi(-d2)) - (S * phi(-d1)))
#
# calls = []
# puts = []
# profit = []
#
# for i in output:
#     S = i
#     nLog = math.log(S / X)
#     d1 = (nLog + (r + ((IV * IV) / 2)) * T) / (IV * math.sqrt(T))
#     d2 = d1 - (IV * math.sqrt(T))
#     calls.append(((S * phi(d1)) - (X * math.exp(-r*T) * phi(d2))) - call)
#     puts.append(((X * math.exp(-r * T) * phi(-d2)) - (S * phi(-d1))) - put)
#
# from operator import add
# profit = list(map(add,calls,puts))
#
# # Create a trace
# trace2 = go.Scatter(
#     x = output,
#     y = profit
# )
#
# data = [trace1, trace2]
#
# py.iplot(data, filename='basic-line')
#
# # import http.client
# #
# # connection = http.client.HTTPSConnection('sandbox.tradier.com', 443, timeout = 30)
# #
# # # Headers
# # headers = {"Accept":"application/json",
# #            "Authorization":"Bearer 8akbH7cl7JD6r5c0bkDu7VkvvOwt"}
# #
# # # Send synchronously
# # connection.request('GET', '/v1/markets/quotes?symbols=spy', None, headers)
# #
# # try:
# #   response = connection.getresponse()
# #   content = response.read()
# #   print(content)
# #   # Success
# #   print('Response status ' + str(response.status))
# # except:
# #     print('Exception during request')
#



WeekNum = []
Fridays = []
WeekDays = []

# build week list
for Week in range(1, 53, 1): WeekNum.append(Week)

# build fridays list
start_date_1 = start_date
while start_date_1 <= end_date:
    if start_date.weekday() == 4:
        Fridays.append(start_date)
    start_date_1 += delta


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
