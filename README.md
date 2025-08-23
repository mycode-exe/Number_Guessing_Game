This project is a simple Python program that challenges the player to guess a randomly generated number. It makes use of Python’s built-in random module to select a number within a given range, and the player must attempt to guess the correct value before running out of lives.

The initial version contains just the basic number guessing script, but the later version(s) provide feedback to let the player know whether their attempt was too high or too low, creating a process of elimination until they succeed or their lives run out.


Update Notes (taken from notes section at bottom of code):
    (v1.1.1);
        - Adding the responses was a fairly easy addition, but getting the timing on the loop seems to be the sticking point. As it shows the 5th try response as the loop ends.
        - I realised I worded the message for the 5th attempt wrong, so it wouldn't fit in the loop. And I also realised that I needed to add a 'and lives_left > 0' to the end of the higher/lower arguement so the text didn't print to screen if the player had already lost.
        - I decided to also add different win & lose state responses, just to add to the extra flavour
        - The next update will likely be a fix of the higher/lower arguement, as it doesn't seem to give accurate guidance to the user with some numbers generated. Likely due to how the num_diff is calculated and then passed to the bank of 'if' statements.