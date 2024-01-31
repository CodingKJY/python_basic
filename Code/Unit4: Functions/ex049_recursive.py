def sum(n):
    if n == 1: 
        print(f'sum({n}) = {n}')
        return n 
    print(f'{n} + sum({n-1})')
    return n + sum(n - 1)

print('sum(5) = ', sum(5))
