from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import urllib3 # импортируем библиотеку urllib3
def parse():
    urllib3.disable_warnings() # отключаем варнинги чтобы пустило на сайт
    url = 'https://www.omgtu.ru/news/?SHOWALL_1=1' # ссылка
    page = requests.get(url,verify=False) # запрос html
    print(page.status_code) # ответ от страницы
    soup = BeautifulSoup(page.text, "html.parser") # передаем данные в bs4
    block = soup.findAll('div', class_='news__list') # ищем нужный блок
    description = ''
    for data in block: # бегаем по блоку
        if data.find('h3'): # находим нужный тег
            description = data.text # записываем с него текст
    textfile=open('textfile.txt',"w+",encoding="utf-8") # создаем txt файл в который запишем данные заголовков
    textfile.write(description) # записываем
    textfile.close() # закрываем файл
    print("Файл создан") # проверка
    # файл сохраняется в каталоге проекта