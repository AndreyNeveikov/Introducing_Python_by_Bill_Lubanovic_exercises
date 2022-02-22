"""Поиск видео в Internet Archive
по фрагменту названия и отображение его"""

import sys
import webbrowser
import requests


def search(title):
    """Возвращает список кортежей, состоящих из трех элементов
       (идентификатор, заголовок, описание), котороые описывают видеоролики,
       чьи заголовки частично соответствуют значению переменной title."""

    search_url = "http://archive.org/advancedsearch.php"
    params = {
        "q": f"Title: ({title}) AND mediatype: (movie)",
        "fl": "identifier,title,description",
        "output": "json",
        "rows": 10,
        "page": 1,
        }
    resp = requests.get(search_url, params=params)
    data = resp.json()
    docs = [(doc["identifier"], doc["title"], doc["description"])
            for doc in data["response"]["docs"]]
    return docs


def choose(docs):
    """Вывод номера строки, заголовка и частичного описания для
       каждого кортежа из списка :docs. Позволим пользователю выбрать
       номер строки. Если он корректен, вернем первый элемент выбранного
       кортежа ("идентификатор"). В противном случае вернем None."""

    last = len(docs) - 1
    for num, doc in enumerate(docs):
        print(f"{num}: ({doc[1]}) {doc[2][:30]}...")
    index = input(f"Which would you like to see (0 to {last})?")
    try:
        return docs[int(index)][0]
    except:
        return None


def display(identifier):
    """Отображение видео из архива в браузере с помощью идентификатора """
    details_url = f"http://archive.org/details/{identifier}"
    print("Loading", details_url)
    webbrowser.open(details_url)


def main(title):
    """Поиск всех фильмов, чье название соответствует значению переменной
    :title. Получение выбора пользователя и отображение его в браузере."""

    identifiers = search(title)
    if identifiers:
        identifier = choose(identifiers)
        if identifier:
            display(identifier)
        else:
            print("Nothing selected")
    else:
        print("Nothing found for", title)


if __name__ == "__main__":
    main(sys.argv[1])

