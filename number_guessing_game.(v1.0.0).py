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
# Version: v1.0.0
# Builder: mycode.exe
#
#   Potential Components:
#   [ ] - Use 'random' module to generate random number
#   [ ] - Give user limited lives/tries until game over
#   [ ] - Give hints depending how far the generated number is from the user's guesses
#   [ ] - Use 'while' loop to keep program running until lives are used up or number is guessed
#   [ ] - 
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
#num_to_guess = 29 [debugging code]
lives_left = 5
user_guess = 0

while lives_left > 0 and user_guess != num_to_guess:
    #print(num_to_guess) [debugging comment]
    user_guess = int(input("What is your guess?: "))
    if user_guess == num_to_guess:
        print(f"Well done! The number was indeed {num_to_guess}.")
        break
    if user_guess != num_to_guess:
        print("You were incorrect! Try again.")
        lives_left = lives_left - 1
        print(f"You have {lives_left} lives remaining.")
    if lives_left == 0:
        print(f"The answer was {num_to_guess}.")