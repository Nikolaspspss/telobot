import telebot
help(telebot)
@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')
