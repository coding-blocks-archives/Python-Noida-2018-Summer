def run():
    print("Hello green fields")
    return 10


v = run()

print(v)

def fact(num):
    if num == 1:
        return 1

    return num * fact(num - 1)

# bhaag = run
#
# print(run)
# print(bhaag)


print(fact(3))

print("Hello")

print(__name__)