#import the random module
import random

print("Hello!")
while True:
    print(" May i know your name?: ")
    userName=input().strip()
    #Ensure the name is neither empty nor contains a number
    if userName== "":
        print("You need to enter your Name")
        continue
    elif not userName.isalpha():
        print ("alphabets only allowed")
        continue
    else:
        break

print ("Hello " + userName + "!," + " welcome to my Dice game")
#Computer takes a random number
secretNumber = random.randint(1,6)
print ("i just rolled a dice")

#only 3 chances to guess
guessNo=0
for guessChance in range(1,4): 
    guessNo+=1
    try:
        guess=int(input("take a guess: "))
        if guess < 0:
            print ("That cant be a dice")
            continue
        elif guess == "": #No empty guess allowed
            print ("you need to enter a number")
            continue
    except ValueError:
        print ("You need to enter a number")
        continue
    if guess < secretNumber:
        print ("Oops... that guess is too low")
    elif guess > secretNumber:
        print ("You guessed higher")
    else:
        break
    
    #output when it is guessed on first attempt is a bit different
if guessNo==1 and guess==secretNumber:
        print("Congrats " + userName + "!," + " You guessed right after " + str(guessNo) + " try" )
elif guess == secretNumber:
    print("Congrats " + userName + "!," + " You guessed right after " + str(guessNo) + " tries" )
else:
    print("You exhausted the available chances, the number is: " + str(secretNumber))
