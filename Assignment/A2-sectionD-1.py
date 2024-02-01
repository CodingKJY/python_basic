# n = 1, level = 1
# *
# n = 3, level = 2
# - *
# * * *
# n = 5, level = 3
# - - *
# - * * *
# * * * * *

# n = 2 * level - 1
n = eval(input('Enter an integer: '))
print(f'\nThe input integer is {n}.')
if n % 2 == 0: n -= 1
level = n // 2 + 1
print(f'There are/is {level} level(s).')
print(f'There are {n} star(s) at the bottom level.\n')

for i in range(level):
    space = '  ' * (level - i - 1)
    stars = '* ' * (2 * i + 1)
    print(space + stars + '\n')