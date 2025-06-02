base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]

def add(a, b):
    return a + b

pow_num = list(map(pow, base_numbers, powers))
print(pow_num)

sum_num = list(map(add, base_numbers, powers))
print(sum_num)

list_of_words = ['apple', 'banana', 'cherry']
upper_words = list(map(str.upper, list_of_words))
print(upper_words)

# zip
list1 = [1, 2, 3, 0]
list2 = ['a', 'b', 'c', 'd']
zipped = zip(list1, list2)
print(list(zipped))

list3 = [4, 5, 6, 10]
sums = [a + b for a, b in zip(list1, list3)]
print(sums)