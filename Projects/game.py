import random
print("===============WELCOME TO PASSGEN===============")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

number = input("how many passwords do you want? ")
number = int(number)

lenght = input("what should the lenght of your password be? ")
lenght = int(lenght)

print("are you ready to get your awesome password? ")

for w in range(number):
    password = ""
    for i in range(lenght):
        password += random.choice(chars)
    print(password)
input("enter anything when done")
