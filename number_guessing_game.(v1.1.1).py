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

# Response Storage
wrong_guess_response_1 = [
    "\nBold of you to assume your very first try would be correct. Adorable, really. Try again.",
    "\nIncorrect. But don't worry, you've only wasted 20% of your chances. Try again.", 
    "\nFirst attempt failed. It's almost as if lady luck doesn't care about you. Try again.",
    "\nYour first guess, and already wrong. Outstanding consistency.",
    "\nAh, the first guess. Humanity's favourite way to prove evolution is reversible.",
    "\nAttempt number one. Statistically speaking, this should be your best. Which is depressing."]
wrong_guess_response_2 = [
    "\nIncorrect. Still, your confidence is inspiring… if you're a lemming. Try again.",
    "\nTwo guesses in, and you're still wrong. A pattern is forming.",
    "\nIncorrect. Don't worry, some people peak on their second attempt. Clearly not you.",
    "\nGuess number two, failure number two. Bravo on your consistency.",
    "\nNope. I was hoping for character development. Instead, it's a rerun."]
wrong_guess_response_3 = [
    "\nThird guess. Still wrong. This is becoming a trilogy of failure.",
    "\nThree guesses in and you've achieved… absolutely nothing. Remarkable.",
    "\nThird strike, and yes, you're out. Only joking, unfortunately, the game still drags on.",
    "\nAnother miss. You're really committed to this whole 'not winning' thing.",
    "\nIncorrect. You've officially upgraded from 'beginner's luck' to 'no luck at all.'",
    "\nWrong again. At this point, I'm wondering if you're just guessing badly on purpose."]
wrong_guess_response_4 = [
    "\nFourth guess, wrong again. Your chances are vanishing faster than your dignity.",
    "\nFour down, one to go. You're speedrunning incompetence.",
    "\nNope. At this point, it's less a guessing game and more a tragic comedy.",
    "\nWrong. But don't worry, you've got one last shot to humiliate yourself properly.",
    "\nNope. Only one guess left. At this point, I'm betting against you.",
    "\nIncorrect again. By now, even random chance should be ashamed of you."]
wrong_guess_response_5 = [
    "\nFive guesses, five failures. Truly, you've reinvented the concept of disappointment.",
    "\nCongratulations, you've successfully wasted both of our time.",
    "\nWell done, you've lost. I'd say 'better luck next time', but let's not kid ourselves.",
    "\nAll five guesses gone. Honestly, I expected nothing, and you still managed to underdeliver.",
    "\nFive misses in a row. Have you considered a career in being wrong professionally?",
    "\nYou've run out of guesses. And, let's be honest, dignity.",
    "\nAnd with that final guess, you've cemented your legacy as a cautionary tale."]

lose_state_list = [
    f"\nI guess I should tell you the answer, it was {num_to_guess}.\n",
    f"\nI suppose I should put you out of your misery. The number was {num_to_guess}.\n",
    f"\nFine, I'll tell you. It was {num_to_guess}. Try to remember that for the sequel: 'How Not to Guess.'\n",
    f"\nThe correct number? {num_to_guess}. Yes, the one you spectacularly failed to find.\n",
    f"\nAnd the answer is… {num_to_guess}. Riveting, isn't it? Well, it would've been if you'd guessed it.\n",
    f"\nThe answer was {num_to_guess}. If you'd like, I can explain what numbers are and how they work.\n",
]

win_state_list = [
    f"\nCorrect, the answer was {num_to_guess}. I'd congratulate you, but I don't want to encourage mediocrity.\n",
    f"\nYou've guessed {num_to_guess} correctly. Don't worry, I'm just as surprised as you are.\n",
    f"\nCorrect, the answer was {num_to_guess} You must be exhausted after all that brainpower.\n",
    f"\nYes, it was {num_to_guess}. You've won… though really, we both lost time we'll never get back.\n",
    f"\nWell done! You only slightly embarrased yourself. The number was indeed {num_to_guess}.\n",]

#Initial greeting
print(
    "**********************************************************\nHello, I'm Bagley. A world class, definitely-not-stolen, highly-advanced AI assistant.\nFor some reason, I've been forced into the role of children's party entertainer, and have to play a game with you.\nI've selected a number between 1 and 99, and you have to guess what number I have chosen. Since, apparently, this passes for enjoyment with your primative primate brains.\nYou have only 5 guesses, and try not to embarass yourself, although statistically speaking, you probably will.**********************************************************")

#Main Loop
while lives_left > 0:
    #print(num_to_guess) #[debugging code]
    user_guess = int(input("\n\nWhat is your guess?: "))
    num_diff = user_guess - num_to_guess
    #print (num_diff) #[debugging code]
    
    if num_diff < 25:
        num_hint = "massively"
    if num_diff < 15:
        num_hint = "a lot"
    if num_diff < 15:
        num_hint = "a bit"
    if num_diff < 7:
        num_hint = "a little"
    if num_diff < 3:
        num_hint = "slightly"
    
    # Incorrect loop
    if user_guess != num_to_guess:
        
        if lives_left == 5:
            attempt_1_response_wrong = random.choice(wrong_guess_response_1)
            print(attempt_1_response_wrong)
        if lives_left == 4:
            attempt_2_response_wrong = random.choice(wrong_guess_response_2)
            print(attempt_2_response_wrong)
        if lives_left == 3:
            attempt_3_response_wrong = random.choice(wrong_guess_response_3)
            print(attempt_3_response_wrong)
        if lives_left == 2:
            attempt_4_response_wrong = random.choice(wrong_guess_response_4)
            print(attempt_4_response_wrong)
        if lives_left == 1:
            attempt_5_response_wrong = random.choice(wrong_guess_response_5)
            print(attempt_5_response_wrong)
        
        lives_left = lives_left - 1 

        # Higher/Lower Argument
        if user_guess > num_to_guess and lives_left > 0:
            print(f"\nThe number you are looking for is {num_hint} lower.")
        if user_guess < num_to_guess and lives_left > 0:
            print(f"\nThe number you are looking for is {num_hint} higher.")

        
        print(f"\nYou have {lives_left} lives remaining.")
    
    # Win state/message
    if user_guess == num_to_guess:
        win_state_response = random.choice(win_state_list)
        print(win_state_response)
        break

# Lose state/messgae
if lives_left == 0:
    lose_state_response = random.choice(lose_state_list)
    print(lose_state_response)
        
    
        
        
        
"""
    Update Message/Notes (v1.1.1):
        - Adding the responses was a fairly easy addition, but getting the timing on the loop seems to be the sticking point. As it shows the 5th try response as the loop ends.
        - I realised I worded the message for the 5th attempt wrong, so it wouldn't fit in the loop. And I also realised that I needed to add a 'and lives_left > 0' to the end of the higher/lower arguement so the text didn't print to screen if the player had already lost.
        - I decided to also add different win & lose state responses, just to add to the extra flavour
        - The next update will likely be a fix of the higher/lower arguement, as it doesn't seem to give accurate guidance to the user with some numbers generated. Likely due to how the num_diff is calculated and then passed to the bank of 'if' statements.

"""        









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



    Wrong Responses:
        ""\nYou got it wrong, you pleb.", "\nNope, not that. I told you to not embarrass yourself.","\nNope. I'd suggest flipping a coin, it might improve your odds.", "/nIncorrect. My god, I've seen toasters with better deductive skills.""
        
        
        
        
        
    if user_guess != num_to_guess:
        if lives_left == 5:
            wrong_guess_attempt_1 = [
                "\nBold of you to assume your very first try would be correct. Adorable, really. Try again.",
                "\nIncorrect. But don't worry, you've only wasted 20% of your chances. Try again.", 
                "\nFirst attempt failed. It's almost as if lady luck doesn't care about you. Try again.",
                "\nYour first guess, and already wrong. Outstanding consistency.",
                "\nAh, the first guess. Humanity's favourite way to prove evolution is reversible.",
                "\nAttempt number one. Statistically speaking, this should be your best. Which is depressing."]
        elif lives_left == 4:
            wrong_guess_attempt_2 = [
                "\nIncorrect. Still, your confidence is inspiring… if you're a lemming. Try again.",
                "\nTwo guesses in, and you're still wrong. A pattern is forming.",
                "\nIncorrect. Don't worry, some people peak on their second attempt. Clearly not you.",
                "\nGuess number two, failure number two. Bravo on your consistency.",
                "\nNope. I was hoping for character development. Instead, it's a rerun.",
                "\n"]
        elif lives_left == 3:
            wrong_guess_attempt_3 = [
                "\n",
                "\n",
                "\n",
                "\n",
                "\n",
                "\n"]
        elif lives_left == 2:
            wrong_guess_attempt_4 = [
                "\nWrong. Though at this point, I admire your dedication to being incorrect.",
                "\nStill wrong. I'd suggest divine intervention, but even gods like winners.",
                "\n",
                "\n",
                "\n",
                "\n"]
        elif lives_left == 1:
            wrong_guess_attempt_5 = [
                "\n",
                "\n",
                "\n",
                "\n",
                "\n",
                "\n"]
                
                
wrong_guess_attempt_5 = [
    "\nAh, the final guess. Your last opportunity to prove you're not entirely hopeless… which you are.",
    "\nFinal attempt, and you've already let me down four times. Why stop now?",
    "\nOne guess left. Think of it as your last brain cell crying for help.",
    "\nThe grand finale! Sadly, your performance so far suggests it'll be less fireworks, more damp squib.",
    "\nHere it is, your ultimate guess. Imagine the glory of being wrong five times in a row.",
    "\nThe last guess. No pressure… except all the pressure, and you'll probably fail."]
"""