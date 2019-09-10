'''
Program picks a pseudorandom number between 0 and 1023 and keeps promting the
user to guess until they guess the number picked 
Hina Sekine
'''
# Program initliazation 
import random 

print("Hello there!\nI have some skittles between 0 and 1023!\n")

candyNum = random.randint(0, 1023)

# User guesses 
userGuess = ''
while userGuess != str(candyNum):
    userGuess = input("Your Guess: ")
    
    if userGuess.isdigit() == False:
        print("That's a quantity of candy? :o")
    else: 
        if int(userGuess) > 1023:
            print("That's not in the range...")
        elif int(userGuess) < candyNum:
            print("That's too low...")
        elif int(userGuess) > candyNum:
            print("That's too high...")

print("Yay you got it!\nThanks for playing! ;)")
