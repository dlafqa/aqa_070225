# lage_squares = [i*i for i in range(500)]
# print(lage_squares)

lage_squares_gen = (i*i for i in range(500))
print(next(lage_squares_gen))
print(next(lage_squares_gen))
print(next(lage_squares_gen))
for i in range(5):
    print(next(lage_squares_gen))

print("*"*88)

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
for value in gen:
    print(value)

def my_generator(n): 
    # Ініціалізуємо лічильник
    value = 1 
    # Цикл виконується доти, доки лічильник не стане менше n
    while value <= n:
        # Повертаємо поточне значення лічильника
        yield value
        # Збільшуємо лічильник
        value += 1

print("*"*88)
# Виконуємо ітерацію генератора
for value in my_generator(7):
    # Виводимо кожне значення, отримане від генератора
    print(value)

generator = my_generator(3)
print(next(generator))  # 0
print(next(generator))  # 1
print(next(generator))  # 2
#print(next(generator))
print("generator:", *generator)

numbers = [1, 2, 3, 4, 5]
iterator = map(lambda x: x * 2, numbers)
print(iterator)
print(next(iterator))  # 0
print(next(iterator))  # 1
for i in iterator:
    print(i)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

iterator = zip(names, ages)
print(iterator)  # <zip object at 0x...>
print(next(iterator))
print(list(iterator))
