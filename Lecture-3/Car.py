class Car:

    population = 0

    slogan = "Default slogan"

    def __init__(self, name = "Default Name"):
        self.name = name
        Car.population += 1

    def start(self, sound):
        print(sound)

    def start(self, sound, bull):
        print(sound)

    def set_slogan(self, data):
        Car.slogan = data


my_car = Car("Anuj ki gadi")
my_car.set_slogan("Code is fun")

print(my_car.name)

bhavya_sports = Car("My red farrari")
bhavya_sports.set_slogan("Bhavya")

print(bhavya_sports.name)

my_car.start("Blob blob")

print(my_car.slogan)

print(Car.population)


ishan_car = Car()

print(ishan_car.name)

