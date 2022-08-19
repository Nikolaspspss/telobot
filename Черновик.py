import telebot
help(telebot)
@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Привет раб системы, жми /start, чтобы начать')

    if len(values) != 3:
            raise ConvertionException('Эээээ, слыш, нормально введи.')
        quote, base, amount = message.text.split('')
