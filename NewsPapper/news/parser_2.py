import requests
from bs4 import BeautifulSoup as BS
from NewsPapper.news.models import News

r = requests.get('https://stopgame.ru/news')
soup = BS(r.text, "lxml")

list_news = soup.find(class_="list-view").find_all(class_="_title_1tbpr_49")

for idx, news in enumerate(list_news):
    if idx >= 20:
        break
    news_title = news.text
    news_date = news.find(class_='_date_1hiz0_2').get_text()

    print(news_title)
    print(news_date)

    obj = News()
    obj.date = news_date
    obj.title = news_title
    obj.description = '---'
    obj.save()