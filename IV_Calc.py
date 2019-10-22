import math

def phi(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

#20.85
# ATM strike price
k = 20.5
# risk free rate
r = 0.0159
# annualized time to maturity
T = 5/265
# ATM call price
C = .65
# ATM put price
P = .31
# implied forward price
Ft = k + (math.exp(r*T)*C)-(math.exp(r*T)*P)

IV = (math.log(X / Ft)) / ((20.85 / 20.5) * math.sqrt(T))
print(IV)
IV = (math.log(X / Ft)) / ((20.5 / 20.85) * math.sqrt(T))
print(IV)
IV = ((S / X) * math.sqrt(T))

IV = .5297
for IV in range(200,2000,1):
    IV = IV/1000
    moneyness = (math.log(20.5/21.29))/(IV*math.sqrt(T))
    print(moneyness)


IV = (math.log(k / Ft)) / ((Ft - k) * math.sqrt(T))

# ATM strike price
k = 21
# risk free rate
r = 0.0159
# annualized time to maturity
T = 7/265
# ATM call price
C = .73
# ATM put price
P = .48
# implied forward price
Ft = k + (math.exp(r*T)*C)-(math.exp(r*T)*P)

IV = .5297
moneyness = (math.log(k/Ft))/(IV*math.sqrt(T))


prgram = 'done'
#
#
# #Current Stock price
# S = 21.74
# #Strike Price
# X = 21.5
# #Rate%
# r =
# #Time in days
# T=17/365
# #Implied Volatility
# #IV=.5659
#
# #Call Price
# C1 = 1.19
#
#
# for i in range(500,800,1):
#     IV = i/1000
#
#     nLog = math.log(S/X)
#     d1 = (nLog + (r+((IV*IV)/2))*T) / (IV*math.sqrt(T))
#     d2 = d1 - (IV*math.sqrt(T))
#
#     call = (S * phi(d1)) - (X * math.exp(-r*T) * phi(d2))
#     if round(call,2) == C1:
#         print(str(IV) + " " + str(call))
#
# # put = ((X * math.exp(-r*T) * phi(-d2)) - (S * phi(-d1)))




