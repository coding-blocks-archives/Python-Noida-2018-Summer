class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author

#
# home = Book("Home Alone", "Random author")
# mistake = Book("Any Book", "Chetan Bhagat")
#
# f = open("persist.db", "wt")
#
# l = [home, mistake]
#
# for item in l:
#     f.write(item.name + ";" + item.author+"\n")
#
# f.close()


f = open("persist.db")

l = []

for line in f:
    temp = line.split(";")
    l.append(Book(temp[0], temp[1]))

for book in l:
    print(book.name, ",",book.author)