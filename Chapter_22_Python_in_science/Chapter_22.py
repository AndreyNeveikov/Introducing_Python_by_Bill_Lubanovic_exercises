import pandas as pd


data_frame = pd.read_csv('titles.csv', delimiter=',')
print(data_frame)  # output with function 'print'

n = 2
print(data_frame.head(n))  # n строк с начала
print(data_frame.tail(n))  # n строк с конца
print(data_frame.sample(n))  # случайная строка (цифра в скобках показывает сколько строк)

print(data_frame[['title', 'year']])
print(data_frame[data_frame.year >= 2000])

print(data_frame[['title', 'author']].head(n)) # функции выполняются по-очереди, сначала поиск столбцов 'title', 'author', потом вывод n элементов сверху
