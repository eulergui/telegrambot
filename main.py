import time
import random
import datetime
import telepot
import requests
import dotenv
import os
from telepot.loop import MessageLoop


dotenv.load_dotenv(dotenv.find_dotenv())

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #logmessage = "Got command: {1} from {2}".format(str(command), str(chat_id))
    #print (logmessage)

    if command == '/rolar':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
    elif command == '/dolar':
        cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        cotacoes = cotacoes.json()
        cotacao_dolar = cotacoes['USDBRL']["bid"]
        bot.sendMessage(chat_id, cotacao_dolar)
    elif command == '/euro':
        cotacoes = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
        cotacoes = cotacoes.json()
        cotacao_euro = cotacoes['EURBRL']["bid"]
        bot.sendMessage(chat_id, cotacao_euro)
    elif command == '/bitcoin':
        cotacoes = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
        cotacoes = cotacoes.json()
        cotacao_bitcoin = cotacoes['BTCBRL']["bid"]
        bot.sendMessage(chat_id, cotacao_bitcoin)
    elif command == '/clima' :
        umitemp = requests.get(f"https://api.thingspeak.com/channels/{os.getenv('TSChannel')}/feeds.json?results=1&timezone=America/Sao_Paulo")
        umitemp = umitemp.json()
        for i in umitemp['feeds']:
            climadata = "Ultima leitura em: {0}\nTemperatura: {1}\nUmidade: {2}%".format(str(i['created_at']), str(i['field1']), str(i['field2'].strip()))
            bot.sendMessage(chat_id, climadata)


bot = telepot.Bot(os.getenv('telegram_key'))

MessageLoop(bot, handle).run_as_thread()
#print ('I am listening ...')

while 1:
    time.sleep(10)
