import guessing_game
import hangman_game

print("*********************************************")
print("****************** Jojinhos *****************")
print("*********************************************")

print("Select a game: ")
print("(1) Guessing Game (2) Hangman ")
game = int(input("Select a game: "))

if game == 1:
    print("Starting Guessing Game...")
    guessing_game.play()
elif game == 2:
    print("Starting Hangman...")
    hangman_game.play()


# Modularity is the ability to break a program into smaller pieces that are easier to understand and maintain.