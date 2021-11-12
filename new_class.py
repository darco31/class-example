class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + " is walking")

    def speak(self):
        print(
            f"Hello my name is {self.name} and I am {str(self.age)} years old")


john = Person("John", 23)
mariam = Person("Mariam", 18)

print(f"{john.name} {str(john.age)}")
john.walk()
john.speak()
mariam.walk()
