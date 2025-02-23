def calc(a, b, ope):
    if ope is '+':
        return a+b
    elif ope is '-':
        return a-b
    elif ope is '*':
        return a*b
    elif ope is '/':
        return a/b

ask = 'n'
do_calc = True
while do_calc:
    if ask == 'n':
        x = float(input('What is the first number? '))
    operation = input('+ \n - \n * \n / \nchose an operation: ')
    y = float(input('enter the second number? '))
    print(f"{x} {operation} {y} = {calc(a=x, b=y, ope=operation)}")
    ask = input(f'type y for calculating with {calc(a=x, b=y, ope=operation)} or Type for exit or Type n for calculate with new no.: ').lower()
    if ask == 'y':
        x = calc(a=x, b=y, ope=operation)
    if ask == 'e':
        do_calc = False


                                             # method2👇

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
my_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
ask = 'n'
do_calc = True
while do_calc:
    if ask == 'n':
        x = float(input('What is the first number? '))
    print('chose an operation: ')
    for key in my_dict:
        print(key)
    operation = input()
    function = my_dict[operation]
    y = float(input('enter the second number? '))
    print(f"{x} {operation} {y} = {function(a=x,b=y)}")
    ask = input(f'type Y for calculating with {function(a=x,b=y)} or Type E for exit or Type N for calculate with new no.: ').lower()
    if ask == 'y':
        x = function(a=x, b=y)
    if ask == 'e':
        do_calc = False
