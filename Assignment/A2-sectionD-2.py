import random

def generate_eight() -> list:
    lucky_numbers = [random.randint(10, 99) for _ in range(8)]
    return lucky_numbers

def main():
    studentID = input('Enter your student ID: ')
    digits = studentID[len(studentID) - 2:]
    
    while True:
        lucky_numbers = generate_eight()
        print('-' * 40)
        print(f'Last two digits in my student ID: {digits}')
        print(f'Lucky numbers are: {lucky_numbers}')

        if int(digits) in lucky_numbers: 
            print(f'Finally I am lucky with this number: {digits}\n')
            break
        if input('Not lucky. Try again?[y or n]: ').upper() == 'N': break

main()