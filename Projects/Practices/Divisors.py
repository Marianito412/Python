number = int(input("Give me the number: "))
result = ""
x = range(1, number)
for i in x:
    if(number%i == 0):
        result = result + str(i) + ","
print(result)
