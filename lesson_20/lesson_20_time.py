import time

current_time = time.localtime()
print(current_time)
# DST - Daylight Saving Time — це англомовне позначення переходу на літній час
print("Year", current_time.tm_year)
print("Month", current_time.tm_mon)
print("Day", current_time.tm_mday)
some_time = time.asctime((1980, 1, 2, 3, 4, 5, 2, 2, 2))
print(some_time)
some_time = time.asctime(current_time)
print(some_time)
my_real_time = time.asctime() # my_real_time_2 = time.asctime(time.localtime())
print("my time", my_real_time)
# час епохи
print("unix time 0", time.ctime(0))
nix_time_now = time.ctime(1686547846)
print("unix time 1", nix_time_now)
time_now =time.ctime(1722270782)
print("unix time 2",time_now)
print(time.time())
time.sleep(0.5) # НАЙЖАХЛИВІШИЙ СПОСІБ !!
print(time.time())
print(time.ctime(time.time()))
some_day_1 = "Sep 20, 2022"
some_day_2 = "Dec 21, 2022"
pattern = "%b %d, %Y"
my_datetime = time.strptime(some_day_1, pattern)
print(my_datetime)
my_datetime_2 = time.strptime(some_day_2, pattern)
print(my_datetime_2)
print(time.strptime("19:45:55", '%H:%M:%S'))

# Рядок з часом
time_string = '2023/12/31 23:59:59'
# Формат рядка
format_string = '%Y/%m/%d %H:%M:%S'
# Перетворення рядка у структуру часу
time_obj = time.strptime(time_string, format_string)
print(time_obj)

good_time_output = time.strftime("Now year %Y %m month and day is %d time is: %H:%M",
                     time.localtime())
print(good_time_output)