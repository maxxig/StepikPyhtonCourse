n,m,k,x,y,z,t,a = int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
nm2 = n + m - x - t
mk2 = m + k - y - t
nk2 = n + k - z - t
answer1 = (n-nk2-t-nm2) + (m - nm2 - t - mk2) + (k - nk2 - t - mk2)
answer2 = nm2 + mk2 + nk2
answer3 = a - (answer1 + nk2 + mk2 + nm2 + t)
print(answer1)
print(answer2)
print(answer3)


