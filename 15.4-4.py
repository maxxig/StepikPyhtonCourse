athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
s = int(input())

def mysort(val):
    return val[s-1]

athletes = sorted(athletes, key=mysort)

for at in athletes:
    print(f'{at[0]} {at[1]} {at[2]} {at[3]}')