#1
secret = 7
guess = 9

if guess < 7:
    print('too low')
elif guess > 7:
    print('too high')
else:
    print('just right')


#2
small = False
green = False

if small:
    if green:
        print('polka dots')
    else:
        print('cherry')
else:
    if green:
        print('watermelon')
    else:
        print('pumpkin')
