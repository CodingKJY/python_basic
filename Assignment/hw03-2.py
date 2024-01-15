number_of_student = eval(input('How many student\'s score need to be mark? '))

for i in range(number_of_student):
    score = eval(input('Input a score: '))

    if score > 100 or score < 0:
        print('Out of range')
    elif score >= 95:
        print('Grade A+')
    elif score >= 90:
        print('Grade A')
    elif score >= 85:
        print('Grade B+')
    elif score >= 80:
        print('Grade B')
    else:
        print('Grade C')