import random
import sys
choices = []

def main():
    print("")
    print("-------------")
    print("1. Add choice\n2. Show List\n3. Choose\n4. Quit")
    print("-------------")
    select = int(input("Choose an option:"))
    if select == 1:
        Add()
    if select == 2:
        Print()
    if select == 4:
        sys.exit()
    if select == 3:
        Choose()

def Add():
    print(" ")
    string_to_add = input("Write the choice you wish to add: ")
    choices.append(string_to_add)
    main()

def Print():
    i = 1
    print("----------------------")
    for choice in choices:
        print(str(i)+". "+choice)
        i = i+1
    print("----------------------")    
    input("Press any key to return to main menu")
    main()

def Choose():
    print("You shall choose: "+random.choice(choices))
    print("I have spoken")
    input("Press any key to return to main menu")
    main()

if __name__ == "__main__":
    main()   