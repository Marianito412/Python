from keyboard import press, release, send, add_hotkey, wait
from time import sleep
from threading import Thread

# This script is meant to automate the boring process of flying the Opressor MkII in GTA Online
# Press shift+i to toggle the automatic flight

def boost():
    release("ctrl+shift")
    send("x")

def autofly():
    i = 0
    while True:
        global kill
        if kill == False:
            #Go up for 2 sec
            press("ctrl+w")
            sleep(2)
            release("ctrl+w")

            #Go down for 1.5 sec
            press("shift")
            sleep(1.5)
            release("shift")

            if i%2==0:
                boost()
                sleep(2)
                i=0;
            i = i+1

def killTask():
    global kill
    kill = not kill
    print("Killed" if kill else "Running")

if __name__ == "__main__":
    kill = True
    fly = Thread(target=autofly)
    fly.start()
    add_hotkey("shift+i", killTask)
    wait()
