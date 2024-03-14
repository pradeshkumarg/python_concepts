class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # method
    def bark(self):
        print(f"{self.name} says woof !!")


class WorkingDog(Dog):
    # Additional attribute specific to WorkingDog
    working_type = "Herding"

    def bark(self):
        print(f"{self.name} says: Yip yip!")

    # Additional method specific to WorkingDog
    def work(self):
        print(f"{self.name} is {self.working_type}!")

if __name__ == "__main__":
    jack = Dog("Jack", "Kombai")
    tommy = Dog("Tommy", "Pomeranian")
    dog3 = WorkingDog("dog3", "Lab")

    jack.bark()
    tommy.bark()
    dog3.work()
