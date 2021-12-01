from time import sleep

def slowPrint(text):
    for i in text:
        print(i, end="")
        time.sleep(0.01)
        
slowPrint("Birch shouldn't be here")
slowPrint("Neither should Dylan, but here I am anyway")
