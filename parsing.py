class Element(object):
    """docstring for Element."""
    def __init__(self, value, degree, sign):
        self.value = value
        self.degree = degree
        self.sign = sign

    def __sub__ (self, nb):
        """Quand on soustrait deux objets"""
        if self.value >= 0 and self.value - nb < 0:
            self.sign = ' - '
        if self.value < 0 and self.value - nb >= 0:
            self.sign = ' + '
        self.value -= nb

    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "{}{} * X^{}".format(self.sign, formatNumber(abs(self.value)), self.degree)

def formatNumber(num):
    """ Pour enlever les 0 inutiles sur les float """
    if num % 1 == 0:
        return int(num)
    else:
        return num

def GetData(arg, i):
    """ Retourne le nombre, son signe et son exposant """
    try:
        value = float(arg[i - 2])
    except ValueError:
        print('4 Mauvais type de données : ' + BeforeEqual[i - 2])
        exit()
    try:
        degree = int(arg[i].split('^')[1])
    except:
        print('3 Mauvais type de données : ' + BeforeEqual[i].split('^')[1])
        exit()
    if i > 2 and arg[i - 3] == '-':
        value *= -1
        sign = ' - '
    else:
        sign = ' + '
    return value, degree, sign


def GetParam(arg):
    """ Recup les nombre et leur exposant puis les insert dans une liste """
    calcul = arg.split('=')
    BeforeEqual = calcul[0].split()
    values = []
    push = 0
    if len(calcul) == 1:
        print('No equal sign')
        exit()
    for i, elem in enumerate(BeforeEqual):
        if "X^" in elem and i >= 2:
            value, degree, sign = GetData(BeforeEqual, i)
            values.append(Element(value, degree, sign))
    AfterEqual = calcul[1].split()
    for i, elem in enumerate(AfterEqual):
        if "X^" in elem and i >= 2:
            for elm in values:
                nb, degree, sign = GetData(AfterEqual, i)
                if degree == elm.degree:
                    elm = elm - nb
                    push = 1
            if push == 0:
                value, degree, sign = GetData(AfterEqual, i)
                value *= -1
                if sign == ' + ':
                    sign = ' - '
                else:
                    sign = ' + '
                values.append(Element(value, degree, sign))
    if (len(values) == 0):
        print("Wrong input")
        exit()
    values.sort( key=lambda Element: Element.degree)
    values[0].sign = ''
    return (values)
