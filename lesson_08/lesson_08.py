
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Помилка ділення на нуль: {e}")
        result = None
    except TypeError as e:
        print(f"Помилка даних: {e}")
        if not isinstance(a, (int,float)):
            a = float(a)
        if not isinstance(b, (int,float)):
            b = float(b)
        return divide(a, b) 
    return result


def sum(a, b):
    try:
        return a + b
    except TypeError:
        print("Do not use None here")
        return None


def mid_processor(list_store:list):
    list_len = len(list_store)
    index_of_mid_element = list_len // 2
    try:
        return list_store[index_of_mid_element]
    except (IndexError, ValueError):  # multi-exeption
        print("Empty list. Dont do it again!!!")
        # return 0
    except:
        print("Do smth here")


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль.")
    else:
        "Блок else виконується, якщо в блоку try не виникло жодного виключення"
        print(f"Результат ділення {a} на {b}: {result}")
    finally:
        # наприклад збереження в файл
        print("Цей блок завжди виконується, незалежно від того, чи виникла помилка чи ні")


# while True:
#    # try:
#         print("*"* 88)
#    # except:   
#    #     pass # KeyboardInterrupt


def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    return age


def check_email(mail:str):
    if not isinstance(mail, str):
        raise TypeError("String type only expected")
    if mail.count("@") < 1:
        raise ValueError("@ expected in mailbox")
    return mail


def sum_2(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "int, float is expected"
    #if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    #   raise AssertionError("int, float is expected")
    try:
        return a + b
    except TypeError:
        print("Do not use None here")
        return None

if __name__ == "__main__":
    
    divide(10, "0")
    print("Hello")
    # divide(10, "a")
    sum(10, "a")

    # (a + b) / c
    a = 10
    b = 5
    c = 3
    result = divide(sum(a, b), c)
    print(result)

    a_plus_b = sum(a, b)
    a_plus_b_div_c = divide(a_plus_b, c)
    print(a_plus_b_div_c)

    my_list = [2, 4, 5, 3, 2, 7, 4]
    print(mid_processor(my_list))
    print(mid_processor([1,2,3]))
    print(mid_processor([1]))
    print(mid_processor([]))

    print(check_email("some@gmail.com"))
    print(check_email("s@g.c"))
    print(check_email("@"))
    # print(check_email(""))
    # print(check_email(1))
    print(sum_2("a",0))