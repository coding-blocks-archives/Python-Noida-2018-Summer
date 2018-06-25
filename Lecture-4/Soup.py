from bs4 import BeautifulSoup

# file = open("Hello.html")

from urllib import request


def hook(index=0, frame_size=0, total=0):

    downloaded = index * frame_size

    per = downloaded/total * 100

    print(int(per))


request.urlretrieve("https://i.ytimg.com/vi/kYnx7nPw-xo/maxresdefault.jpg",
                    "bunny.jpg", hook)



#
# file = open("google.html")
#
# soup = BeautifulSoup(file.read(), "html.parser")
#
# print(soup.a)
#
# l = soup.find_all('a')
#
# for item in l:
#     if item.has_attr("href"):
#         print(item["href"])
#
#

