ip_arr = input().split('.')
print(all(map(lambda x:True if x.isdigit() and int(x)>=0 and int(x)<=255 else False , ip_arr)))
#print(list(filter(lambda x:True if isinstance(x,int) and x >=0 and x <= 255 else False , ip_arr)))