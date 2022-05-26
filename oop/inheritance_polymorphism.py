class Animal():
    def __init__(self):
        print("Animal Created")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Created Dog")

    def speak(self):
        print("Woof")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Created Cat")

    def speak(self):
        print("Meow")



if __name__ == "__main__":
    fido = Dog()
    whiskers = Cat()
    for pet in [fido, whiskers]:
        print(type(pet))
        pet.speak()