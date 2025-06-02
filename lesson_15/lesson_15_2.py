from abc import ABC, abstractmethod
import requests


# Абстрактний клас тварини
class Animal(ABC):

    def __init__(self, name:str):
        self.name = name.title()
    
    @abstractmethod
    def make_sound(self):
        pass


# Клас собаки, що успадковує абстрактний клас Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Tweet!"


class BaseAPITest(ABC):
    BASE_URL = "https://api.example.com"

    @abstractmethod
    def test_endpoint(self):
        """Кожен тест повинен реалізувати цей метод"""
        pass

    def get(self, endpoint):
        response = requests.get(self.BASE_URL + endpoint)
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(self.BASE_URL + endpoint, json=data)
        return response.json()


class UserTest(BaseAPITest):
    def test_endpoint(self):
        data = {"username": "test_user", "password": "123456"}
        response = self.post("/login", data)
        assert response["status"] == "success"



if __name__ == "__main__":
    bingo = Dog("bingo")
    tom = Cat("Tomas")
    owl = Bird("Owl")

    for animal in [bingo, tom, owl]:
        print(animal.name, animal.make_sound())
