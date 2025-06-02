def outer(x):
    def inner(y):
        return x + y
    return inner
# add_five = outer(5)
# result = add_five(6)
# print(result) 

def add(x, y):
    return x + y

def diff(x, y):
    return x - y

def calculate(func, x, y):
    return func(x, y)
 
# result_a = calculate(add, 4, 6)
# result_b = calculate(diff, 4, 6)
# print(result_a, result_b)

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello
 
# greet = greeting("Atlantis")
# print(greet())

class MyClass:
    # def __new__(cls, *args, **kwargs):
    #     cls.count = 0

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x
    
    @staticmethod
    def my_static_method(name):
        print(f"This is a static method, {name}")
    
    @classmethod
    def my_class_method(cls):
        cls.count = 1

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Параметризований декоратор для встановлення максимальної кількості повторних спроб
def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    # Спроба виклику функції, яку декоруємо
                    return func(*args, **kwargs)
                except Exception as e:
                    # Обробка помилки та вивід повідомлення про спробу
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    retries += 1
            # Викидаємо виняток, якщо досягнуто максимальну кількість спроб
            raise Exception("Досягнуто максимальну кількість спроб")
        return wrapper
    return decorator

# Параметризоване застосування декоратора
@retry(max_retries=3)
def connect_to_server():
    # Спроба з'єднатися з сервером
    # request_to server
    raise ConnectionError("Не вдалося підключитися до сервера")




if __name__ == "__main__":
    point = MyClass(1)
    # print(point.x)
    # msm = MyClass.my_static_method("Alsdlde")
    # point_2 = MyClass(4785)
    # print(point_2.x)
    # point_2.my_class_method()
    # print(point.count)
    # Виклик функції, прикрашеної декоратором
    say_hello("Dmytro")
    connect_to_server()
