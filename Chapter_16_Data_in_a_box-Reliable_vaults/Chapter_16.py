#1
import csv


author_book = [
    {'author': 'J R R Tolkien', 'book': 'The Hobbit'},
    {'author': 'Lynne Truss', 'book': '"Eats, Shoots & Leaves"'}
]

with open('books', 'wt') as fout:
    cout = csv.DictWriter(fout, ['author', 'book'])
    cout.writeheader()
    cout.writerows(author_book)


#2
with open('books', 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)


#3
titles =[
    {'title': 'The Weirdstone of Brisingamen', 'author': 'Alan Garner', 'year': '1960'},
    {'title': 'Perdido Street Station', 'author': 'China Mieville', 'year': '2000'},
    {'title': 'Thud!', 'author': 'Terry Pratchett', 'year': '2005'},
    {'title': 'The Spellmam', 'author': 'LisaLutz', 'year': '2007'},
    {'title': 'Small Gods', 'author': 'Terry Pratchett', 'year': '1992'},
]

with open('titles.csv', 'wt') as fout:
    cout = csv.DictWriter(fout, ['title', 'author', 'year'])
    cout.writeheader()
    cout.writerows(titles)


#4
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
(title VARCHAR(50) PRIMARY KEY,
author VARCHAR(50),
year INT)''')


#5
ins_str = 'INSERT INTO books VALUES(?, ?, ?)'
with open('titles.csv', 'rt') as infile:
    titles = csv.DictReader(infile)
    for title in titles:
        curs.execute(ins_str, (title['title'], title['author'], title['year']))

conn.commit()


#6
curs.execute('SELECT * FROM books ORDER BY title')
rows = curs.fetchall()
print(rows)


#7
curs.execute('SELECT * FROM books ORDER BY year')
rows_published = curs.fetchall()
print(rows_published)


#8
import sqlalchemy as sa

connect = sa.create_engine('sqlite:///books.db')
rows_sa = connect.execute('SELECT title FROM books ORDER BY title ASC')
for row in rows_sa:
    print(row)


#9
import redis
conn_redis = redis.Redis()
conn_redis.delete('test')

conn_redis.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
print(conn_redis.hgetall('test'))


#10
conn_redis.hincrby('test', 'count', 3)
print(conn_redis.hget('test', 'count'))


