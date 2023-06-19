'''from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

r = requests.get('https://stopgame.ru/')

with open ('https://stopgame.ru/') as file:
    src = file.read

soup = BeautifulSoup(src, 'lxml')
title = soup.head

print(title.text)

# Create your views here.
#def my_view(request):
 #   text = 'aaaaaaaaaaaaaaaaaaaa'

  #  value1 = text[0: 19] + '...'
   # value2 = "Пример текста"
    #value3 = 'Дата'
    #return render(request, 'C:/Users/User/PycharmProjects/Django_projects/NewsPapper/templates/flatpages/default.html',
     #           {'value1': value1, 'value2': value2, 'value3' : value3})
'''

import requests
from bs4 import BeautifulSoup as BS
from .models import News
#from parser import parcer

r = requests.get('https://stopgame.ru/news')
soup = BS(r.text, "lxml")

list_news = soup.find(class_="list-view").find_all(class_="_title_1tbpr_49")

for news in list_news:
    news = news.text
    print(news)

for date in soup.findAll(class_='_content__bottom_1tbpr_1'):
    date = date.find("span").get_text()
    print(date)

    object = News()
    object.date = date
    object.title = news
    object.description = '---'
    object.save()
