from decimal import *
num = Decimal(input())
if len(num.as_tuple().digits) == abs(num.as_tuple().exponent):
    print(max(num.as_tuple().digits))
else:
    print(max(num.as_tuple().digits) + min(num.as_tuple().digits))