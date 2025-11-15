class Dog:

    animal = 'animal'


    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color




Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)


print("\nAccessing class variable using class name")
print(Dog.animal)






