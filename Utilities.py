from datetime import date, timedelta
import math

def parse_JSON(response):
    strike_obj = {}
    response = str(response.content).split('{')
    for line in response:
        line = line.replace('"','').replace('}','')
        if line.startswith('date'):
            line = line.split(',')
            new_line = {}
            for tokens in line:

                if tokens != '':
                    if tokens.startswith('date'):
                        tokens = tokens.split(':')
                        date = tokens[1]
                        #tokens[1] = tokens[1].split('-')
                        #new_line[tokens[0]] = date(int(tokens[1][0]), int(tokens[1][1]), int(tokens[1][2]))
                    else:
                        tokens = tokens.split(':')
                        new_line[tokens[0]] = tokens[1]
            strike_obj[date] = new_line
            #strike_obj.append(new_line)

    return strike_obj

def create_option_symbol(strike, option_exp, cp):

    month = str(option_exp.month)
    day = str(option_exp.day)

    # format date
    if len(month) < 2:
        month = '0' + month
    if len(day) < 2:
        day = '0' + day

    strike = '000' + str(strike).replace('.','') + '00'
    # Build symbol`
    symbol = 'VXX' + str(option_exp.year)[2:4] + month + day + cp + strike

    return symbol

def phi(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def Average(lst):
    return sum(lst) / len(lst)

def IV(S, X, call_price, r, exp, curr_date):
    T = int((exp - curr_date).days) / 253
    S = float(S)
    call_price = float(call_price)
    k = []
    for i in range(1, 3000, 1):

        IV = i/1000

        nLog = math.log(S/X)
        d1 = (nLog + (r+((IV*IV)/2))*T) / (IV*math.sqrt(T))
        d2 = d1 - (IV*math.sqrt(T))

        call = (S * phi(d1)) - (X * math.exp(-r*T) * phi(d2))
        if round(call,2) == call_price:
            # getting close
            k.append(IV)
    if k != []:
        k = Average(k)
    else:
        k = 1
    return k


def IV2(S, X, call_price, put_price, r, exp, curr_date):

    # S is stock price
    # X is strike price
    T = int((exp - curr_date).days) / 365
    S = float(S)
    call_price = float(call_price)
    put_price = float(put_price)
    Ft = X + (math.exp(r * T) * call_price) - (math.exp(r * T) * put_price)
    for IV in range(100,1000,1):
        IV = IV/1000
        moneyness = (math.log(X / Ft)) / (IV * math.sqrt(T))
        print(moneyness)
    IV = (math.log(X / Ft)) / ((S/X) * math.sqrt(T))

    return IV

