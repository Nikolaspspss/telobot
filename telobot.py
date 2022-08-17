import telebot

TOKEN = '5362674577:AAERla3VxzYoyApN0Dvghl_X2bux9ZthEeU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')




bot.polling()