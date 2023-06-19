'''import requests
from bs4 import BeautifulSoup as BS

main_url = "https://stopgame.ru/newsdata/"
link = 58316

for i in range(0, 20):

    r = requests.get(main_url + str(link))
    soup = BS(r.text, "lxml")

    title = soup.find("h1").get_text()
    date = soup.find("span", class_="_date_1c0t7_537 _date--full_1c0t7_1").get_text()
    description = ""

    for i in soup.findAll('p', class_="_text_1c0t7_89 _text-width_1c0t7_89"):
        description = description + str(i.get_text()) + "\n"

    link += 1

    print(title)'''

#with open ('https://stopgame.ru/') as file:
 #   src = file.read
#soup = BeautifulSoup(src, 'lxml')
#title = soup.head

#print(list_news)

def parcer():
    import requests
    from bs4 import BeautifulSoup as BS
    from .models import News

    r = requests.get('https://stopgame.ru/news')
    soup = BS(r.text, "lxml")


    list_news = soup.find(class_ = "list-view").find_all(class_ = "_title_1tbpr_49")

    for news in list_news:
        news = news.text
        #print(news)


    for date in soup.findAll(class_='_content__bottom_1tbpr_1'):
        date = date.find("span").get_text()
        #print(date)


    object = News()
    object.date = date
    object.title = news
    object.description = '---'
    object.save()
