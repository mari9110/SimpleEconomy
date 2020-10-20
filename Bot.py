import telebot
import Text

bot = telebot.TeleBot('1008655818:AAERu26TQlQpE5Lx0OrwNj16Do-aEcPegGw')


@bot.message_handler(commands=['start'])
def welcome(message):
    audio = open(r'Вступление.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    bot.send_message(message.chat.id, Text.welcome)
    print(message.from_user.first_name, message.from_user.last_name, ': "' + message.text + '"')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, message.text + '?!')
    print(message.from_user.first_name, message.from_user.last_name, ': "' + message.text + '"')


@bot.message_handler(content_types=['photo'])
def func(message):
    bot.send_message(message.chat.id, "классный парень")


bot.polling(none_stop=True)
