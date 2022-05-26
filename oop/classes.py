class Dog():

    #class object attribbute, same for all instances
    species = 'mammal'

    def __init__(self, breed:str, name:str, spots:bool):
        #instance attributes
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self):
        print(f'WOOF my name is {self.name}.')

if __name__ == "__main__":
    dog = Dog("Chihuaha", "Fido", False)
    dog.bark()