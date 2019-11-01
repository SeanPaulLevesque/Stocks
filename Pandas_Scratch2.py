import os
import pandas as pd
import numpy as np
from scipy.special import erf
from Utilities import IV, create_option_symbol, weeks, calc_closest_strike
from datetime import date, timedelta, datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots


year = 2019
month = 9
day = 20
r = 0.0159
IV = .6

option_exp = date(year, month, day)
delta = timedelta(days=15)
ticker = create_option_symbol(25, option_exp, 'C')

df = pd.read_csv('Pandas/Quotes/' + str(ticker[0:9]) + 'C.txt', index_col='date')


Call_Thing = pd.DataFrame(round(df.Underlying_open + df.Underlying_close)/2, columns=['closest_strike'])
Call_Thing['closest_strike'] = Call_Thing['closest_strike'].astype(str) + '_close'

df_dict = df.to_dict()
Call_dict = Call_Thing.to_dict()
test = []
for key,val in Call_Thing['closest_strike'].items():
    if float(val.split('_')[0]) > 29:
        test.append('nan')
        continue
    test.append(df_dict[val][key])


BlackSchules = pd.DataFrame(round(df.Underlying_open + df.Underlying_close)/2, columns=['closest_strike'])
BlackSchules['Underlying_close'] = df.Underlying_close
BlackSchules['Call_Price'] = test
BlackSchules['nlog'] = np.log(BlackSchules['Underlying_close']/BlackSchules['closest_strike'])
BlackSchules['t_exp'] = ((pd.to_datetime(option_exp) - pd.to_datetime(BlackSchules.index)).days)/253
BlackSchules.replace(["NaN", 'NaT', "nan"], np.nan, inplace = True)
BlackSchules = BlackSchules.dropna()
BlackSchules['IV'] = np.sqrt((2*np.pi)/BlackSchules['t_exp']) * (BlackSchules['Call_Price']/BlackSchules['closest_strike'].dropna())
# for index, row in BlackSchules.iterrows():
#     test = 'done'
# BlackSchules['d1'] = ((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp'])))
# BlackSchules['d2'] = (BlackSchules['d1'] - (IV*np.sqrt(BlackSchules['t_exp'])))
# BlackSchules['phi_d1'] = ((1.0 + erf(BlackSchules['d1'] / np.sqrt(2.0))) / 2.0)
# BlackSchules['phi_d2'] = ((1.0 + erf(BlackSchules['d2'] / np.sqrt(2.0))) / 2.0)
# BlackSchules['calc_call_price'] = (BlackSchules['Underlying_close'] * BlackSchules['phi_d1']) - (BlackSchules['closest_strike'] * np.exp(-r*BlackSchules['t_exp']) * BlackSchules['phi_d2'])

#
# BlackSchules['d1'] = ((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp'])))
# BlackSchules['d2'] = (((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp']))) - (IV*np.sqrt(BlackSchules['t_exp'])))
# BlackSchules['phi_d1'] = ((1.0 + erf(((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp']))) / np.sqrt(2.0))) / 2.0)
# BlackSchules['phi_d2'] = ((1.0 + erf((((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp']))) - (IV*np.sqrt(BlackSchules['t_exp']))) / np.sqrt(2.0))) / 2.0)
# for IV in range(1, 2000, 1):
#     IV = IV/1000
#     BlackSchules['calc_call_price_' + str(IV)] = (BlackSchules['Underlying_close'] * ((1.0 + erf(((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp']))) / np.sqrt(2.0))) / 2.0)) - (BlackSchules['closest_strike'] * np.exp(-r*BlackSchules['t_exp']) * ((1.0 + erf((((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp']))) - (IV*np.sqrt(BlackSchules['t_exp']))) / np.sqrt(2.0))) / 2.0))
#

# print(0.039525691699604744 in BlackSchules.values)
# test = BlackSchules.loc['2019-10-08'][5]
# print(test)
# print(BlackSchules.loc['2019-10-08'].where(BlackSchules.loc['2019-10-08'] == test))

# 0.75602

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x=BlackSchules.index, y=BlackSchules['IV'], name="IV"), secondary_y=True)
#fig.add_trace(go.Scatter(x=BlackSchules.index, y=BlackSchules['Call_Price'], name="Call Price"), secondary_y=True)
fig.add_trace(go.Scatter(x=BlackSchules.index, y=BlackSchules['closest_strike'], name="Strike Price"),secondary_y=False)
fig.add_trace(go.Scatter(x=df.index, y=df['23.5_close'], name="23.5C Price"),secondary_y=True)
fig.update_layout(xaxis_range=[option_exp - delta,option_exp],
                  title_text="Expiration" + str(month)+str(day))
fig.show()

program = 'done'