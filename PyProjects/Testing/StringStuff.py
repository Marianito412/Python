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
center2()