import os
import pandas as pd
import numpy as np
from scipy.special import erf
from Utilities import IV, create_option_symbol, weeks, calc_closest_strike
from datetime import date, timedelta, datetime
import plotly.graph_objects as go


year = 2019
month = 10
day = 18
r = 0.0159
IV = .6

option_exp = date(year, month, day)

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
for IV in range(1,2000,1):
    IV = IV/1000
    BlackSchules['calc_call_price_' + str(IV)] = (BlackSchules['Underlying_close'] * ((1.0 + erf(((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp']))) / np.sqrt(2.0))) / 2.0)) - (BlackSchules['closest_strike'] * np.exp(-r*BlackSchules['t_exp']) * ((1.0 + erf((((BlackSchules['nlog'] + (r+((IV*IV)/2))*BlackSchules['t_exp']) / (IV*np.sqrt(BlackSchules['t_exp']))) - (IV*np.sqrt(BlackSchules['t_exp']))) / np.sqrt(2.0))) / 2.0))

program = 'done'





# #vol = df.applymap(lambda (df['Underlying_open'], df['Underlying_close']))
# fig = go.Figure()
#
# fig.add_trace(go.Scatter(x=df.date, y=df['25.0_close']))
#
# fig.update_layout(xaxis_range=['2019-06-25','2019-10-18'],
#                   title_text="Manually Set Date Range")
# fig.show()

