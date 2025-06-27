from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1300)
        self.img = self.get_img()
        self.name = self.get_name()
        self.weight = self.get_weight()
        self.hp = randint(80,120)
        self.power = randint(18,22)

        Pokemon.pokemons[pokemon_trainer] = self

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
        if randint(1,2) == 1:
            type_pok = Wizard
        else:
            type_pok = Figter
            
        info_str = f"Имя твоего покемона: {self.name}\n Он {type_pok}\nВес: {self.weight} кг\n У него {self.hp} здоровья и он наносит {self.power} урона"  # Формируем строку с информацией
        print(info_str)  # Выводим информацию в консоль
        return info_str  # Возвращаем строку с информацией






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
        self.mana = randint(8,12)    
    
    
    def heal(self, cost = 1):
        self.mana -= cost
        self.hp += 18
    #more methods in progress
class Figter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.power_boost = randint(5,10)
        #self.hp_boost
    def super_attack(self, enemy):
        dmg = self.power + self.power_boost
        if enemy.hp > dmg:
            enemy.hp -= dmg
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "   
        




