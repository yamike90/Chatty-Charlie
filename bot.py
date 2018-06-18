#py 3.6.5
# pip install python-telegram-bot --updater     #пакет для работы с телеграм ботами
# pip install python-telegram-bot[socks]        #пакет для работы с прокси

# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN='594208169:AAGpydkJ5AhiprXaxxedDZkdsEGea_i0uoY' #токен @ChattyCharlieBot
REQUEST_KWARGS={
    'proxy_url': 'socks5://c3po.vivalaresistance.info:3306/', #прокси получил с помощью @FCK_RKN_bot
    'urllib3_proxy_kwargs': {
        'username': 'swcbbabh',
        'password': 'aYEbh6q5gQ',
        }
}
updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS) #ловит апдейты от телеграма и передает диспетчеру
dispatcher = updater.dispatcher #диспетчер работает с хэндлерами, от которых апдейты пердаются для вызова кол беков
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
