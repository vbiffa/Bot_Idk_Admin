from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.weight = self.get_weight()

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
    
         info_str = f"Имя твоего покемона: {self.name}\nВес: {self.weight} кг"  # Формируем строку с информацией
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



