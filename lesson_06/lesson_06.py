
user_age = 18 # int(input("Enter your age:"))
is_student = False
has_experience = True

if 18 > user_age > 1 and is_student: #умова_1
    print("Hello!") # Код, який виконається, якщо умова_1 правдива
elif user_age >= 18 or not is_student: #умова_2
    print("Good morning!") # Код, який виконається, якщо умова_2 правдива
else:
    print("Hi bro")# Код, який виконається, якщо жодна з умов не виконується

if (user_age >= 18 and is_student) or (has_experience and user_age < 30):
    print("You are either an adult student or have experience and are under 30.")
else:
    print("You don't meet any of the specified conditions.")

count = 0
while count <= 5:
    print(count)
    count = count + 1 # count +=1

some_str = "qwerty"
for char in some_str:
    print(char)

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

person_0 = {"name": "John", "age": 30, "city": "New York", "student": True, "year": 2022}
# for key, value in person_0:
#     print(key, ":", value)  ## Код не працює!!!

print(person_0.items())
for key, value in person_0.items():
    print(key, ":", value)

person_2 = {"name": "Ace", "age": 16, "city": "New York", "student": True, "year": 2025}
person_3 = {"name": "Bill", "age": 20, "city": "New York", "student": False, "year": 2022}
person_1 = {"name": "Denny", "age": 20, "city": "New York", "student": True, "year": 2025}

students = [person_0, person_2, person_3, person_1]
# students = [
#     {"name": "John", "age": 30, "city": "New York", "student": True, "year": 2022},
#     {"name": "Ace", "age": 16, "city": "New York", "student": True, "year": 2022},
#     {"name": "Bill", "age": 20, "city": "New York", "student": False, "year": 2022}
# ]
for person in students:
    print(person["name"])
    name  = person.get("name", "")
    age_of_person = person.get("age", 14)
    is_student = person.get("student", False)
    year_of_lerning = person.get("year", 2022)

    if age_of_person >= 18:
        print("You are an adult")
        if is_student:
            print("And you are a student")
            current_year = 2025

            if current_year - year_of_lerning > 1:
                print("You are not first year student")
    else:
        print("You are not adult")

for i in range(10):
    if i == 7:
        #print("Break викликаний на i =", i)
        break
    elif i == 4:
        #print("continue викликаний на i =", i)
        continue
    else:
        print(i)
else:
    print("Break не викликаний")


if user_age > 12:
    pass # IDK
else:
    pass #this is need for...
