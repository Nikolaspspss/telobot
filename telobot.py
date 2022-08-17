import telebot

TOKEN = '5362674577:AAERla3VxzYoyApN0Dvghl_X2bux9ZthEeU'

bot = telebot.TeleBot(TOKEN)


keys = {'биток': 'BTC',
        'эфириум': 'ETH',
        'доллар': 'USD',
        }

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
    <какую валюту перевести> \
    <количество переводимой валюты>'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n',join((text, key,))
    bot.reply_to(message, text)


bot.polling()