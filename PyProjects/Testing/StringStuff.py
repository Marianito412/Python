def center():
    string = """hello world"""
    string = string.center(30)
    for i in range(4):
        string = string + "\n" + str(i).center(30)
    print(string)

def center2():
    string = """hello world"""
    string = '{:-^50}'.format(string)
    for i in range(4):
        string = string + "\n" + '{:-^50}'.format(str(i))
    print(string)


def hello(nam):
    return nam

def asdf(name):
    return "Hello "+name

url = "https://stream-1-1.loadshare.org/stream/3/VideoID-d3uvIIVH/nCAGMm/jZerET/E9z5EA/548foB/,360,.urlset/index-v1-a1.m3u8?token=ip=186.159.197.207~st=1587927662~exp=1587942062~acl=/*~hmac=0859b0020d28bb4da4b8a46e32e33ae96f9bc3c45d9a8446af4759ad0cd01c1b"
print(url.split("index")[0])