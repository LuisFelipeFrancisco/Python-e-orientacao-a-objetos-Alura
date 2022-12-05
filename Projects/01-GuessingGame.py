print("*********************************************")
print("*************** Guessing Game ***************")
print("*********************************************")

secret_number = 91
guess_limit = 3
round = 1

for round in range(1, guess_limit + 1):
    print("Round {} of {}".format(round, guess_limit))
    guess = int (input("Guess a number between 1 and 100: "))
    
    if guess < 1 or guess > 100:
        print("You must enter a number between 1 and 100")
        continue

    right_guess = int(guess) == secret_number
    above_guess = int(guess) > secret_number
    below_guess = int(guess) < secret_number

    print ("Your guess is {}".format(guess))

    if right_guess:
        print("You guessed it!")
        break
    else:
        if above_guess:
            print("Too high!")
        elif below_guess:
            print("Too low!")

    guess_limit -= 1

print("Game over!")

# The input function returns a string, so we need to convert it to an integer before we can compare it to the secret number.
# The int function converts a string to an integer.
# Intends are important in Python. 
# The code inside the if statement is indented, and the code outside the if statement is not indented.
# elif is short for else if.
# .format is a method that allows us to insert variables into strings.
# String formatting - https://docs.python.org/3/library/string.html#formatexamples
# The range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# range(start, stop, [step])
# Continue allows us to skip the rest of the code in the current iteration of the loop and continue with the next iteration.