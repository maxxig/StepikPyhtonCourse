n = int(input())
z1 = complex(input())
z2 = complex(input())

print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate() ** (n+1))



# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
#
# d = {n:float(abs(n)) for n in numbers}
# max ={'max': {'compl': numbers[0], 'abs': float(abs(numbers[0]))}}
# for k, v in d.items():
#     if v > max.get('max').get('abs'):
#         max['max']['compl'] = k
#         max['max']['abs'] = v
# print(max['max']['compl'])
# print(max['max']['abs'])



# #max = max(numbers, lambda n: abs(complex(n)))
# max = 0.0
# for n in numbers:
#     z = abs(n)
#     if z > max:
#         max = z
# print(max)
# # print(max)

# z1 = complex(input())
# z2 = complex(input())
#
# print(f'{z1} + {z2} = {z1 + z2}')
# print(f'{z1} - {z2} = {z1 - z2}')
# print(f'{z1} * {z2} = {z1 * z2}')