#1
years_list = [2002, 2003, 2004, 2005, 2006, 2007]


#2
print("my third birthday was in ", years_list[2])


#3
print("I was the oldest in ", max(years_list))


#4
things = ['mozzarella', 'cinderella', 'salmonella']
print(things)


#5
print(things[1].capitalize())
print(things)

things[1] = things[1].capitalize()
print(things)


#6
things[0] = things[0].upper()
print(things)


#7
things.remove('salmonella')
print(things)


#8
surprise = ['Groucho', 'Chico', 'Harpo']
surprise[2] = surprise[2].lower()
print(surprise)


#9
print(surprise[2].capitalize()[::-1])


#10
even = [number for number in range(10) if number % 2 == 0]
print(even)


#11
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', "say we're done")
]
start2 = 'Someone better'

start1_caps = ' '.join([word.capitalize() + '!' for word in start1])
for first, second in rhymes:
    print(f'{start1_caps} {first.capitalize()}!')
    print(f'{start2} {second}.')

