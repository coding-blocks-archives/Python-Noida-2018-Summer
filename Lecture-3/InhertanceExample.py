class Car:

    def __init__(self, color = "White", slogan = "Jai guru dev"):
        self.doors = 4
        self.seats = 4
        self.color = color
        self.slogan = slogan

    def start(self):
        print("I am car, I am starting ")

    def acc(self):
        print("dhrooom dhrooom")

    def stop(self):
        print("I am car, I am stopping ")

    def __add__(self, dusra):
        print("Abe tu add karega be?")


class Maruti(Car):

    def __init__(self, abs = True, color = "Silver", slogan = "Music is my soul"):
        super().__init__(color, slogan)
        self.seats = 5
        self.abs = abs



    def honk(self):
        print("pee pee poo poo")

    def start(self):
        super().start()
        print("I am Maruti, I run like a horse")


first = Car()
print(first.color)
print(first.slogan)

second = Car("Red")
print(second.color)
print(second.slogan)

third = Car("Red", "Bhai ki jai")
print(third.color)
print(third.slogan)

# print(third.start())

fourth = Maruti(False, "Pink", "I play Dota")
fourth.start()
fourth.acc()
fourth.stop()
fourth.honk()

print(fourth.doors)
print(fourth.seats)
print(fourth.color)
print(fourth.abs)

fifth = Maruti()

print(fifth.color)

s = first + fifth

print(s)



