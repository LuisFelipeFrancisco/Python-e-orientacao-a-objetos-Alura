def play():
    print("*********************************************")
    print("**************** Hangman Game ***************")
    print("*********************************************")
    
    secret_word = "banana".upper()
    correct_letters = ["_", "_", "_", "_", "_", "_"]
    
    hanged = False
    guessed = False
    tries = 6
    
    print (correct_letters)
    
    while (not hanged and not guessed):
        
        guess = input("What is your guess? ")
        guess = guess.strip().upper() # Remove whitespace from the beginning and end of the string, and convert to uppercase.
        
        if guess in secret_word:
            index = 0
            for letter in secret_word:
                if letter == guess:
                    correct_letters[index] = letter
                index += 1
        else:
            tries -= 1
            print("You missed! You have {} tries left.".format(tries))
            
        hanged = tries == 0
        guessed = "_" not in correct_letters    
        print(correct_letters)
    
    if guessed:
        print("You guessed it!")
    else:
        print("You got hanged!")
    print("Game over!")


if __name__ == "__main__":
    play()

# Keywords always in lowercase in Python.
# bool is a type that can be either True or False.
# The not operator inverts the value of a boolean.
# Python str type documentation: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# [] its a list, a list of values that can be changed.
# () its a tuple, a list of values that can't be changed.
# {} its a set, a list of values that can't be repeated.
# {:} its a dictionary, a list of values that can't be repeated and can be accessed by a key.
# Python list documentation: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists