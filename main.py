import telebot
import config
#import sqlite3
#db = sqlite3.connect('db/database.db') as db:

from telebot import types

bot = telebot.TeleBot(config.TOKEN)




@bot.message_handler(commands=['start'])
def welcome(message):
  #  sti = open('static/sticker.webp', 'rb')
  #  bot.send_sticker(message.chat.id, sti)


# keyboard


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Я знаю что я хочу")
    item2 = types.KeyboardButton("Я не знаю что я хочу")

    markup.add(item1, item2)



    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, этот бот созданный чтобы помогать вам в готовке.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def x(message):
    if message.chat.type == 'private':
        if message.text == 'Я знаю что я хочу':
            bot.send_message(message.chat.id, 'база данных')



        elif message.text == 'Я не знаю что я хочу':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Супы", callback_data='1')
            bot.send_message(message.chat.id, 'вот что могу предложить ')
            item2 = types.InlineKeyboardButton("Горячие блюда", callback_data='2')
            item3 = types.InlineKeyboardButton("Салаты", callback_data='3')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'смотри', reply_markup=markup)


        else:
            bot.send_message(message.chat.id, 'Я не знаю что вам ответить 😢')




@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                bot.send_message(call.message.chat.id, '-')
            elif call.data == '2':
                markup = types.InlineKeyboardMarkup(row_width=3)

                item5 = types.InlineKeyboardButton("курица", callback_data='111')
                item6 = types.InlineKeyboardButton("говядина", callback_data='222')
                item7 = types.InlineKeyboardButton("свинина", callback_data='333')
                markup.add(item5, item6, item7)
                bot.send_message(call.message.chat.id, 'смотри', reply_markup=markup)

            elif call.data == '3':
                bot.send_message(call.message.chat.id, 'пока пусто')


            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как делак?",
                             #     reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="123")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)