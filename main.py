import telebot
from telebot import types

bot = telebot.TeleBot('5366774335:AAGppdEQ_SxFTn1_SLUZGAefRq90vHBeXyM')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить саит", url="https://youtube.com"))
    bot.send_message(message.chat.id, "Отиличный выбор, просто нажми на кнопку",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['insta'])
def instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в инстаграм", url="https://www.instagram.com/_cool_cars_md_/"))
    bot.send_message(message.chat.id, "Самые шикарные авто тут",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('website')
    start = types.KeyboardButton('start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'press here', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "hello":
        bot.send_message(message.chat.id, "и тебе привет!",  parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('NatGeo17.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "video":
        video = open('sagun - I ll Keep You Safe (feat_ Shiloh)(720p).mp4', 'rb')
        bot.send_video(message.chat.id, video)
    else:
        bot.send_message(message.chat.id, "пащол нах", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'вау, крутое фото')


bot.polling(none_stop=True)
