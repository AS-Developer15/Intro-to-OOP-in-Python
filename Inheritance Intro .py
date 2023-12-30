# Single Inheritance


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet():
        print("Hello, {} welcome to this program.".format(self.name))


class Student(Person):
    def __init__(self, name, age, mtr) -> None:
        self.mtr = mtr
        super().__init__(name, age)


student = Student("Aradhya", 12, 56)
print(student.__dict__)
print("Does the code belong to Person Class", isinstance(student, Person))
print("Does the code belong to Student Class", isinstance(student, Student))
"""

# Single Inheritance
"""


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet():
        print("Hello, {} welcome to this program.".format(self.name))


class Student(Person):
    def __init__(self, name, age, mtr) -> None:
        self.mtr = mtr
        super().__init__(name, age)


student = Student("Aradhya", 12, 56)
print(student.__dict__)
print("Does the code belong to Person Class", isinstance(student, Person))
print("Does the code belong to Student Class", isinstance(student, Student))
