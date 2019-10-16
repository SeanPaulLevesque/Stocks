import math


def phi(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


#Current Stock price
S = 21.74
#Strike Price
X = 21.5
#Rate%
r = 0.0159
#Time in days
T=17/365
#Implied Volatility
#IV=.5659

#Call Price
C1 = 1.19


for i in range(500,800,1):
    IV = i/1000

    nLog = math.log(S/X)
    d1 = (nLog + (r+((IV*IV)/2))*T) / (IV*math.sqrt(T))
    d2 = d1 - (IV*math.sqrt(T))

    call = (S * phi(d1)) - (X * math.exp(-r*T) * phi(d2))
    if round(call,2) == C1:
        print(str(IV) + " " + str(call))

# put = ((X * math.exp(-r*T) * phi(-d2)) - (S * phi(-d1)))
#




