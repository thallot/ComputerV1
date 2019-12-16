import re

class Variable(object):
    """docstring for Variable."""
    def __init__(self, string, revSign = False):
        try:
            self.value, self.degree, self.sign = self.getValue(string, revSign)
        except:
            print("Invalid Input")
            exit()

    def __repr__(self):
        return ('{} * X ^ {}' .format(self.value, self.degree))

    def getValue(self, string, revSign):
        """ Recupere le signe, la valeur et l'exposant d'un element """
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
    param = [0, 0]
    if len(sys.argv) == 1:
        arg = input('> Enter data\n')
        values, MaxDegree = GetParam(arg)
    else:
        if len(sys.argv) == 2:
            if sys.argv[1][0] == '-':
                if 'v' in sys.argv[1]:
                    param[0] = 1
                if 'd' in sys.argv[1]:
                    param[1] = 1
                arg = input('> Enter data\n')
                values, MaxDegree = GetParam(arg)
            else:
                param, values, MaxDegree = GetParam(sys.argv[1])
        else:
            if sys.argv[1][0] == '-':
                if 'v' in sys.argv[1]:
                    param[0] = 1
                if 'd' in sys.argv[1]:
                    param[1] = 1
                values, MaxDegree = GetParam(sys.argv[2])
            elif sys.argv[2][0] == '-':
                if 'v' in sys.argv[2]:
                    param[0] = 1
                if 'd' in sys.argv[2]:
                    param[1] = 1
                values, MaxDegree = GetParam(sys.argv[1])
            else:
                print('Usage : \n python3 main.py [-v]["Equation"]')
                exit()
    return param, values, MaxDegree

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
    values.sort(key=lambda Variable: Variable.degree)
    for i, token in enumerate(values):
        if i + 1 < len(values) and values[i].degree == values[i + 1].degree:
            values[i].value += values[i + 1].value
            del values[i + 1]
    if not len(values):
        MaxDegree = -1
    else:
        MaxDegree = values[-1].degree
    return values, MaxDegree
