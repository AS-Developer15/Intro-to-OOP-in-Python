# Class Instantiation with Instance Method


class Person:
    def __init__(self, Name: str, Age: int):
        self.Name = Name
        self.Age = Age

    # Creating a Instance Method
    def greet(self):
        print(f"Hello {self.Name} welcome to this OOP Program. ")


# Code related to Person Class

# Creating Dictionary from the given data
person = Person("Shreya", 14)
dicval = person.__dict__
print(dicval)
# Referencing to instance variable
print("The name of the person is :", person.Name)
print("The age of the person is  :", person.Age)
person.greet()
