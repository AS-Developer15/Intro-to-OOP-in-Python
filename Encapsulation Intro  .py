# Property Method
# Getter And Setter in Python


class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split()
        self.first = first_name
        self.last = last_name

    @fullname.deleter
    def fullname(self):
        print("Deleting Content")
        self.first = None
        self.last = None


emp_1 = Employee("Jhon", "Smith")
emp_1.fullname = "Tommy Schafer"
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first)
print(emp_1.last)
