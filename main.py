from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests


def parse():
    url = 'https://omgtu.ru/l/?SHOWALL_1=1'  # передаем необходимы URL адрес
    page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code)  # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4
    block = soup.find_all('h3', class_="news-card__title")  # находим контейнер с нужным классом
    with open('file_parser.txt', 'w', encoding="utf-8") as file:  # открываем файл file_parser.txt
        count = 0
        for item in block:  # проходим циклом по содержимому контейнера
            res = item.text.replace(' ' * 40, '')  # убираем пробелы в начале строки
            if count:
                file.write(res)
            else:
                file.write(res[1:])  # убирает первую пустую строку
                count += 1


if __name__ == '__main__':
    parse()
