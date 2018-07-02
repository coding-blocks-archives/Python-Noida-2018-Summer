class Library:

    def __init__(self):
        self.books = list()
        self.room = 32
        self.cabin = False

    def __repr__(self):
        return str(self.books)


class Book:

    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def __repr__(self):
        return str([self.name, self.author, self.price])


if __name__ == "__main__":

    lib = Library()

    b1 = Book("Azkabaan ka kaidi", "JKR", 324)
    b2 = Book("Paras Pathar", "JKR", 100)
    b3 = Book("Can love happen twice", "Rajesh", 200)
    b4 = Book("Half Girlfriend", "Chetan Bhabat", 50)

    lib.books += [b1, b2, b3, b4]

    print(lib)

    books = list(filter(lambda item: item.author == "JKR", lib.books))

    print(books)