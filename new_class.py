class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person("John", 23)
mariam = Person("Mariam", 18)

print(john.name + " is " + str(john.age) + " years old!!!")
