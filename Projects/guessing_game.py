import random   # Import the random module

def play():
    print("*********************************************")
    print("*************** Guessing Game ***************")
    print("*********************************************")

    secret_number = random.randrange(1, 101)  # Generate a random number between 1 and 100
    guess_limit = 0
    round = 1
    points = 1000 

    print("Select a difficulty level: ")
    difficulty_level = int(input("(1) Easy (2) Medium (3) Hard: "))

    if difficulty_level == 1:
        guess_limit = 20
    elif difficulty_level == 2:
        guess_limit = 10
    else:
        guess_limit = 3

    for round in range(1, guess_limit + 1):
        print("Round {} of {}".format(round, guess_limit))
        guess = int (input("Guess a number between 1 and 100: "))
        
        if guess < 1 or guess > 100:
            print("You must enter a number between 1 and 100")
            continue

        right_guess = int(guess) == secret_number
        above_guess = int(guess) > secret_number
        below_guess = int(guess) < secret_number

        if right_guess:
            print("You guessed it!")
            print("You scored {} points!".format(points))
            break
        else:
            lost_points = abs(secret_number - guess)
            points = points - lost_points
            if above_guess:
                print("Too high!")
                if round == guess_limit:
                    print("You lost! The secret number was {}".format(secret_number))
                    print("You scored {} points!".format(points))
            elif below_guess:
                print("Too low!")
                if round == guess_limit:
                    print("You lost! The secret number was {}".format(secret_number))
                    print("You scored {} points!".format(points))

    print("Game over!")

if __name__ == "__main__":
    play()

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
# Modules are Python files with a .py extension that contain functions you can include in your application.