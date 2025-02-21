import random #import the random function

def noAttempts():
    print(f"Sorry, you've used all 5 attempts. The number was {number}.")



# Start game
def getGuess():#define a function to get a guess
    global attempts#make the attempts global and be able to use everywhere
    attempts += 1#add a attempt to the variable
    return int(input("Enter your guess: "))#get the guess



def checkGuess(guess):#make a function to check the guess
    global number#make the number global
    print(guess)#print the guess
    if guess == number:#if the guess is correct then you got the answer
         print(f"Congratulations! You guessed the number in {attempts} tries.")
    else:
         if guess > number:#is the guess is too large print too high
           print("Too high! Try again.")
         else:#else print too low
           print("Too low! Try again.")


print("Welcome to the Guessing Game!")#welcome to the guessing game
print("I'm thinking of a number between 1 and 10...")#rules
number = random.randint(1, 10)#set a boundry for the random numbers
attempts = 0#set a variable
while attempts < 5:#while the attempts is less than 5
    checkGuess(getGuess())#check the guess from the get guess function

    if attempts == 5:
        noAttempts()#if they ran out of attempts tell them


