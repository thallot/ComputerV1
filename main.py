import sys
import math
from fractions import Fraction

class Element(object):
    """docstring for Element."""

    def __init__(self, arg, i):
        self.value = float(arg[i - 2])
        if i > 2 and arg[i - 3] == '-':
            self.value *= -1
            self.sign = ' - '
        else:
            self.sign = ' + '
        self.degree = int(arg[i].split('^')[1])

    def __sub__ (self, nb):
        """Quand on soustrait deux objets"""
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

def GetParam(arg):
    """ Recup les nombre et leur exposant puis les insert dans une lister """
    calcul = arg.split('=')
    BeforeEqual = calcul[0].split()
    values = []
    push = 0
    for i, elem in enumerate(BeforeEqual):
        if "X^" in elem and i >= 2:
            values.append(Element(BeforeEqual, i))
    if len(calcul) == 1:
        print('No equal sign')
        exit()
    AfterEqual = calcul[1].split()
    for i, elem in enumerate(AfterEqual):
        if "X^" in elem and i >= 2:
            for elm in values:
                if elm.degree == int(AfterEqual[i].split('^')[1]):
                    elm = elm - float(AfterEqual[i - 2])
                    push = 1
            if push == 0:
                values.append(Element(AfterEqual, i))
    if (len(values) == 0):
        print("Wrong input")
        exit()
    values.sort( key=lambda Element: Element.degree)
    values[0].sign = ''
    return (values)

if __name__ == "__main__":

    if len(sys.argv) == 1:
        arg = input('Entrez votre polynome\n')
        try:
            values = GetParam(arg)
        except(ValueError, NameError):
            print ("Oops!  That was no valid equation")
            exit()
    else:
        try:
            values = GetParam(sys.argv[1])
        except(ValueError, NameError):
            print ("Oops!  That was no valid equiation")
            exit()
    a = float(0)
    b = float(0)
    c = float(0)
    MaxDegree = values[len(values) - 1].degree
    print("Polynomial degree:", MaxDegree)
    if MaxDegree == 0:
        print("All reel numbers are solution")
        exit()
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
    if MaxDegree == 1:
        print('The solution is:')
        if b == 0:
            print("All reel numbers are solution")
        else:
            print(c/b * -1)
    elif MaxDegree == 2:
        delta = b*b-4*a*c
        if (delta > 0):
            print('Discriminant is strictly positive, the two solutions are:')
            racineDelta = math.sqrt(delta)
            res = (-b-racineDelta)/(2*a)
            print('%9.6f | Fraction : ' %res, Fraction(res).limit_denominator(1000))
            res =(-b+racineDelta)/(2*a)
            print('%9.6f | Fraction : ' %res, Fraction(res).limit_denominator(1000))
        elif delta == 0:
            print('Discriminant is strictly null, the two solutions are:')
            res =-b/(2*a)
            print('%9.6f | Fraction : ' %res, Fraction(res).limit_denominator(1000))
        else:
            print('Discriminant is strictly nagative, there is no solution')
    elif MaxDegree == 3:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
