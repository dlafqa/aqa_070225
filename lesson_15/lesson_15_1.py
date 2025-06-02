# LEGB
# L-local - локальній області видимості всередині функції 
# E-enclosing - у локальних областях видимості охоплюючих функцій
# G-global - глобальна
# B-built-in  - вбудовані
import json

def _print(arg):
    return arg

# def sum(a,b):
#     return a + b

print(sum([1,1,1,1,1,1]))

# print(_print.__builtins__)

x = 2 # Global

def example_function():
    # x = 10 # Local
    print(x)

example_function()

def outer_function():
    z = 30

    def inner_function():
        print(z)  # Звертається до змінної з більш високого рівня

    inner_function()
outer_function()

PDV = 20
class MyBuh():
    b = 5  # Enclosing

    def count(self):
        print("b>", self.b)
        print("ПДВ:", PDV)

coun_buh = MyBuh()
coun_buh.count()
print(PDV)


class Parent1:
    x = 10
    common_field = "значення від Mama"
    def method1(self):
        print("Виклик методу method1 з Parent1")


class Parent2:
    y = 20
    common_field = "значення від Papa"
    def method2(self):
        print("Виклик методу method2 з Parent2")
# 4
#             3.1     #3.2   #3......
class Child(Parent1, Parent2):  # успадковуємо від обох батьків
    # 2
    def access_common_field(self):
        # 1
        common_field_from_mama = Parent1.common_field
        common_field_from_dad = Parent2.common_field
        print("Значення common_field з Mama:", common_field_from_mama)
        print("Значення common_field з Dad:", common_field_from_dad)
        print("From self:", self.common_field)


child = Child()
child.method1()  # Виведе: Виклик методу method1 з Parent1
child.method2()  # Виведе: Виклик методу method2 з Parent2
print(child.x)
print(child.y)
child.access_common_field()