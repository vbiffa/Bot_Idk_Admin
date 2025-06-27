# import telebot
# from config import token
# from random import choice



#   # Импортируем библиотеку telebot для работы с Telegram API
# from telebot import types  # Импортируем модуль types для создания кнопок и клавиатур
# # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
# BOT_TOKEN = token # Токен вашего бота, полученный от BotFather
# # Создаем экземпляр бота
# bot = telebot.TeleBot(BOT_TOKEN)  # Создаем объект бота, используя токен
# # Функция для создания клавиатуры
# def create_keyboard():
#     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Создаем клавиатуру с двумя кнопками в ряду
#     help_button = types.KeyboardButton("Help")  # Создаем кнопку "Help"
#     keyboard.add(help_button)  # Добавляем кнопку "Help" на клавиатуру
#     return keyboard  # Возвращаем созданную клавиатуру
# import telebot
# from config import token



#   # Импортируем библиотеку telebot для работы с Telegram API
# from telebot import types  # Импортируем модуль types для создания кнопок и клавиатур

# # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
# BOT_TOKEN = token # Токен вашего бота, полученный от BotFather

# # Создаем экземпляр бота
# bot = telebot.TeleBot(BOT_TOKEN)  # Создаем объект бота, используя токен

# # Функция для создания клавиатуры
# def create_keyboard():
#     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Создаем клавиатуру с двумя кнопками в ряду
#     help_button = types.KeyboardButton("Help")  # Создаем кнопку "Help"
#     keyboard.add(help_button)  # Добавляем кнопку "Help" на клавиатуру
#     return keyboard  # Возвращаем созданную клавиатуру
# # Обработчик команды /start
# @bot.message_handler(commands=['start'])  # Декоратор указывает, что функция обрабатывает команду /start
# def send_welcome(message):
#     # Отправляем приветственное сообщение с клавиатурой
#     bot.reply_to(message, "Привет! Я простой бот. Напиши что-нибудь, и я повторю.", reply_markup=create_keyboard())
#     # Отправляем ответ пользователю с текстом и клавиатурой
# @bot.message_handler(commands=['coin'])
# def coin_handler(message):
#     coin = choice(["ОРЕЛ", "РЕШКА"])
#     bot.reply_to(message, coin)
# # Обработчик текстовых сообщений
# @bot.message_handler(func=lambda message: True)  # Декоратор указывает, что функция обрабатывает любые текстовые сообщения
# def handle_message(message):
#     if message.text == "Help":  # Если текст сообщения равен "Help"
#         # Если нажата кнопка Help
#         bot.reply_to(message, "Я могу повторять ваши сообщения. Просто напишите что-нибудь!")
#         # Отправляем справочное сообщение пользователю
#     else:
#         # Эхо-ответ на любые другие сообщения
#         bot.reply_to(message, f"Вы сказали: {message.text}")
#         # Повторяем текст, отправленный пользователем
# # Запуск бота
# if __name__ == '__main__':  # Проверяем, запущен ли скрипт как основная программа
#     print("Бот запущен...")  # Выводим сообщение в консоль о запуске бота
#     bot.polling()  # Запускаем бота в режиме ожидания новых сообщений



# import telebot # библиотека telebot
# from config import token # импорт токена

# bot = telebot.TeleBot(token) 

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Привет! Я бот для управления чатом.")

# @bot.message_handler(commands=['ban'])
# def ban_user(message):
#     if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
#         chat_id = message.chat.id # сохранение id чата
#          # сохранение id и статуса пользователя, отправившего сообщение
#         user_id = message.reply_to_message.from_user.id
#         user_status = bot.get_chat_member(chat_id, user_id).status 
#          # проверка пользователя
#         if user_status == 'administrator' or user_status == 'creator':
#             bot.reply_to(message, "Невозможно забанить администратора.")
#         else:
#             bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
#             bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
#     else:
#         bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")

# @bot.message_handler(func=lambda message: True)
# def ban_https(message):
#     chat_id = message.chat.id
#     user_id = message.reply_to_message.from_user.id
#     user_status = bot.get_chat_member(chat_id, user_id).status 
#     text = message.text
#     if 'https://' in text.lower() or 'http://' in text.lower():
#         try:
#             bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
#             bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен зы отправку ссылки.")
#         except:
#             pass
#     else: 
#         pass


            
# bot.infinity_polling(none_stop=True)
import telebot # библиотека telebot
from config import token # импорт токена

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом.")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
        chat_id = message.chat.id # сохранение id чата
         # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
         # проверка пользователя
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text

    # Проверяем, содержит ли сообщение http или https
    if 'http://' in text.lower() or 'https://' in text.lower():
        try:
            # Баним пользователя
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь @{message.from_user.username} был забанен за отправку ссылки.")
        except Exception as e:
            # Обработка ошибок
            bot.reply_to(message, f"Произошла ошибка: {e}")
    else:
        # Если нет ссылки, просто повторяем сообщение
        pass
@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
bot.infinity_polling(none_stop=True)
