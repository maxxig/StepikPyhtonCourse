timur = 'камень'
ruslan = 'ножницы'
# dict={'ящерица' : 0, 'ножницы' : 1, 'бумага' : 2, 'ящерица':3, 'Спок' : 4}
dict={ 0:'камень', 1:'ножницы' , 2:'бумага', 3:'ящерица', 4:'Спок'}
ind_timur = -2
ind_ruslan = -2
for i, name in dict.items():
    if name == timur:
        ind_timur = i
for i, name in dict.items():
    if name == ruslan:
        ind_ruslan = i
print(ind_timur)
print(ind_ruslan)
r=[
   # к  н  б  я  с
    [ 0, 1,-1, 1,-1],   #к
    [-1, 0, 1, 1,-1],    #н
    [ 1,-1, 0,-1, 1],    #б
    [-1,-1, 1, 0, 1],    #я
    [ 1, 1,-1,-1, 0]     #с
]
if(r[ind_timur][ind_ruslan] == 1):
    print('Тимур')
elif(r[ind_timur][ind_ruslan] == -1):
    print('Руслан')
elif(r[ind_timur][ind_ruslan] == 0):
    print('ничья')