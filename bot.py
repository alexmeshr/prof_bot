# -*- coding: utf-8 -*-
import config
import telebot
from utils import *

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_messages(message):
    parsing(message)


if __name__ == '__main__':
    bot.infinity_polling()
