# Class Instantiation with Static Methods


class people:
    @staticmethod
    def func_one(val):
        if val >= 18:
            return True
        else:
            return False

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.is_adult = self.func_one(self.age)


person = people("Unknown", 19)
print(person.is_adult)
