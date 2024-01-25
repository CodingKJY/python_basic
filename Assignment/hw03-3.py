import random

upper_bound = 100
lower_bound = 1

target = random.randint(lower_bound, upper_bound)
guess  = -1
while True:
    guess = eval(input('Guess number: '))
    if guess > upper_bound or guess < lower_bound:
        print("Out of range, guess again")
    elif guess > target: 
        upper_bound = guess - 1
        print(f'Guess too high! range [{lower_bound}, {upper_bound}]')
    elif guess < target: 
        lower_bound = guess + 1
        print(f'Guess too small! range [{lower_bound}, {upper_bound}]')
    else: break

print('Sucessfully Guess! The target is ', guess)