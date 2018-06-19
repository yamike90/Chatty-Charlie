# py 3.6.5
# https://github.com/dialogflow/dialogflow-python-client
# https://github.com/python-telegram-bot
# pip install python-telegram-bot --upgrade     # Пакет для работы с телеграм ботами
# pip install python-telegram-bot[socks]        # Пакет для работы с прокси
# pip install apiai                             # Пакет для работы с API от Dialogflow

# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # Импорт из python-telegram-bot
import apiai, json # Импорт модулей для разбора json
TOKEN='Токен телеграм бота' # Токен @ChattyCharlieBot
REQUEST_KWARGS={
    'proxy_url': 'socks5://c3po.vivalaresistance.info:3306/', # Прокси получил с помощью @FCK_RKN_bot
    'urllib3_proxy_kwargs': {
        'username': 'swcbbabh',
        'password': 'aYEbh6q5gQ',
        }
}
updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS) # Ловит апдейты от телеграма и передает диспетчеру
dispatcher = updater.dispatcher # Диспетчер работает с хэндлерами, от которых апдейты пердаются для вызова кол беков
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Обработка /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет! Поболтаем?')
start_handler = CommandHandler('start', start) # Обработчик для /start
dispatcher.add_handler(start_handler) # добавить хендлер в диспетчер

# Обработка сообщения от пользователя    
def textMessage(bot, update):
    request = apiai.ApiAI('токен dialogflow').text_request() # Токен API к DialogFlow
    request.lang = 'ru' # Какой язык будет использоваться для общения
    request.session_id = 'ChattyCharlie' # ID сессии диалога
    request.query = update.message.text # Отправка пользовательского сообщения на DialogFlow
    responseJson = json.loads(request.getresponse().read().decode('utf-8')) # Получить ответ от сервера, декодировать, распарсить
    response = responseJson['result']['fulfillment']['speech'] # Парсинг JSON
    if response: # Если есть ответ от DialogFlow, оптравить юзеру, если нет, сообщение об ошибке
        bot.send_message(chat_id=update.message.chat_id, text = response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Не понял вас, к сожалению. Поболтаем на другую тему?')
#    response = 'Вы прислали: ' + update.message.text                           # Echo bot
#    bot.send_message(chat_id=update.message.chat_id, text=response)            # Echo bot
text_Message_handler = MessageHandler(Filters.text, textMessage) # Обработчик для сообщения пользователя
dispatcher.add_handler(text_Message_handler) # добавить хендлер в диспетчер

updater.start_polling(clean=True) # поиск апдейтов
updater.idle() # остановка по ctlr + c
