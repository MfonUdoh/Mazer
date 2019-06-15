import os, player

# from player import *

print("Welcome To MAZER")
print("Hello player, you are playing as a photon in a lazer beam, meaning you can only travel straight on until either an edge or wall (X) stops you.")
print("You must light every empty space in the maze to win, use 'w''a''s''d' keys to choose your direction of travel, up, left, down, right and press enter to move.")
print("Hit enter to continue.")
input()



scores = player.player().run_game()
os.system('clear')
totalscore = sum(scores)
print("Congratulations looks like you have illuminated all of the mazes!!!")
print("Your total score is: " + str(totalscore) + " out of 500") # change to vary based on number of levels
