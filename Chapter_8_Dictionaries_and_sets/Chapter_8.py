#1
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

print(e2f)


#2
print(e2f.get('walrus'))


#3
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)


#4
print(f2e.get('chien'))


#5
print(e2f.keys())


#6
from pprint import pprint
life = {
    'animals': {'cats': ['Henry', 'Grumpy', 'Lucy'],
                'octopi': {},
                'emus': {}
               },
    'plants': {},
    'other': {}
}
pprint(life)


#7
print(life.keys())


#8
print(life['animals'].keys())


#9
print(life['animals']['cats'])


#10
squares = {}
for number in range(10):
    squares[number] = number * number
print(squares)


#11
odd = {number for number in range(10) if number % 2 == 0}

print(odd)


#12
for thing in (f'Got %s' % number for number in range(10)):
    print(thing)


#13
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass')

person_type = dict(zip(keys, values))
print(person_type)


#14
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted year shop', 'Check your exits']

movies = dict(zip(titles, plots))
print(movies)


