import config
import telebot
from views import register
from views import get_points
from telebot import types

entered = False
gaming = False
answered = True
user = 0
iteration = 0
bot = telebot.TeleBot(config.token)


def parsing(message):
    global entered
    global answered
    global gaming
    global user
    global iteration

    if not gaming:

        if message.text == "/signup" and not entered:
            user = register(message.chat.id, message.date)  # message.from_user.username
            entered = True
            bot.send_message(message.chat.id, "Вы залогинены!")
            # что-то там с юзернеймом

        elif message.text == "/game" and entered:
            gaming = True
            answered = True
            iteration = 0

        elif message.text == "/exit" and entered:
            user.save()
            entered = False
            gaming = False
            bot.send_message(message.chat.id,
                             str(user.username) + ", Вы завершили игру c " + str(user.score) + " очками!")

    if gaming and iteration < 4:

        points = get_points()
        if answered:
            bot.send_message(message.chat.id, points[iteration].question,
                             reply_markup=generate_markup(points, iteration))
            answered = False
        else:
            if message.text == points[iteration].r_answ:
                bot.send_message(message.chat.id,
                                 "Правильно!" + " Вы получаете " + str(points[iteration].score) + " очков",
                                 reply_markup=next_markup())
                user.score += points[iteration].score
            else:
                bot.send_message(message.chat.id, "Неравильно:(", reply_markup=next_markup())
            answered = True
            iteration += 1
    elif gaming and iteration > 3:
        user.save()
        entered = False
        gaming = False
        bot.send_message(message.chat.id,
                         message.from_user.username + ", Вы завершили игру c " + str(user.score) + " очками!")


def generate_markup(answers, i):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    list_items = []
    for item in answers[i].wr_answ.split(','):
        list_items.append(item)
        print(item)
    list_items.append(answers[i].r_answ)
    for item in list_items:
        markup.add(item)
    return markup


def next_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add("Далее >>")
    return markup
