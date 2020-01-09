str = "9plus2145minus2"

#Version One
lst = str.replace("plus", " + ").replace("minus", " - ").split()
result = int(lst[0])
i = 1
while i<len(lst):
    result = result + int(lst[i] + lst[i+1])
    i = i+2
print(result)

#Version Two
print(eval(str.replace("plus", " + ").replace("minus", " - ")))
        

    