from django.shortcuts import render
from .models import News
import requests
from bs4 import BeautifulSoup as BS
#import json

main_url = "https://stopgame.ru/news"

r = requests.get(main_url)
soup = BS(r.text, "lxml")
news_list = soup.findAll("div", class_="_card_1tbpr_1")

for news in news_list:
    html = news.find("a", class_="_title_1tbpr_49")
    title = html.get_text()
    url = "".join(html.get("href"))
    identificator = url[10:15]
    date = news.find("div", class_="_info-row_1tbpr_105").find("span").get_text()

    print(f"{title} \n {identificator} \n {date}")


    obj = News()
    obj.title = title
    obj.date = date
    obj.description = "Null"
    obj.identificator = identificator
    obj.save()

def my_view(request):
    value1 = 42
    value2 = "Пример текста"
    return render(request, 'C:/python scripts/projects/NewsPaper1/templates/flatpages/table.html', {'value1': value1, 'value2': value2})