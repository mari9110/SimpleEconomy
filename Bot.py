import telebot
import Text
import datetime #добавил чтобы в консоли выводилось время сообщения пользователя
from telebot import types

bot = telebot.TeleBot('1008655818:AAERu26TQlQpE5Lx0OrwNj16Do-aEcPegGw') # не трогать


@bot.message_handler(commands=['start'])   #декорация над методом. в документации очень понятно описано использование и возможные команды
def welcome(message):
    audio = open(r'Вступление.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    #клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("За дело! Игра началась!")
    markup.add(button1)

    msg = bot.send_message(message.chat.id, Text.welcome, reply_markup=markup)
    hour, minute = datetime.datetime.now().hour, datetime.datetime.now().minute    #тут просто создаю объекты часы и минуты
    print(str(hour) + ':' + str(minute), message.from_user.first_name, message.from_user.last_name, #это желательно вставлять в конец каждого метода, чтобы видеть то, что видит пользователь
          ': "' + message.text + '"')        #и в случае чего исправлять ошибки
    bot.register_next_step_handler(msg, first_step) #обработка следующего шага

def first_step(message): #следующий щаг
    markup = types.ReplyKeyboardMarkup()
    markup.add('Загадка 1', 'Загадка 2', 'Загадка 3', 'Загадка 4', 'Загадка 5', 'Загадка 6', 'Загадка 7', 'Загадка 8', 'Загадка 9')
    msg = bot.reply_to(message, "Выберите загадку", reply_markup=markup)


# зона испытаний
@bot.message_handler(content_types=['photo'])
def func(message):
    bot.send_message(message.chat.id, "классный парень")


bot.polling(none_stop=True)
