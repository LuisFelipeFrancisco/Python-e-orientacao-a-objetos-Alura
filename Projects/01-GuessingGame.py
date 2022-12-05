print("*********************************************")
print("*************** Guessing Game ***************")
print("*********************************************")

secret_number = 91
guess_limit = 3

while guess_limit > 0:
    print("You have", guess_limit, "guesses left.")
    guess = (input("Guess a number between 1 and 100: "))

    right_guess = int(guess) == secret_number
    above_guess = int(guess) > secret_number
    below_guess = int(guess) < secret_number

    print("You guessed: ", guess)

    if right_guess:
        print("You won!")
        print("Game over!")
    else:
        if above_guess:
            print("You were above the number!")
        elif below_guess:
            print("You were below the number!")

    guess_limit -= 1

# The input function returns a string, so we need to convert it to an integer before we can compare it to the secret number.
# The int function converts a string to an integer.
# Intends are important in Python. 
# The code inside the if statement is indented, and the code outside the if statement is not indented.
# elif is short for else if.
# The while loop will keep running as long as the condition is true.