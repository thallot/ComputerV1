class Element(object):
    """docstring for Element."""
    def __init__(self, arg, i):
        try:
            self.value = float(arg[i - 2])
        except ValueError:
            print('Mauvais type de données : ' + arg[i - 2])
            exit()
        if i > 2 and arg[i - 3] == '-':
            self.value *= -1
            self.sign = ' - '
        else:
            self.sign = ' + '
        try:
            self.degree = int(arg[i].split('^')[1])
        except:
            print('Mauvais type de données : ' + arg[i].split('^')[1])
            exit()

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
    """ Recup les nombre et leur exposant puis les insert dans une liste """
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
                try:
                    degree = int(AfterEqual[i].split('^')[1])
                except:
                    print('Mauvais type de données : ' + AfterEqual[i].split('^')[1])
                    exit()
                if elm.degree == degree:
                    try:
                        nb = float(AfterEqual[i - 2])
                    except:
                        print('Mauvais type de données : ' + AfterEqual[i - 2])
                        exit()
                    elm = elm - nb
                    push = 1
            if push == 0:
                values.append(Element(AfterEqual, i))
    if (len(values) == 0):
        print("Wrong input")
        exit()
    values.sort( key=lambda Element: Element.degree)
    values[0].sign = ''
    return (values)
