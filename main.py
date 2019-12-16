""" Calculatrice de polynome : Computor V1

Bonus : Forme fraction
        Forme réduite sans X^0 et X^1
        Le parsing retourne un message en cas d'erreur
        Ajout de -v (verbose) qui affiche les calculs
"""

import sys
from fractions import Fraction
from parsing import *

def ReducedForm(values):
    """ Retourne a b et c. Puis affiche l'équation sous forme réduite """
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

def printReducedForm(values):
    i = 2
    print('Reduced Form :', end=' ')
    while i >= 0:
        if values[i] != 0 and i == 2:
            print('%+dX^2' %values[i], end = ' ')
        elif values[i] != 0 and i == 1:
            print('%+dX' %values[i], end = ' ')
        if values[i] != 0 and i == 0:
            print('%+dX' %values[i], end = ' ')
        i -= 1
    print('= 0')

if __name__ == "__main__":
    """ Main fonction : Donne le resultat d'un polynome """
    verbose, values, MaxDegree = ParseParam(sys)
    a = values[2]
    b = values[1]
    c = values[0]
    printReducedForm(values)
    print("Polynomial degree:", MaxDegree)
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
            if verbose == 1:
                print("\nCalcul : \n")
                print("     Result = -( " + str(c) + " / " + str(b) + ")")
                print("     Result = " + str(c/b * -1))
            else:
                print(c/b * -1)
    elif MaxDegree == 2:
        delta = (b*b)-(4*a*c)
        if (delta > 0):
            racineDelta = delta ** 0.5
            ResOne = ((b * -1) - racineDelta) / (2 * a)
            ResTwo = ((b * -1) + racineDelta) / (2 * a)
            if verbose == 1:
                print("\nCalcul : \n")
                print("     Delta = (" + str(b) + ")² - 4 * " + str(a) + " * " + str(c))
                print("     Delta = %.2f\n" %delta)
                print("     R1 = (-" + str(b) + " - √" + str(delta) + ") / (2 * " + str(a) + ")")
                print("     R1 = " + str(round(racineDelta - b, 2)) + " / " + str(2 * a))
                print("     R1 = %.2f\n" %ResOne)
                print("     R2 = (-" + str(b) + " + √" + str(delta) + ") / (2 * " + str(a)  + ")")
                print("     R1 = " + str(round(racineDelta - b, 2))+ " / " + str(2 * a))
                print("     R2 = %.2f\n" %ResTwo)
            print('Discriminant is strictly positive, the two solutions are:')
            print('%9.6f | Fraction : ' %ResOne, Fraction(ResOne).limit_denominator(100))
            print('%9.6f | Fraction : ' %ResTwo, Fraction(ResTwo).limit_denominator(100))
        elif delta == 0:
            res =-b/(2*a)
            print('Discriminant is strictly null, the two solutions are:')
            print('%9.6f | Fraction : ' %res, Fraction(res).limit_denominator(1000))
        else:
            print('Discriminant is strictly negative, the two solutions are:')
            print('-' + str(int(b)) + ' + i√' + str(delta) + ' / 2 * ' + str(int(a)))
            print('-' + str(int(b)) + ' - i√' + str(delta) + ' / 2 * ' + str(int(a)))
    elif MaxDegree == 3:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
