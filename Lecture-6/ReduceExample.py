from functools import reduce

li = [567, 567, 456, 567, 657]

s = reduce(lambda x, y: x.union({y}), li, set())




print(s)