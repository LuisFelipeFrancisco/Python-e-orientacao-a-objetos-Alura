import random

def show_welcome_message():
    print("*********************************************")
    print("**************** Hangman Game ***************")
    print("*********************************************")

def load_secret_word():
    words = []
    
    with open("words.txt", "r") as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

def load_correct_letters(secret_word):
    correct_letters = ["_" for letter in secret_word]
    return correct_letters

def ask_guess():
    guess = input("What is your guess? ")
    guess = guess.strip().upper() # Remove whitespace from the beginning and end of the string, and convert to uppercase.
    return guess

def set_correct_letters(guess, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if letter == guess:
            correct_letters[index] = letter
        index += 1

def winner_message():
    print("You guessed it!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("Congratulations! You won!")

def loser_message(secret_word):
    print("You got hanged!")
    print("The secret word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def draw_hangman(tries):
    print("  _______     ")
    print(" |/      |    ")
    
    if tries == 6:
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    
    if tries == 5:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    
    if tries == 4:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    
    if tries == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    
    if tries == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    
    if tries == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    
    if tries == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    
    print(" |            ")
    print("_|___         ")
    print()

def play():
    
    show_welcome_message()
    secret_word = load_secret_word()
    correct_letters = load_correct_letters(secret_word)
    print (correct_letters)
    
    hanged = False
    guessed = False
    tries = 6

    while (not hanged and not guessed):
        
        guess = ask_guess()
                
        if guess in secret_word:
            set_correct_letters(guess, correct_letters, secret_word)
        else:
            tries -= 1
            draw_hangman(tries)
            print("You missed! You have {} tries left.".format(tries))
            
        hanged = tries == 0
        guessed = "_" not in correct_letters    
        print(correct_letters)
    
    if guessed:
        winner_message()
    else:
        loser_message(secret_word)
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
# List comprehension. It's a way to create a list in a single line of code.