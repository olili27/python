# class Person:
#     name: str
#     age: int
#
# p = Person()
# print(p.name, p.age) # cannot read attributes that have been assigned values
#
#
# class Person:
#     name: str = "person"
#     age: int = 25

class Person:
    def __init__(self, name, age) -> None:
        # assign instance variables default values
        # self.name = "name"
        # self.age = 25

        # initiate instance variables  with the values passed via the constructor
        self.name = name
        self.age = age


class Man(Person):
    def __init__(self, name, age, number_of_wives, number_of_fights) -> None:
        super().__init__(name, age)
        self.wives = number_of_wives
        self.fights = number_of_fights


p = Person("dan", 32)
m = Man("tim", 25, 4, 2)
print(p.name, p.age)
print(m.name, m.age, m.wives, m.fights)

if __name__ == "__main__":
    pass
