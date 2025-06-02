
class Car:

    def __init__(self, maker, model):
        self.maker = maker
        self.model = model
        self.__is_engine_run  = False

    @property
    def engine_run(self):
        return self.__is_engine_run

    def is_engine_run(self):
        self.__is_engine_run = not self.__is_engine_run
    
    def __del__(self):
        print(f"{self.model} is delete")
    
    def __str__(self):
        return f"It is {self.model} develop by {self.maker}"
    
    def __repr__(self): # можна не задавати якщо є __str__
        return f"It is {self.model} develop by {self.maker}"
    
    def __len__(self):
        return 42

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)
    
    def __eq__(self, c):
        return self.x == c or self.y == c

class Person():
    def __init__(self, age:int = 0) -> None:
        self.__age = age
        self.__name = ""

    @property  # it is getter
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, years:int):
        #self.__age = years
        if not isinstance(years, int):
            raise ValueError("add_year must be int")
        if years >= self.__age:
            self.__age = years
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if not isinstance(new_name, str):
            raise ValueError("new_name must be str")
        if len(new_name) >= len(self.__name):
            self.__name = new_name

class Human():
    def __init__(self, name = "", age:int = 0) -> None:
        self.age = age
        self.name = name


if __name__ == "__main__":
    my_car = Car("Toyota", "Camry")
    print("is run?", my_car.engine_run)
    my_car.is_engine_run()
    print("is run?", my_car.engine_run)
    print(my_car)
    print("len", len(my_car))
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Len stack", len(stack))
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    result = point1 + point2
    print(result.x, result.y, type(result))
    print(point1 == 4)
    print(point2 == 4)

    print("PERSON")
    p = Person(3)
    print(p.age)
    p.age = 2
    print(p.age)
    p.age = 4
    print(p.age)
    p.name = "A"
    print(p.name)
    p.name = "Bb"
    print(p.name)
    # p.name = 7
    # print(p.name) # Exception ValueError: new_name must be str
    h = Human("Alex", 5)
    h.age = -120
    h.name = list("woeu3ui4")
    print(h.age, h.name)


