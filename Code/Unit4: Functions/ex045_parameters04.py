def func(*paras):
    sum = 0
    for para in paras:
        print(f'para = {para}')
        sum += para
    return  sum 

print(func(1))
print(func(1, 2, 3))
print(func(1, 2, 3, 4))
