my_list = [1, 2, 5, 7, 7, 56, 32]
*unpack, a = my_list
print(unpack)
def processing(*args):
    for a in args:
        print(a)

processing(my_list)