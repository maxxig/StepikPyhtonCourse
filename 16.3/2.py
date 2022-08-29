from functools import reduce
def product_of_odds(data):
    f = list(filter(lambda x: x % 2 == 1, data))
    res = reduce(lambda x, y: x * y , f, 1)
    return res

# def product_of_odds(data):   # data - список целых чисел
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result

print(product_of_odds([1,2,3,4,5,6]))

