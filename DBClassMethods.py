from peewee import *

db = SqliteDatabase("bot_db.db")


# Основной класс
class User():
    id = IntegerField(primary_key=True)
    chat_id = IntegerField()
    state = TextField()

    class Meta():
        database = db


# Функции основного класса
def create_new_user(message):
    user = User(chat_id=message.chat.id)
    user.save()

# states Состояния
NONE = 'none'
WAIT_TAG = 'wait_tag'
TAGGET = 'tagget'

def change_state(state):
    # Функция записывает в бд состояние
    pass


# Тэги тут

class Tag():
    id = IntegerField(primary_key=True)
    tag = TextField()

    class Meta():
        database = db

