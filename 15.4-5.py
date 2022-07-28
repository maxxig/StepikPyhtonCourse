import math
def kvadrat(x):
    return x**2
def cube(x):
    return x**3
def koren(x):
    return x**0.5
def modul(x):
    return abs(x)
def sinus_func(x):
    return math.sin(x)

dict = {'квадрат': kvadrat, 'куб': cube, 'корень': koren, 'модуль': modul, 'синус':sinus_func}

val = int(input())
f = input()
print(dict[f](val))