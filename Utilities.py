from datetime import date, timedelta

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

def create_option_symbol(strike, option_exp):

    strike = '000' + str(strike).replace('.','') + '00'
    # Build symbol`
    symbol = 'VXX' + str(option_exp.year)[2:4] + str(option_exp.month) + str(option_exp.day) + 'C' + strike

    return symbol
