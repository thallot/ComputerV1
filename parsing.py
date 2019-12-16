import re

class Variable(object):
    """docstring for Element."""
    def __init__(self, string, revSign = False):
        try:
            self.value, self.degree, self.sign = self.getValue(string, revSign)
        except:
            print("Invalid Input")
            exit()

    def getValue(self, string, revSign):
        tmp = string.replace('*', '').replace('^', '').split('X')
        value = float(tmp[0])
        degree = int(tmp[1])
        if revSign:
            value = -value
        if value >= 0:
            sign = '+'
        else:
            sign = '-'
        return value, degree, sign

def formatNumber(num):
    """ Pour enlever les 0 inutiles sur les float """
    if num % 1 == 0:
        return int(num)
    else:
        return num

def ParseParam(sys):
    """ Parse les parametre en entrée et retourne le resultat"""
    verbose = 0
    if len(sys.argv) == 1:
        arg = input('> Enter data\n')
        values, MaxDegree = GetParam(arg)
    else:
        if len(sys.argv) == 2:
            values, MaxDegree = GetParam(sys.argv[1])
        else:
            if sys.argv[1] == '-v':
                verbose = 1
                values, MaxDegree = GetParam(sys.argv[2])
            elif sys.argv[2] == '-v':
                verbose = 1
                values, MaxDegree = GetParam(sys.argv[1])
            else:
                print('Usage : \n python3 main.py [-v]["Equation"]')
                exit()
    return verbose, values, MaxDegree

def GetParam(arg):
    """ Recup les nombre et leur exposant puis les insert dans une liste """
    calcul = arg.split('=')
    if len(calcul) == 1:
        print('No equal sign')
        exit()
    Before = calcul[0].replace(' ', '')
    After = calcul[1].replace(' ', '')
    BeforeEqual = calcul[0].split()
    partOne = re.findall('\-?[\d+\.]*\d+\*X\^*\d*', Before)
    partTwo = re.findall('\-?[\d+\.]*\d+\*X\^*\d*', After)
    values = []
    for token in partOne:
        values.append(Variable(token))
    for token in partTwo:
        values.append(Variable(token, True))
    power = [0.0,0.0,0.0]
    MaxDegree = -2
    if not len(values):
        MaxDegree = -1
    for token in values:
        if token.degree == 0:
            power[0] += token.value
        elif token.degree == 1:
            power[1] += token.value
        elif token.degree == 2:
            power[2] += token.value
        else:
            MaxDegree = token.degree
    if MaxDegree == -1 or MaxDegree == -2:
        if not power[2] == 0:
            MaxDegree = 2
        elif not power[1] == 0:
            MaxDegree = 1
        elif not power[0] == 0:
            MaxDegree = 0
    return power, MaxDegree
