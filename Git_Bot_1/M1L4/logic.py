from random import randint
import requests
from datetime import timedelta, datetime


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1300)
        self.img = self.get_img()
        self.name = self.get_name()
        self.weight = self.get_weight()
        self.max_hp = randint(80,120)
        self.hp = self.max_hp
        self.power = randint(18,22)
        self.last_feed_time = datetime.now()
        if randint(1,2) == 1:
            type_pok = 'Wizard'
        else:
            type_pok = 'Figter'
        self.type_pok = type_pok
        if self.type_pok == 'Wizard':
            Wizard.pokemons[pokemon_trainer] = self
        else:
            Figter.pokemons[pokemon_trainer] = self
        

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"
 
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["front_default"])
        else:
            return "Pikachu"
    def get_vers_name(self):
        pass
        # url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        # response = requests.get(url)
        # if response.status_code == 200:
        #     data = response.json()
        #     return (data['version_group'])
        # else:
        #     return "Pikachu"
    # Метод для получения имени покемона через API
    


    def get_weight(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'   # Формируем URL для запроса данных о покемоне
        response = requests.get(url)  # Отправляем GET-запрос к API
        if response.status_code == 200:  # Проверяем, успешен ли запрос (код 200)
            data = response.json()  # Преобразуем ответ в JSON-формат
            weight = data['weight']  # Извлекаем вес покемона (в десятых долях килограмма)
            print(f"Вес покемона: {weight / 10} кг")  # Выводим вес в килограммах
            return weight / 10  # Возвращаем вес в килограммах
        else:
            print("Не удалось получить вес покемона.")  # Логируем ошибку
            return None  # Если запрос не удался, возвращаем None
    def info(self):
        info_str = f"Имя твоего покемона: {self.name}\n Он {self.type_pok}\nВес: {self.weight} кг\n У него {self.hp} здоровья и он наносит {self.power} урона"  # Формируем строку с информацией
        print(info_str)  # Выводим информацию в консоль
        return info_str  # Возвращаем строку с информацией
    def get_type(self):
        return self.type_pok
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def vers_name(self):
        return self.vers_name
    def attack(self, enemy):
    
   # Метод для атаки другого покемона.
   # Уменьшает здоровье противника на значение силы текущего покемона.
   # Если здоровье противника становится меньше или равно нулю, объявляется победа.
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return (f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n"
                    f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")
        else:
            enemy.hp = 0
            return (f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!\n"
                    f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")  
class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.max_mana = randint(8,12)  
        self.mana = self.max_mana  
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        return super().feed(self, feed_interval, hp_increase)
    def s_a1(self, enemy):
        self.mana += 2
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        return f'@{self.pokemon_trainer} восстановил(а) ману.\n Мана @{self.pokemon_trainer}: {self.mana}'
    def s_a2(self, enemy):
        cost = 1
        if self.mana < cost:
            self.mana += 2
            if self.mana > self.max_mana:
                self.mana = self.max_mana
            return f'@{self.pokemon_trainer} восстановил(а) ману.\n Мана @{self.pokemon_trainer}: {self.mana}'
        else:
            self.mana -= cost
            self.hp += 20
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            return f'@{self.pokemon_trainer} восстаноил(а) здоровье.\n Здоровье @{self.pokemon_trainer}: {self.hp}\n Мана @{self.pokemon_trainer}: {self.mana} '
    #more methods in progress
class Figter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.power_boost = randint(5,10)
        #self.hp_boost
    def feed(self, feed_interval = 20, hp_increase = 15):
        return super().feed(self, feed_interval , hp_increase)
    def s_a1(self, enemy):
        if enemy.max_hp - enemy.hp < enemy.hp:
            dmg = self.power + self.power_boost
            if enemy.hp > dmg:
                enemy.hp -= dmg
                return (f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n"
                        f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")
            else:
                enemy.hp = 0
                return (f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!\n"
                        f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")  
        else: 
            if enemy.hp > self.power -2:
                enemy.hp -= (self.power-2) 
                return (f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n"
                        f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")
            else:
                enemy.hp = 0
                return (f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!\n"
                        f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")
    def s_a2(self, enemy):
        if enemy.max_hp - enemy.hp < enemy.hp:
            dmg = self.power + self.power_boost
            if enemy.hp > dmg:
                enemy.hp -= dmg
                return (f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n"
                        f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")
            else:
                enemy.hp = 0
                return (f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!\n"
                        f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")  
        else: 
            if enemy.hp > self.power -2:
                enemy.hp -= (self.power-2) 
                return (f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n"
                        f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")
            else:
                enemy.hp = 0
                return (f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!\n"
                        f"Здоровье @{enemy.pokemon_trainer}: {enemy.hp}")       
        

