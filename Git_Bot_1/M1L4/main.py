import telebot 
from config import token
from random import randint

import logic as l
from logic import Pokemon
from logic import Wizard
from logic import Figter
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
       # bot.send_message(message.chat.id, pokemon.vers_name())
    else:
        #bot.reply_to(message, "Ты уже создал себе покемона")
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
       # bot.send_message(message.chat.id, pokemon.vers_name())

@bot.message_handler(command=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.info())
    else: 
        bot.send_message(message.chat.id, 'Вы не создали себе покемона')

@bot.message_handler(commands=['feed'])
def feed(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Сначала создайте покемона с помощью /go")
        return
    user = Pokemon.pokemons[username]
    if user.type_pok == 'Figter' :
        user = Figter.pokemons[username]
    result = user.feed()
    bot.send_message(message.chat.id, result)
# Battle Functions  |
#                   |
#                  \ /


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
    if attacker_username == enemy_username:
        bot.reply_to(message, "Вы не можете атаковать самого себя")
        return
    attacker = Pokemon.pokemons[attacker_username]  # Получаем объект атакующего покемона
    enemy = Pokemon.pokemons[enemy_username]  # Получаем объект атакуемого покемона
    result = attacker.attack(enemy)
    bot.send_message(message.chat.id, result)
    if enemy.hp == 0:
        del Pokemon.pokemons[enemy_username]
        bot.send_message(message.chat.id, f"@{enemy_username} выбывает из игры!")
@bot.message_handler(commands=['special_attack1'])
def special_attack1(message):
    if not message.reply_to_message:  # Проверяем, является ли сообщение ответом на другое сообщение
        bot.reply_to(message, "Используйте команду /special_attack1 в ответ на сообщение противника.")
        return
    attacker_username = message.from_user.username  
    enemy_username = message.reply_to_message.from_user.username  
    if attacker_username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Сначала создайте покемона с помощью /go")
        return
    if enemy_username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Противник не создал покемона.")
        return
    if attacker_username == enemy_username:
        bot.reply_to(message, "Вы не можете атаковать самого себя")
        return
    attacker = Pokemon.pokemons[attacker_username]  # Получаем объект атакующего покемона
    if attacker.type_pok == 'Wizard':
        attacker = Wizard.pokemons[attacker_username]
    else:
        attacker = Figter.pokemons[attacker_username]
    enemy = Pokemon.pokemons[enemy_username]  # Получаем объект атакуемого покемона
    result = attacker.s_a1(enemy)
    bot.send_message(message.chat.id, result)
    if enemy.hp == 0:
        del Pokemon.pokemons[enemy_username]
        bot.send_message(message.chat.id, f"@{enemy_username} выбывает из игры!")
@bot.message_handler(commands=['special_attack2'])
def special_attack2(message):
    if not message.reply_to_message:  # Проверяем, является ли сообщение ответом на другое сообщение
        bot.reply_to(message, "Используйте команду /special_attack2 в ответ на сообщение противника.")
        return
    attacker_username = message.from_user.username  
    enemy_username = message.reply_to_message.from_user.username  
    if attacker_username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Сначала создайте покемона с помощью /go")
        return
    if enemy_username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Противник не создал покемона.")
        return
    if attacker_username == enemy_username:
        bot.reply_to(message, "Вы не можете атаковать самого себя")
        return
    attacker = Pokemon.pokemons[attacker_username]  # Получаем объект атакующего покемона
    if attacker.type_pok == 'Wizard':
        attacker = Wizard.pokemons[attacker_username]
    else:
        attacker = Figter.pokemons[attacker_username]
    enemy = Pokemon.pokemons[enemy_username]  # Получаем объект атакуемого покемона
    result = attacker.s_a2(enemy)
    bot.send_message(message.chat.id, result)
    if enemy.hp == 0:
        del Pokemon.pokemons[enemy_username]
        bot.send_message(message.chat.id, f"@{enemy_username} выбывает из игры!")

bot.infinity_polling(none_stop=True)

