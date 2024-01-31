def func(x, y, z):
    print(f'x = {x}\ny = {y}\nz = {z}')

a = [1, 2, 3]
b = {'y': 1, 'x': 2, 'z': 3}

func(*a)
print()
func(**b)
