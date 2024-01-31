def func(**kwargs):
    for key, value in kwargs.items():
        print(f'Key = {key}, Value = {value}')

func(x = 15, y = 10, z = 0)
