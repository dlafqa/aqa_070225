from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

base = declarative_base()
engine = create_engine("sqlite:///mybase.db", echo=True) 
# "sqlite://" - база створюється в пам'яті


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class Department(base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee", back_populates="department")


class Employee(base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))
    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department", back_populates="employees")

    def __repr__(self):
        return f"{self.name} from department id:{self.department_id}"

base.metadata.create_all(engine)

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

# Додавання нового користувача
def add_new_item_to_user(name='Andrey', age=30, session=session):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
# add_new_item_to_user("Petro", 25)


def select_all_user():
    all_users = session.query(User).all()
    return all_users


def select_all_department():
    all_dep = session.query(Department).all()
    return all_dep


def select_all_employee():
    all_emp = session.query(Employee).all()
    return all_emp


def out_users_data(all_users:list):
    for user in all_users:
        print(user.age, user.name, user.id)


def out_departments(departments_list:list):
    for i in departments_list:
        print(i.name, i.employees)


def out_employees(employees_list:list):
    for i in employees_list:
        print(i.name, i.department_id)


if __name__ == "__main__":
    all_users = select_all_user()
    out_users_data(all_users)

    # it_department = Department(name='IT')
    # hr_department = Department(name='HR')

    # john = Employee(name='John', department=it_department)
    # alice = Employee(name='Alice', department=hr_department)
    # bob = Employee(name='Bob', department=it_department)

    # session.add_all([it_department, hr_department, john, alice, bob])
    # session.commit()
    all_dep = select_all_department()
    out_departments(all_dep)
    all_e = select_all_employee()
    out_employees(all_e)
