#program that accepts time in 24hours format and then greet the user#

time = int(input('Enter your time:'))
if time >= 0 & time <= 12:
    print('Good morning')
elif time >= 13 & time <= 16:
    print('Good afternoon')
elif time >= 17 & time <= 20:
    print('Good evening')
elif time >= 21 & time <= 24:
    print('Good night')
else:
    print('wrong input')

