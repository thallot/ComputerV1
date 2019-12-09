import sys
from fractions import Fraction
from parsing import *

def ReducedForm(values):
    a = float(0)
    b = float(0)
    c = float(0)
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
    return (a,b,c)

if __name__ == "__main__":

    if len(sys.argv) == 1:
        arg = input('Entrez votre polynome\n')
        values = GetParam(arg)
    else:
        values = GetParam(sys.argv[1])

    MaxDegree = values[len(values) - 1].degree
    print("Polynomial degree:", MaxDegree)
    a, b, c = ReducedForm(values)
    if MaxDegree == 0:
        if c == 0:
            print("All reel numbers are solution ( ∀ x ∈ ℝ  x est solution)")
        else:
            print('The solution is:\n0')
    elif MaxDegree == 1:
        print('The solution is:')
        if b == 0 and c !=0:
            print("0")
        elif b == 0 and c == 0:
            print("All reel numbers are solution ( ∀ x ∈ ℝ  x est solution)")
        else:
            print(c/b * -1)
    elif MaxDegree == 2:
        delta = (b*b)-(4*a*c)
        if (delta > 0):
            racineDelta = delta ** 0.5
            ResOne = ((b * -1) - racineDelta) / (2 * a)
            ResTwo = ((b * -1) + racineDelta) / (2 * a)
            print('Discriminant is strictly positive, the two solutions are:')
            print('%9.6f | Fraction : ' %ResOne, Fraction(ResOne).limit_denominator(1000))
            print('%9.6f | Fraction : ' %ResTwo, Fraction(ResTwo).limit_denominator(1000))
        elif delta == 0:
            res =-b/(2*a)
            print('Discriminant is strictly null, the two solutions are:')
            print('%9.6f | Fraction : ' %res, Fraction(res).limit_denominator(1000))
        else:
            print('Discriminant is strictly negative, the two solutions are:')
            print('-' + str(int(a)) + ' + i√' + str(delta) + ' / 2 * ' + str(int(a)))
            print('-' + str(int(a)) + ' - i√' + str(delta) + ' / 2 * ' + str(int(a)))
    elif MaxDegree == 3:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
