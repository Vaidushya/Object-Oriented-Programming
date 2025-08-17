class dog_breed:
    species = "dog"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

flame = dog_breed('blu', 10, 'Labrador')
litening = dog_breed('woo', 15, 'Poodle')

print("Blu is a {}".format(flame.species))
print("Woo is also a {}".format(litening.species))

print("{} is {} years old".format(flame.name, flame.age))
print("{} is a {}".format(flame.name, flame.breed))
print("{} is {} years old".format(litening.name, litening.age))
print("{} is a {}".format(litening.name, litening.breed))