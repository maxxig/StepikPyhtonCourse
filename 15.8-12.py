from functools import reduce
def evaluate(coefficients, x):
    max_mult = len(coefficients) - 1
    coefficients2 = map(lambda k: (k[1],  max_mult - k[0]), enumerate(map(int, coefficients)))
    print(reduce(lambda n1, n2: n1 + n2[0] if n2[1] == 0 else n1 + n2[0] * x ** n2[1], coefficients2,0))

evaluate(input().split(),int(input()))