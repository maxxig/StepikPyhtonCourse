#6.3-1
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# res = 1
# for i in numbers:
#     res = res * i
# print(res)


#6.3-2
# numbers = (
# data = 'Python для продвинутых!'
#
# print(tuple(data))


#6.3-3
# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = poet_data[:-1] + ('Москва',)
#
# print(poet_data)

#6.3-4
# import statistics
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
# print([statistics.mean(list(i)) for i in numbers])
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# res =[]
# for i in numbers:
#     res.append(sum(i)/len(i))
# print(res)

#6.3-4
# a = int(input())
# b = int(input())
# c = int(input())
# res = (-(b/(2*a)), (4*a*c-b*b)/(4*a))
# print(res)

# n = int(input())
# clas = ()
# arr =[]
# for i in range(n):
#     student = input().split()
#     t = (student[0], int(student[1]))
#     arr.append(t)
#
# for i in arr:
#     print(i[0], i[1])
# print()
# for i in arr:
#     if i[1]>3:
#         print(i[0], i[1])

# n = int(input())
# f1, f2, f3 = 1,1,1
# for i in range(n):
#     print(f1, end =' ')
#     f1, f2, f3 = f2, f3, f3 + f2 + f1

# a, b, c = 'Beegeek loves Stepik'.split()
# print(b)

n,m,k,x,y,z = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
print((n-x)+x+(m-x-y)+y+(k-y)+z)