import random

numbers = [1, 2, 3, 4, 5, 6, 7]
# randint(2, 100)
print('randint(2, 100) = ', random.randint(2, 100))
# random()
print('random() = ', random.random())
# shuffle numbers
print('numbers = ', numbers)
random.shuffle(numbers)
print('numbers (after shuffle) = ', numbers)
# choice numbers
print('choice(numbers) = ', random.choice(numbers))