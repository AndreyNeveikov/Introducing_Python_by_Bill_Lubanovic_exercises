#1
import os

print(os.listdir('.'))


#2
print(os.listdir('..'))


#3
test1 = "This is the emergency text system"

with open('test.txt', 'wt') as test_file:
    test_file.write(test1)


# 4
with open('test.txt', 'rt') as test_file:
    test2 = test_file.read()

print(test1 == test2)