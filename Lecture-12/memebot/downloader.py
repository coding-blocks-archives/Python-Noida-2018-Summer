from urllib import request

def download(url):
    fname = url.split("/")[-1].split("?")[0]
    loc = "temp/" + fname
    print(fname)
    request.urlretrieve(url, loc)
    return loc