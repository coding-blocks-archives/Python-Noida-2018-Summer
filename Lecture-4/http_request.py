from urllib import request

data = request.urlopen("http://google.com/35647689654321")

print(data.status)


