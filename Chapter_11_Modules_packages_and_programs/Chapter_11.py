#1
import zoo


print(zoo.hours())


#2
import zoo as menagerie


print(menagerie.hours())


#3
from zoo import hours


print(hours())


#4
from zoo import hours as info


print(info())


#5
plain = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(plain)


#6
from collections import OrderedDict


fancy = OrderedDict(plain)

for keys in plain:
    print(keys)


#7
from collections import defaultdict


dict_of_lists = defaultdict(list)
dict_of_lists['a'] = 'something for a'

print(dict_of_lists['a'])