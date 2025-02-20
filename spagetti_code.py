import random

# Start game
def getGuess():
    guess = int(input("Enter your guess: "))
    global attempts
    attempts += 1
    return guess



def checkGuess():
    if guess == number:
         print(f"Congratulations! You guessed the number in {attempts} tries.")
    else:
         if guess > number:
           print("Too high! Try agaiin.")
         else:
           print("Too low! Try again.")






print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10...")
number = random.randint(1, 10)
attempts = 0
while True:
    while(attempts <= 5):
        getGuess()
        print(getGuess)


        checkGuess()


        getGuess()
        print(getGuess)


        checkGuess()


        getGuess()
        print(getGuess)

        checkGuess()


        getGuess()
        print(getGuess)


        getGuess()
        print(getGuess)

        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} tries.")
        else:
            print(f"Sorry, you've used all 5 attempts. The number was {number}.")

