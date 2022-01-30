#1
song = """When an eel grab your arm,
And it causes great harm,
That's - a moray!"""
print(song.replace(' m', ' M'))

#2
questions = [
    "We don't serve string around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]
print(f'\nQ: {questions[0]} \nA: {answers[1]}')
print(f'\nQ: {questions[1]} \nA: {answers[2]}')
print(f'\nQ: {questions[2]} \nA: {answers[0]}')


#3
print("""
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s,
And now thinks he's a %s.
""" % ('roast beef', 'ham', 'head', 'clam'))


#4
letter = ("""
Dear {salutation} {name}

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}
""")


#5
print(letter.format(
    salutation='Professor',
    name='Bill',
    product='TV',
    verbed='exploded',
    room='bathroom',
    animals='seals',
    amount='5.99$',
    percent='50',
    spokesman='Tom Smith',
    job_title='Executive Director'
))


#6
objects = ['duck', 'pumpkin', 'spitz']
for object in objects:
    print("%sy Mc%sface" % (object.title(), object.title()))
print('')


#7
for object in objects:
    print("{}y Mc{}face".format(object.title(), object.title()))
print('')


#8
for object in objects:
    print(f"{object.title()}y Mc{object.title()}face")
