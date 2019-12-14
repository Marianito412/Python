import random
choices = ["0", "1", "2"]
tests = int(input("number of experiment:" ))
win_count = 0
lost_count = 0
for i in range(tests):
    print("")
    print("Starting experiment number " + str(i))
    
    boxes = ["car", "goat", "goat"]
    
    #Player picks a random box
    c1 = int(random.choice(choices))
    choice = boxes[c1]
    print("First pick: "+choice)

    #Reveal the leftover box
    for i in range(2):
        lft = boxes[i]
        if i != c1 and "goat" in boxes[i]:
            print("Revealed " + lft)
            del boxes[i]
    
    #Switch
    boxes.remove(choice)

    if boxes[0] == "car":
        print("WON!!")
        win_count = win_count + 1
        
    else:
        print("LOST!!")
        lost_count = lost_count + 1

    print("")
print("Amount of wins:" + str(win_count))
print("Amount of loses:" + str(lost_count))

print("Number of experiments: " + str(tests))
wer = win_count/(tests) 
print("Win / Test Ratio: " + str(wer))
print("Success percentage " + str(wer*100)) 
    
