def play():
    print("*********************************************")
    print("**************** Hangman Game ***************")
    print("*********************************************")
    
    secret_word = "banana"
    
    hanged = False
    guessed = False
    
    while (not hanged and not guessed):
        
        guess = input("What is your guess? ")
        guess = guess.strip() # Remove whitespace from the beginning and end of the string.
        
        index = 0
        for letter in secret_word:
            if letter.upper() == guess.upper():
                print("Found the letter {} in position {}".format(letter.upper(), index))
            index = index + 1
        
        print("Playing...")

    print("Game over!")


if __name__ == "__main__":
    play()

# Keywords always in lowercase in Python.
# bool is a type that can be either True or False.
# The not operator inverts the value of a boolean.
# Python str type documentation: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str