def arithmetic_operation(oper):
    def add (x, y):
        return x + y
    def div (x, y):
        return x / y
    def mult (x, y):
        return x * y
    def sub (x, y):
        return x - y
    if oper == '+':
        return add
    if oper == '/':
        return div
    if oper == '-':
        return sub
    if oper == '*':
        return mult
add = arithmetic_operation('+')
div = arithmetic_operation('/')
sub = arithmetic_operation('-')
print(sub(20, 10))
print(div(20, 5))