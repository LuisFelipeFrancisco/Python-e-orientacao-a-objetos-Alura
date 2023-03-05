def play():
    print("*********************************************")
    print("**************** Hangman Game ***************")
    print("*********************************************")
    
    secret_word = "banana"
    correct_letters = ["_", "_", "_", "_", "_", "_"]
    
    hanged = False
    guessed = False
    
    print (correct_letters)
    
    while (not hanged and not guessed):
        
        guess = input("What is your guess? ")
        guess = guess.strip() # Remove whitespace from the beginning and end of the string.
        
        index = 0
        for letter in secret_word:
            if letter.upper() == guess.upper():
                correct_letters[index] = letter
            index = index + 1
        
        print(correct_letters)

    print("Game over!")


if __name__ == "__main__":
    play()

# Keywords always in lowercase in Python.
# bool is a type that can be either True or False.
# The not operator inverts the value of a boolean.
# Python str type documentation: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str