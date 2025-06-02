

print(all([1, 2, "good"]))
print(all([0, 2, "good"]))

print(any([1, 2, "good"]))
print(any([0, 0, "g"]))
print(any([0, 0, ""]))

print(bin(7))
print(bin(8))

print(chr(1111))

code = '''
def greet(name):
    print("Hello, " + name)

greet("World")
'''
compiled_code = compile(code, '<string>', 'exec')
exec(compiled_code)

my_dict = {"key":"value"}
my_dict_2 = dict(key="value", c=[0, "a"])
print(my_dict_2)

a = 3
b = 2
print(divmod(a, b)) #  (a // b, a % b)

fruits = ['apple', 'banana', 'cherry']
print(list(enumerate(fruits)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return n % 2 == 0

filtered_number = list(filter(is_even, numbers))
print(filtered_number)
print(float("3.14"))

formatted_string = "Some text {} and {}.".format("value1", "value2")
print(formatted_string)

print(hex(42))
print(id(formatted_string))

# value = input("Input value:")

my_number = int("1323442")
print(my_number)

print(isinstance(my_number, int))
print(isinstance(my_number, str))

print(len("1323442"))
print(list("a, b, c"))

print(max(1,2,3))
print(min(1,2,3))

print(ord("ї"))

print(pow(2, 6))

print()

print(range(5))
print(round(3.50))
print(round(2.60))
print(round(2.50))
print(round(2.40))

print(set("123"))
print(str([123]))
print(sum([1, 1, 1, 1]))
print(tuple("hello"))
print(type(my_number))