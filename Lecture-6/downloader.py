import time
import threading


def download(name):
    for i in range(5):
        time.sleep(1)
        print("We have downloaded", i, "of 5", name)


class Worker(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        download(self.name)


w1 = Worker("anuj.mp4")
w2 = Worker("yash.mp4")


w1.start()

time.sleep(2)

w2.start()

print("Hello from CB")

for item in threading.enumerate():
    if(item.name == "anuj.mp4"):
        item.join()





