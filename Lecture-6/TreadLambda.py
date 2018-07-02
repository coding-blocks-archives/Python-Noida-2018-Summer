from threading import Thread

from urllib import request

import os

# t = Thread()
#
# t.run = lambda: print("Hello World")
#
# print("Boss is boss")
#
# t.start()


# f_name = url.split("/")[-1]
#
# Thread(target=lambda: request.urlretrieve(url, f_name)).start()

os.mkdir("images/download/")

for i in range(10):
    url1 = "http://dlp2gfjvaz867.cloudfront.net/product_photos/40229682/Ryuk_18X12_original.jpg"
    url2 = "https://cdn.vox-cdn.com/thumbor/w8EiSqPEUuBjj7iG-fxukrVIFXk=/99x0:1179x720/1200x800/filters:focal(99x0:1179x720)/cdn.vox-cdn.com/uploads/chorus_image/image/50878485/death-note.0.0.jpg"

    f_name1 = "images/download/" + str(i) + url1.split("/")[-1]
    f_name2 = "images/download/" + str(i) + url2.split("/")[-1]
    Thread(target=lambda: request.urlretrieve(url1, f_name1)).start()
    Thread(target=lambda: request.urlretrieve(url2, f_name2)).start()

