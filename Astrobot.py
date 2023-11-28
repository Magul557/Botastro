import telebot
from telebot import types

bot = telebot.TeleBot('6453652066:AAHdArxm23kdPJFDgCXz4hz-q_R4ita0HaI')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(" Наш астрономический сайт", url = http://astro.gulden.tv/#Intro)
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на наш астрономический сайт", reply_markup=markup)

bot.polling(none_stop = "True", interval = 0)


