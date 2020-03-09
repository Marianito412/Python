angles = [30,60,90]

def triangle(angles):
    type = ""
    if 90 in angles:
        print("Recto, digite base y altura")
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("Area: " + str(base*altura/2))
    else:
        for angle in angles:
            if (angle>90):
                type = "obtuse"
                break
            else:
                type = "acute"
    print(type)
triangle(angles)
            

        