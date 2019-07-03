import config
import telebot
from telebot import apihelper
from DBClassMethods import *

# прокси
apihelper.proxy = {'https': config.PROXY}

# тело будущего чата
bot = telebot.TeleBot(token=config.TOKEN)

# Наш код бдуго га
@bot.message_handler(commands=['start'])
def say_hello_to_user(message):
    # Приветсвенно сообщение, регистрация юзера
    bot.send_message(message.chat.id, "Привет я новый бот, а точнее эмуляция тегового чата, "
                                      "Все последующие сообщения будут метиться тэгами, просто вводи сообщение")
    create_new_user(message)
    print(type(message.chat.id))

@bot.message_handler(func=lambda message: message.text.startswith("#"))
def check_is_it_tagget(message):
    # В сообщении выбранный тег, благодаря которому изменяется соощение или же чеез STATE все реализовать
    print("It's TAG!")

@bot.message_handler(content_types=['text'])
def get_message_from_user(message):
    # тут мы принимаем сообщение и просим поставить теги
    print("It's message")


bot.polling(none_stop=True)