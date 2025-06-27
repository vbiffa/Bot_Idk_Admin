import telebot 
from config import token
from random import randint

import logic as l
from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in l.Pokemon.pokemons.keys():
        pokemon = l.Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
       # bot.send_message(message.chat.id, pokemon.vers_name())
    else:
        #bot.reply_to(message, "Ты уже создал себе покемона")
        pokemon = l.Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
       # bot.send_message(message.chat.id, pokemon.vers_name())
# @bot.message_handler(commands=['attack'])
# def attack(message):
#     if not message.reply_to_message:
#         bot.reply_to(message, 'используй команду на сообщение противника.')
#         return 
#     attacker_username = message.from_user.username  # Получаем имя атакующего пользователя
#     enemy_username = message.reply_to_message.from_user.username  # Получаем имя атакуемого пользователя
#     result = attacker_username.attack(enemy_username)
#     bot.send_message(message.chat_id, result)
@bot.message_handler(commands=['attack'])
def attack(message):
    if not message.reply_to_message:  # Проверяем, является ли сообщение ответом на другое сообщение
        bot.reply_to(message, "Используйте команду /attack в ответ на сообщение противника.")
        return
    attacker_username = message.from_user.username  
    enemy_username = message.reply_to_message.from_user.username  
    if attacker_username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Сначала создайте покемона с помощью /go")
        return
    if enemy_username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Противник не создал покемона.")
        return
    attacker = Pokemon.pokemons[attacker_username]  # Получаем объект атакующего покемона
    enemy = Pokemon.pokemons[enemy_username]  # Получаем объект атакуемого покемона
    result = attacker.attack(enemy)
    bot.send_message(message.chat.id, result)
    if enemy.hp == 0:
        del Pokemon.pokemons[enemy_username]
        bot.send_message(message.chat.id, f"@{enemy_username} выбывает из игры!")

bot.infinity_polling(none_stop=True)

