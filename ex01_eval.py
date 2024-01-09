# input a number
a = input('Input number1: ')
b = input('Input number2: ')
# since the 'input()' function returns string type
# we use 'eval()' to transfer string to numerical type
a = eval(a)
b = eval(b)
# calculate addition value
c = a + b 
# output the result
print('a = ', a)
print('b = ', b)
print('a + b = ', c)
