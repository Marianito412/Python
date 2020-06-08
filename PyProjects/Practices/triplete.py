from math import sqrt

def triplete():
    a = int(input("Lado 1: "))
    b = int(input("Lado 2: "))
    c = int(input("Lado 3: "))

    if sqrt(a**2 + b**2) == c:
        print("Triplete válido")
    if sqrt(a**2 + c**2) == b:
        print("Triplete válido")
    if sqrt(c**2 + b**2) == a:
        print("Triplete válido")
    else:
        print("triplete inválido")
#triplete()

def recursiveTripleta():
    a = int(input("Lado 1: "))
    b = int(input("Lado 2: "))
    c = int(input("Lado 3: "))
    lista = [a, b, c]
    for i in range(len(lista)):
        if sqrt(lista[i]**2 + lista[i-1]**2) == lista[i-2]:
            print("Tripleta válida")
            break
        elif i == 2:
            print("Tripleta inválida")
recursiveTripleta()