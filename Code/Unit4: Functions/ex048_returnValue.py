# n = q * m + r
def mod(n, m):
    q = n // m
    r = n %  m 
    return q, r 

q, r = mod(5, 3)
print(f'q = {q}, r = {r}')
