import json
import random
import requests
import os
import sys
import math

from datetime import datetime


def httpbin(url:str = 'https://httpbin.org/basic-auth/user/pass'):
    r = requests.get(url, auth=('user', 'pass'))
    return r


if __name__ == "__main__":
    r = httpbin()
    print(r.status_code)
    result = math.sqrt(25) # отримуємо корінь квадратний з числа
    print(result)
    now = datetime.now()  # отримуємо поточне значення часу
    print(now)
    random_number = random.randint(1, 10) # отримуємо випадкове ціле (int) число від 1 до 10
    print(random_number)
    current_directory = os.getcwd()  # отримуємо шлях до поточної папки
    print(current_directory)
    print(sys.version)
    print(dir(print))
    print(dir())
    print(dir(__builtins__))
    # from json import *
    # print(loads(dumps('123')))
    print(json.__file__)
