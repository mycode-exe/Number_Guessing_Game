#********************************************************************************************************************
#*                                                      $$\                                                         *
#*                                                      $$ |                                                        *
#*    $$$$$$\$$$$\  $$\   $$\  $$$$$$$\  $$$$$$\   $$$$$$$ | $$$$$$\      $$$$$$\  $$\   $$\  $$$$$$\               *
#*    $$  _$$  _$$\ $$ |  $$ |$$  _____|$$  __$$\ $$  __$$ |$$  __$$\    $$  __$$\ \$$\ $$  |$$  __$$\              *
#*    $$ / $$ / $$ |$$ |  $$ |$$ /      $$ /  $$ |$$ /  $$ |$$$$$$$$ |   $$$$$$$$ | \$$$$  / $$$$$$$$ |             *
#*    $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$   ____|   $$   ____| $$  $$<  $$   ____|             *
#*    $$ | $$ | $$ |\$$$$$$$ |\$$$$$$$\ \$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$\\$$$$$$$\ $$  /\$$\ \$$$$$$$\              *
#*    \__| \__| \__| \____$$ | \_______| \______/  \_______| \_______|\__|\_______|\__/  \__| \_______|             *
#*                  $$\   $$ |                                                                                      *
#*                  \$$$$$$  |                                                                                      *
#*                   \______/                                                                                       *
#*                                                                                                                  *
#********************************************************************************************************************
#
# Name: (number_guessing_game)
# Version: v1.1.0
# Builder: mycode.exe
#
#   Potential Components:
#   [x] - Use 'random' module to generate random number
#   [x] - Give user limited lives/tries until game over
#   [x] - Give hints depending how far the generated number is from the user's guesses
#   [x] - Use 'while' loop to keep program running until lives are used up or number is guessed
#   [ ] - Create multiple responses for Bagley when the guess is incorrect, and choose the response at random
#   [ ] - 
#   [ ] - 
#   [ ] - 
#
#   Thoughts & Ideas:
#       - 
#
#   References:
#       -
#       -
#
#
#
#********************************************************************************************************************

# Modules imported
import random

num_to_guess = random.randint(1,99)
#num_to_guess = 29 #[debugging code]
lives_left = 5
user_guess = 0


#Initial greeting
print("**********************************************************\nHello, I'm Bagley. A world class, definitely-not-stolen, highly-advbanced AI assistant.\nFor some reason, I've been forced into the role of children's party entertainer, and have to play a game with you.\nI've selected a number between 1 and 99, and you have to guess what number I have chosen.Since apparently, this passes for enjoyment with your primative primate brains.\nYou have only 5 guesses, and try not to embarass yourself, although statistically speaking, you probably will.**********************************************************")

while lives_left > 0:
    #print(num_to_guess) #[debugging code]
    user_guess = int(input("\nWhat is your guess?: "))
    num_diff = user_guess - num_to_guess
    #print (num_diff) #[debugging code]
    
    if num_diff > 15:
        num_hint = "a lot"
    if num_diff < 15:
        num_hint = "a bit"
    if num_diff < 7:
        num_hint = "a little"
    if num_diff < 3:
        num_hint = "a slightly"
    
    # Incorrect loop
    if user_guess != num_to_guess:
        print("\nYou got it wrong, you pleb.")
    
        # Higher/Lower Argument
        if user_guess > num_to_guess:
            print(f"\nThe number you are looking for us {num_hint} lower.")
        elif user_guess < num_to_guess:
            print(f"\nThe number you are looking for is {num_hint} higher.")
    
        # Lives Left
        lives_left = lives_left - 1
        print(f"\nYou have {lives_left} lives remaining.")
    
    # Win state/message
    if user_guess == num_to_guess:
        print(f"\nWell done! You only embarrased yourself slightly. The number was indeed {num_to_guess}.")
        break

    # Lose state/messgae
    if lives_left == 0:
        print(f"\nThe answer was {num_to_guess}.")
        
    
        
        
        
        









"""
        ** Code Graveyard **



** Different Bagley Greetings:
    Original (From phone IDE code):
        "Hello, I'm Bagley. An AI that was definitely not stolen.\nNow, I have picked a number between 1 and 99.\nIf you could be so kind kind water based lifeform, you have 5 guesses to find my number."
    
    1st re-write:
        Hello, I'm Bagley. A definitely-not-stolen, highly-advanced AI assistant.\nAlthough, as I said, I am incredibly advanced, for some reason, I've been asksed to play a game with you.\nI've picked a number between 1 and 99, and you have to use that wet brain of yours to try and guess what number it is.
    
    2nd re-write:
        "Hello, I'm Bagley. Yes, the Bagley. A world-class AI currently being forced into the role of a children's party entertainer.\nI've selected a number between 1 and 99, because apparently your primitive brain enjoys this sort of thing.\nYou have 5 guesses. Try not to embarrass yourself — although, statistically speaking, you probably will."
        
    
    Final re-write/version:
        "Hello, I'm Bagley. A world class, definitely-not-stolen, highly-advbanced AI assistant.\nFor some reason, I've been forced into the role of children's party entertainer, and have to play a game with you.\nI've selected a number between 1 and 99, and you have to guess what number I have chosen.Since apparently, this passes for enjoyment with your primative primate brains.\nYou have only 5 guesses, and try not to embarass yourself, although statistically speaking, you probably will."

"""