class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound = 'Woff'):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound = 'Bark'):
        return f"{self.name} says {sound}"

pia = Dog('Pia', 4)
print(pia.speak())

bella = GoldenRetriever('Bella', 7)
print(bella.speak())