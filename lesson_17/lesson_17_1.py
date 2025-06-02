# a = 0
# while a < 2: # невизначена ітерація
#     print("hi")
#     a += 1

# hello = "Hello, boys and girls!" # визначена ітерація
# for i in hello:
#     print(i)

class Counting:
    def __init__(self, count_to, step=1):
        self.current = 1
        self.step = step
        self.count_to = count_to * step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.count_to:
            raise StopIteration
        current = self.current
        self.current += self.step
        return current


class FibonacciIterator:
    def __init__(self):
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        self._current, self._next = (self._next, self._current + self._next)
        return self._current


if __name__ == "__main__":
    my_iter = Counting(5, 1)
    print("my_iter", my_iter)
    # for i in my_iter:
    #     print(i)
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    # print(next(my_iter))
    my_iter_list = iter([1, 2, 3])
    print(my_iter_list)
    print(next(my_iter_list))
    print(next(my_iter_list))
    print(next(my_iter_list))
    # print(next(my_iter_list)) # StopIterration
    print("*"*88)
    my_fib = FibonacciIterator()
    for i in range(20):
        print(next(my_fib))
    print("DO SMTH  HERE s;kdfjdkdslk")
    for i in range(20):
        print(next(my_fib))
    
    print("Forward only!!!")
    numbers = [1, 2, 3]
    i = iter(numbers)
    print(next(i))
    print(next(i))
    print(next(i))

    print("No len!!!")
    my_list = [1, 2, 3]
    my_iter_list = iter(my_list)
    print(len(my_list))
    try:
        print(len(my_iter_list))
    except TypeError as e:
        print(e)

    print("No index!!!")
    print(my_list[1])
    try:
        print(my_iter_list[1])
    except TypeError as e:
        print(e)
    
    iterator = iter([1, 2, 3])
    print(*iterator)
    print(*iterator) # Нічого не виведе, бо ітератор вже вичерпано!
    iterato_2 = Counting(5, 1)
    print(*iterato_2)
    print(*iterato_2) # Нічого не виведе, бо ітератор вже вичерпано!
    # unpack iterator
    iterator = iter((1, 2, 3))
    # Перетворюємо у список
    lst = list(iterator)
    print(lst) 

    iterator = iter([0, 1, 2, 3, 4])
    print(all(iterator)) 
    print(any(iterator)) 
