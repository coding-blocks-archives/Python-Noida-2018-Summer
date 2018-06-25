file = open("abc.txt")

# read whole file
# a = file.read()
# print(a)

# read file by max char count
# a = file.read(4)
#
# print(a)

# read by line
a = file.readline()
file.readline()
b = file.readline()
print(a, b)


for line in file:
    print(line, end="")

for line in file:
    print(line, end="")


