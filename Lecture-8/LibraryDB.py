from peewee import SqliteDatabase, Model

from peewee import *


blah = SqliteDatabase("library.db")


class Base(Model):
    class Meta:
        database = blah


class User(Base):
    username = PrimaryKeyField()
    password = CharField(unique=True)


class Book(Model):
    id = PrimaryKeyField()
    name = CharField()
    author = CharField()

    class Meta:
        database = blah


blah.connect()

blah.create_tables([Book, User])

b1 = Book.create(name="Azkabaan ka kaidi", author="JKR")
b2 = Book.create(name="Kaidi", author="whbef")


# books = Book.select().where(Book.author == "JKR")
books = Book.select().order_by(Book.name.desc())

for book in books:
    print(book.name, book.author)


# def createUser(username, password):
#     try:
#         return User.create(username=username, password=password)
#     except IntegrityError as e:
#         print(e)

#
# anuj = createUser(1234, "Prime")
# mohit = createUser(2345, "Prime")
#
# users = User.select()
#
# for user in users:
#     print(user.username, user.password)











