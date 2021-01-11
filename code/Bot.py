import telebot
import Text
import datetime #добавил чтобы в консоли выводилось время сообщения пользователя
from telebot import types
from telebot.types import InputMediaPhoto
from enum import Enum
bot = telebot.TeleBot('1008655818:AAERu26TQlQpE5Lx0OrwNj16Do-aEcPegGw') # не трогать


class User:
    def __init__(self, sost, right):
        self.sost = sost
        self.right = right

dictUser = {}
zagad = ['Загадка 1', 'Загадка 2', 'Загадка 3', 'Загадка 4', 'Загадка 5', 'Загадка 6', 'Загадка 7', 'Загадка 8', 'Финал']

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add('Загадка 1', 'Загадка 2', 'Загадка 3', 'Загадка 4', 'Загадка 5', 'Загадка 6', 'Загадка 7', 'Загадка 8', 'Финал')

podskazka1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
podskazka1.add('Подсказка 1', 'Подсказка 2', 'Главное меню')

@bot.message_handler(commands=['start'])   #декорация над методом. в документации очень понятно описано использование и возможные команды
def welcome(message):
    audio = open(r'Вступление.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()

    if message.chat.id not in dictUser:
        dictUser[message.chat.id] = User('start_sost', [])
    print(dictUser)
    #клавиатура
    markup =  types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("За дело! Игра началась!")
    markup.add(button1)

    msg = bot.send_message(message.chat.id, Text.welcome, reply_markup=markup)

    hour, minute = datetime.datetime.now().hour, datetime.datetime.now().minute    #тут просто создаю объекты часы и минуты
    print(str(hour) + ':' + str(minute), message.from_user.first_name, message.from_user.last_name, #это желательно вставлять в конец каждого метода, чтобы видеть то, что видит пользователь
          ': "' + message.text + '"')        #и в случае чего исправлять ошибки
    bot.register_next_step_handler(msg, first_step) #обработка следующего шага

def first_step(message): #следующий щаг
    msg = bot.reply_to(message, "Выберите загадку", reply_markup=markup)



# зона испытаний
@bot.message_handler(content_types=['text'])
def func(message):
    try:
        if dictUser[message.chat.id].sost == 'start_sost':
            if message.text in zagad:
                if message.text == zagad[0] and 1 not in dictUser[message.chat.id].right:
                    bot.send_message(message.chat.id, Text.komnata1)
                    bot.send_message(message.chat.id, 'Загадка: утилз', reply_markup=podskazka1)
                    dictUser[message.chat.id].sost = 'z1_sost'
                elif message.text == zagad[0]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')

                if message.text == zagad[1] and 2 not in dictUser[message.chat.id].right:
                    bot.send_message(message.chat.id, Text.komnata2)
                    bot.send_message(message.chat.id, '\n Загадка: ecnfd ybne vbcbc' \
           '\n 34.8.11. ' \
           '\n 43.32.42. ' \
           '\n 2.13.13. ' \
           '\n 16.7.9. ', reply_markup=podskazka1)
                    dictUser[message.chat.id].sost = 'z2_sost'
                elif message.text == zagad[1]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')

                if message.text == zagad[2] and 3 not in dictUser[message.chat.id].right:
                    bot.send_message(message.chat.id, Text.komnata3)
                    bot.send_photo(message.chat.id, 'https://sun9-6.userapi.com/impf/RFrRdTiN7fyVzoveoxseI-PnshUA0mthqOV_QQ/Ss1pqUCtuHc.jpg?size=779x816&quality=96&proxy=1&sign=1034e04e7fe14c52c8e41bf85137be27&type=album', 'Загадка: Восстановите порядок. ' \
           '\n Даны предложения (1-11) и их дословные переводы (w-a) на русский язык. Переводы даны в перепутанном порядке. ' \
           '\n Если вы расставите переводы в правильном порядке, то в середине комбинации английских букв (w-a) вы найдете правильное слово.', reply_markup=podskazka1)
                    dictUser[message.chat.id].sost = 'z3_sost'
                elif message.text == zagad[2]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')

                if message.text == zagad[3] and 4 not in dictUser[message.chat.id].right:
                    bot.send_message(message.chat.id, Text.komnata4)
                    bot.send_photo(message.chat.id, 'https://sun9-40.userapi.com/impg/VhzbZrmFaH9lcHjrmTsFZ-J9gap6pW6UQU8WDA/wNQvpQxlObM.jpg?size=1213x206&quality=96&proxy=1&sign=ba1176930113750beff32a836c832413&type=album', 'Загадка: о чем идет речь?', reply_markup=podskazka1)
                    dictUser[message.chat.id].sost = 'z4_sost'
                elif message.text == zagad[3]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')


                if message.text == zagad[4] and 5 not in dictUser[message.chat.id].right:
                    bot.send_message(message.chat.id, Text.komnata5,  reply_markup=podskazka1)
                    bot.send_media_group(message.chat.id,
                                         [InputMediaPhoto('https://sun1-22.userapi.com/impg/ZKCFiqOA_3zzrwHBrjQAHHwLXK0H6cBuBDRVlg/P9BjMpL3IGE.jpg?size=898x598&quality=96&proxy=1&sign=d3bdfebaf81aea1d0cd2ee580efd97d1&type=album'),
                                          InputMediaPhoto('https://sun9-37.userapi.com/impg/UOVgcHxbKBIClq_Ypjw9t72Q_6xCFp57GCxgIA/10w3MZRHDfY.jpg?size=1024x610&quality=96&proxy=1&sign=0699e7ca8c2857dde0a45734a8af5e5b&type=album'),
                                          InputMediaPhoto('https://sun9-28.userapi.com/impg/UJsQm8qrQ3GCP1HYNEDDOCzic8dMCoXlrVRAPw/40h-sZWFjdg.jpg?size=640x426&quality=96&proxy=1&sign=067f34752c10df0fbbf468467a553932&type=album'),
                                          InputMediaPhoto('https://sun1-97.userapi.com/impg/oMYwI0xBgVMnMAMML7Oq5f2D0lgBgJVKdqHn-w/Y4BFgGEvGGM.jpg?size=899x511&quality=96&proxy=1&sign=cf6b6814221e606c1c1ad26b337c734c&type=album'),
                                          InputMediaPhoto('https://sun9-28.userapi.com/impg/UJsQm8qrQ3GCP1HYNEDDOCzic8dMCoXlrVRAPw/40h-sZWFjdg.jpg?size=640x426&quality=96&proxy=1&sign=067f34752c10df0fbbf468467a553932&type=album'),
                                          InputMediaPhoto('https://sun9-48.userapi.com/impg/EHVFjYAHnDqRbNT5TUnIQDZkvwjwJDB4mZ9IJA/f8xG1gScybY.jpg?size=604x360&quality=96&proxy=1&sign=6bf9bf8ea271c4911be77b47f681fef0&type=album'),
                                          InputMediaPhoto('https://sun9-44.userapi.com/impg/A0mwGsCT4Qqpjrjyd40xZFsOkDDm1fSqrjZtvQ/T4Li__d8pMg.jpg?size=913x609&quality=96&proxy=1&sign=b83d92ec8f0270c2ae237c30f2122978&type=album')]
                                         )

                    dictUser[message.chat.id].sost = 'z5_sost'
                elif message.text == zagad[4]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')


                if message.text == zagad[5] and 6 not in dictUser[message.chat.id].right:
                    bot.send_message(message.chat.id, Text.komnata6)
                    bot.send_photo(message.chat.id, 'https://sun9-7.userapi.com/impg/jqLX3rq4eQYvVJ7JaJnS6jOvwHHvlaVgH3xzgQ/ZBZ4nAaoTH0.jpg?size=995x837&quality=96&proxy=1&sign=7dffea5c037d58d1803e48e704814d5e&type=album', 'Но судя по всему он мне оставил послание...', reply_markup=podskazka1)
                    dictUser[message.chat.id].sost = 'z6_sost'
                elif message.text == zagad[5]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')


                if message.text == zagad[6] and 7 not in dictUser[message.chat.id].right:
                    bot.send_message(message.chat.id, Text.komnata7)
                    bot.send_message(message.chat.id, 'Загадка: определи место по звукам \n[Нажмите сюда](https://clck.ru/SknJp)', reply_markup=podskazka1, parse_mode='MarkdownV2', disable_web_page_preview=True)
                    dictUser[message.chat.id].sost = 'z7_sost'
                elif message.text == zagad[6]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')


                if message.text == zagad[7] and 8 not in dictUser[message.chat.id].right:
                    bot.send_message(message.chat.id, Text.komnata8)
                    bot.send_photo(message.chat.id, 'https://sun9-12.userapi.com/impg/JkbHCqy1ov39AWjhBvpdc67FCQM38AF8SPLTmQ/qquwSGfSbcg.jpg?size=1043x304&quality=96&proxy=1&sign=b3851158c783297e5f07d2057748fb63&type=album', 'Загадка: Что за слово пришло мне на ум?', reply_markup=podskazka1)
                    dictUser[message.chat.id].sost = 'z8_sost'
                elif message.text == zagad[7]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')


                if message.text == zagad[8] and 'final' not in dictUser[message.chat.id].right and len(dictUser[message.chat.id].right) == 8:
                    bot.send_photo(message.chat.id, 'https://sun9-34.userapi.com/impg/KchNupPBdtgctN4-U4GjSAV6uHBaGMfpWCsrcg/ItEKyYKjVOQ.jpg?size=640x360&quality=96&proxy=1&sign=b4255f02b4258f63f0bfaa3db6de0b92&type=album', Text.final, reply_markup=podskazka1)
                    dictUser[message.chat.id].sost = 'final_sost'
                elif message.text == zagad[8] and len(dictUser[message.chat.id].right) != 8:
                    bot.send_message(message.chat.id, 'Чтобы открыть финал, сначала решите все остальные загадки.')
                elif message.text == zagad[8]:
                    bot.send_message(message.chat.id, 'Эта загадка уже решена.')
            else:
                bot.send_message(message.chat.id, "Неверный ввод. Выберите загадку")





        elif dictUser[message.chat.id].sost == 'z1_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'поезд':
                dictUser[message.chat.id].right.append(1)
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Верно!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "Цезарь - это не только салат, но и полководец, которому нужно было передавать секретные сообщения!")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "Воспользуйтесь шифром Цезаря, 4 шага назад.")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)

        elif dictUser[message.chat.id].sost == 'z2_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'гнев':
                dictUser[message.chat.id].right.append(2)
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Верно!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "Рихорд Зорге - разведчик. Какое оборудование используют разведчики?")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "Под буквами зашифровано название текста. Какие же части текста могут быть зашифрованы под цифрами?")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)

        elif dictUser[message.chat.id].sost == 'z3_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'деньги':
                dictUser[message.chat.id].right.append(3)
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Верно!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "Попробуйте перевести предложения из левого столбика")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "Какое английское слово из 5 букв получилось у вас после того,как вы расставили переводы в правильном порядке? Переведите его нарусский язык. Это и есть улика")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)

        elif dictUser[message.chat.id].sost == 'z4_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'дождь':
                dictUser[message.chat.id].right.append(4)
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Верно!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "Слово-улика соберется из первых букв слов, изображенных на картинках.")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "Железо - Ж.")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)

        elif dictUser[message.chat.id].sost == 'z5_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'начало':
                dictUser[message.chat.id].right.append(5)
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Верно!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "Поищите картинки в интернете при помощи функции “поиск по картинке” или по ключевым словам")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "Цифра на картинке обозначает букву по порядку в спрятанномслове.")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)

        elif dictUser[message.chat.id].sost == 'z6_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'стакан':
                dictUser[message.chat.id].right.append(6)
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Верно!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "Стоит внимательно прочитать текст")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "Стоит проверить правописание текста =)")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)

        elif dictUser[message.chat.id].sost == 'z7_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'пустыня':
                dictUser[message.chat.id].right.append(7)
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Верно!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "А что это за место, где дует ветер?")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "А что это за место, где дует ветер, и слышно каждую песчинку?")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)

        elif dictUser[message.chat.id].sost == 'z8_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'трение':
                dictUser[message.chat.id].right.append(8)
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Верно!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "«закрыть глаза»... что бы это значило?")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "Какая категория людей использует данный шрифт?")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)

        elif dictUser[message.chat.id].sost == 'final_sost':
            if message.text == 'Главное меню':
                dictUser[message.chat.id].sost = 'start_sost'
                bot.send_message(message.chat.id, 'Выберите загадку', reply_markup=markup)
            elif message.text.lower() == 'флакон':
                dictUser[message.chat.id].right.append('final')
                print(dictUser[message.chat.id].right) #!!!!!!!!!!!!!!!!!!!!!!
                bot.send_message(message.chat.id, "Молодцы! Вы отлично справились с прохождением всех загадок. Поздравляем вас с окончанием игры!", reply_markup=markup)
                dictUser[message.chat.id].sost = 'start_sost'
            elif message.text == 'Подсказка 1':
                bot.send_message(message.chat.id, "Ассоциации слов из загадки и улик помогут тебе узнать, где же находится директор")
            elif message.text == 'Подсказка 2':
                bot.send_message(message.chat.id, "Цифры подскажут количество букв в нужной тебе ассоциации")
            else:
                bot.send_message(message.chat.id, "Неверно, попробуйте еще раз! Также вы можете взять подсказку",
                                 reply_markup=podskazka1)
    except KeyError:
        bot.send_message(message.chat.id, 'Похоже вы новый пользователь! Начните с /start')







bot.polling(none_stop=True)
