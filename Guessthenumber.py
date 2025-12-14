#Game for guessing random number from 1 to 100 
import random
target=random.randint(1,100)
while True:
    userinput=int(input("enter your number: "))
    if(userinput==target):
        print("Yeyyy!!!! you guessed the right number")
        break
    elif(userinput<target):
        print("ohh sorry your number is small ")
    else:
        print("ohh sorry your number is big")
print("---Game Over---")