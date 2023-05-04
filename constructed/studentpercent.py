#program to accept student score percentage then print their grades#

score = int(input('Enter student score percentage:'))
if score >= 0 and score <= 35:
    print('F - Fail')
elif score >= 36 and score <= 40:
    print('E - Pass')
elif score >= 41 and score <= 49:
    print('D - Fair')
elif score >= 50 and score <= 59:
    print('C - Credit')
elif score >= 60 and score <= 69:
    print('B - Good ')
elif score >= 70 and score <= 100:
    print('A - Excellent')
else:
    print('Incorrect score/Wrong input')

