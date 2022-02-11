#1
def unicode_data(value):
    import unicodedata
    name = unicodedata.name(value)
    print(f'value = {value} name = {name}')

mystery = ('\U0001f4a9')
print(mystery)
unicode_data(mystery)

#2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

#3
pop_string = pop_bytes.decode()
print(pop_string)
print(pop_string == mystery)

#4
mammoth = """
We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.

We'rt thou suspended from baloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon.
"""

#5
import re

found_all_with_start_c = re.findall(r'\bc\w*', mammoth)
print(found_all_with_start_c)

#6
found_words_of_4_with_start_c = re.findall(r'\bc\w{3}\b', mammoth)
print(found_words_of_4_with_start_c)

#7
found_words_with_end_r = re.findall(r'\b[\w\']*r\b', mammoth)
print(found_words_with_end_r)

#8
found_3_consecutive_vowels = re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammoth)
print(found_3_consecutive_vowels)

#9
import binascii

row = '47494638396101000100800000000000ffffff21f9' + \
    '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(row)
print(gif)

#10

print(gif[:6] == b'GIF89a')

#11
import struct

width, height = struct.unpack('<HH', gif[6:10])
print(width, height)