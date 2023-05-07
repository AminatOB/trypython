#program that accepts time in 24hours format and then greet the user#

time = int(input('Enter your time:'))
if time >= 0 and time <= 12:
    print('Good morning')
elif time >= 13 and time <= 16:
    print('Good afternoon')
elif time >= 17 and time <= 20:
    print('Good evening')
elif time >= 21 and time <= 24:
    print('Good night')
else:
    print('wrong input')




#2#
time = int(input('Enter your time:'))

while time > 0:
    if time >= 0 and time <= 12:
        print('Good morning')
        break
    elif time >= 13 and time <= 16:
        print('Good afternoon')
        break
    elif time >= 17 and time <= 20:
        print('Good evening')
        break
    elif time >= 21 and time <= 24:
        print('Good night')
        break
    else:
        time = int(input('Enter your time:'))

