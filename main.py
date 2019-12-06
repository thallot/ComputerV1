import sys
import math

class Element(object):
    """docstring for Element."""

    def __init__(self, arg, i):
        self.value = float(arg[i - 2])
        if i > 2 and arg[i - 3] == '-':
            self.value *= -1
            self.sign = ' - '
        else:
            self.sign = ' + '
        self.valueAbs = abs(float(arg[i - 2]))
        self.degree = int(arg[i].split('^')[1])

    def __sub__ (self, nb):
        """Quand on soustrait deux objets"""
        self.value -= nb

    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "{}{} * X^{}".format(self.sign, formatNumber(self.valueAbs), self.degree)

def formatNumber(num):
    """ Pour enlever les 0 inutiles sur les float """
    if num % 1 == 0:
        return int(num)
    else:
        return num

def get_param(arg):
    calcul = arg.split('=')
    BeforeEqual = calcul[0].split()
    values = []
    push = 0
    for i, elem in enumerate(BeforeEqual):
        if "X^" in elem and i >= 2:
            values.append(Element(BeforeEqual, i))
    AfterEqual = calcul[1].split()
    for i, elem in enumerate(AfterEqual):
        if "X^" in elem and i >= 2:
            for elem in values:
                if elem.degree == int(AfterEqual[i].split('^')[1]):
                    elem = elem - float(AfterEqual[i - 2])
                    push = 1
                if push == 0:
                    values.append(Element(AfterEqual, i))
    values.sort( key=lambda Element: Element.degree)
    values[0].sign = ''
    for elem in values:
        print('|', elem)
    return (values)

if len(sys.argv) == 1:
    arg = input('Entrez votre polynome\n')
    values = get_param(arg)
else:
    values = get_param(sys.argv[1])

a = float(0)
b = float(0)
c = float(0)
MaxDegree = values[len(values) - 1].degree
print("Polynomial degree:", MaxDegree)
print("Reduced form:", end=' ')
for i, elem in enumerate(values):
    if (elem.degree == 0):
        c = elem.value
    elif (elem.degree == 1):
        b = elem.value
    elif (elem.degree == 2):
        a = elem.value
    print(elem, end='')
print(' = 0')
delta = b*b-4*a*c
if (delta > 0):
    racineDelta = math.sqrt(delta)
    print('Discriminant is strictly positive, the two solutions are:')
    res = (-b-racineDelta)/(2*a)
    print(res)
    res2 =(-b+racineDelta)/(2*a)
    print(res2)
