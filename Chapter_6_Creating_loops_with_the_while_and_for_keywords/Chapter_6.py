#1
list = [3, 2, 1, 0]
for element in list:
    print(element)


#2
guess_me = 7
number = 1

while number:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it')
        break
    elif number > guess_me:
        print('oops')
        break
    number += 1


#3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
