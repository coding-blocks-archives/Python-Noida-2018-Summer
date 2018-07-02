
def square(x):
    return x*x

sq = lambda x : x*x

print(sq(32))

l = [345, 5435, 54, 345]


s = list(map(lambda x: x/2, l))

print(s)

big = list(filter(lambda x: x > 100, l))

print(big)