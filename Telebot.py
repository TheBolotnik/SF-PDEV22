import json

import requests
import telebot
import lxml.html
from lxml import etree

TOKEN = '6036919491:AAFT4IcM18c4DJ1kpR-XkR6_z_UWP3cH-cM'
bot = telebot.TeleBot(TOKEN)

keys = {'доллар' : 'USD',
        'евро' : 'EUR',
        'рубль' : 'RUB'
        }

class Conv_Exp(Exception):
    pass

@bot.message_handler(commands = ['start', 'help'])
def handler_start(message):
    if message.chat.username == None:
        bot.reply_to(message, f'Привет, {message.chat.first_name}')
    else:
        bot.reply_to(message, f'Привет, {message.chat.username}')
    bot.send_message(message.chat.id, 'Чтобы начать работу бота введите команду в следующем формате: \n <начальная валюта>, '
'\n <валюта, в которую перевести>, \n<количество>\n Список доступных валют - /values')

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def converts(message: telebot.types.Message):
    txt = message.text.split(' ')

    if len(txt) != 3:
        bot.send_message(message.chat.id, 'Неверное количество параметров')
        raise Conv_Exp(f'Неверное количество параметров')

    try:
        base = keys[txt[0]]
        quote = keys[txt[1]]
        amount = float(txt[2])
        #print(f'{base} {quote} {amount}')
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

        if amount <= 0:
            raise ValueError

    except KeyError:
        bot.send_message(message.chat.id, 'Неверная валюта')
        raise Conv_Exp(f'Неверная валюта')
    except ValueError:
        bot.send_message(message.chat.id, 'Введено неверное число')
        raise Conv_Exp(f'Введено неверное число')
    if base == quote:
        bot.send_message(message.chat.id, 'Введены одинаковые валюты')
        raise Conv_Exp(f'Введены одинаковые валюты')


    if base != 'RUB':
        if quote != 'RUB':
            value1 = data['Valute'][base]['Value']
            value2 = data['Valute'][quote]['Value']

            result = (float(amount) * float(value1)) / float(value2)
        else:
            value1 = data['Valute'][base]['Value']
            result = float(amount) * float(value1)
    elif base == 'RUB':
        if quote != 'RUB':
            value2 = data['Valute'][quote]['Value']
            result = float(amount) / float(value2)
        else:
            result = int(amount)



    msg = f'Цена {amount} {txt[0]} ровняется {round(result, 2)} {txt[1]}'

    bot.send_message(message.chat.id, msg)

bot.infinity_polling()