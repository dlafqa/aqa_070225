from pony.orm import *
from pony.orm.core import sql_logger

db = Database()

sqlite = dict(
            provider='sqlite',
            filename='mybase.db',
            create_db=True
            )

mysql = dict(
            provider='mysql',
            host="127.0.0.1",
            user="student",
            passwd="welcome2qauto",
            db="person"
            )

db.bind(sqlite)

class Person(db.Entity):
    name = Required(str)
    age = Optional(int)
    cars = Set('Car')


class Car(db.Entity):
    maker = Required(str)
    model = Optional(str)
    owner = Required(Person)

db.generate_mapping(create_tables=True)
set_sql_debug(True) # щоб бачити скл-команди

@db_session
def add_person(name:str = "Isaak", age:int = 21):
    p1 = Person(name=name, age=age)
    c1 = Car(maker="Audi", model="AAs", owner=p1)
    db.commit()

#add_person()

@db_session
def output():
    print(Car.select().show())
    print(Person.select().show())
    # with db_session:
    # result = select(p for p in Person if p.age > 20)
    # for person in result:
    #     print(person.name, person.age)

output()
