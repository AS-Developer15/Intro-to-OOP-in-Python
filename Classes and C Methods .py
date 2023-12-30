# Class Instantiation with Class Methods
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @classmethod
    def ylive(cls, name, byear):
        age = 2023 - byear
        return cls(name, age)


person_a = Person.ylive("Aradhya", 2009)
print(person_a.age, person_a.name)
