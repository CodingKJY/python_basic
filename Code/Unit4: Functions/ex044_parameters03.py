def func(x, y, z = 0):
    print(f'x = {x}\ny = {y}\nz = {z}')
    return x + y + z 

print(func(1, 2))
print(func(1, 2, 3))
print(func(1, y = 2))
print(func(y = 1, x = 2))
print(func(z = 1))
