"""
Snake game in Python Turtle

By K. Ganz (and you!)
https://codingandcommunity.org/

Loosely based off of this tutorial:
https://www.youtube.com/watch?v=rrOqlfMujqQ&ab_channel=ChristianThompson

July 2019
"""

import turtle  # Graphics module
import time # For delay
import random  # For placing fruits
from snake_game import Game, Snake, Food, Scoreboard  # Helpers

# Initialize helper objects
game = Game(600, 600, wn_color='grey', delay=0.05)
snake = Snake(game)
snake.set_direction("stop")
food = Food(game)
scoreboard = Scoreboard(game)

# Counter for tracking the player's score
score = 0

'''
Step 1: Write function to set where the snake will move

Do so with snake.set_direction(dir) where dir is a String and one of:
["up", "down", "left", "right", "stop"]
'''

# TODO write functions to set movement direction
# Replace 'pass' with a call to snake.set_direction
def go_left():
    pass

def go_right():
    pass

def go_up():
    pass

def go_down():
    pass

'''
Step 2: Tell the central game object to call the functions above
        when certain keys are pressed.

e.g. game.set_control('spacebar', jump)
'''
# Map above functions to keyboard input
''' TODO Fill in Step 2 here '''






# Write a You Lose! message. Call this when lose condition is met
def lose():
    snake.set_direction("stop")
    turtle.write("You Lose!", align="center", font=("Arial", 16, "normal"))
    time.sleep(game.delay * 10)

'''
Every time the game updates, the loop below executes. During this step we have
to make sure relevant game mechanics occur.

        Condition | Results
-----------------------------------------------
Player goes       | Lose game
out of bounds     |
-----------------------------------------------
Player hits a     | Add a body segment to snake
fruit             | Add to score
                  | Place fruit somewhere else
-----------------------------------------------
Player hits a     | Lose game 
body segment      | 
-----------------------------------------------
Always            | Update snake's head and
                  |     body positions
                  | Write score to screen
'''

# Main game loop
while True:
    '''Step 3: TODO see if player has gone of out bounds, lose game if so'''


    ''' Step 4: TODO Fill in actions for when food is hit '''
    if snake.head_distance_from(food.turt) < 20:

        print(end='') # Delete this line

        # TODO Put the food somewhere else by getting
        #   and setting a new position in the game window

        # TODO Extend snake body by making a new segment, then
        #   adding it to the snake
        
        # TODO Update score counter
        
    ''' 
        Step 5: TODO update the positions of all the snake body segments (not the head)

        This part is tough! Ask for help if you need it!
    '''
    # body is a list of the snake's segments except for the head
    body = snake.get_body()

    ''' TODO Fill in Step 5 here '''

    

    # Update the snake's head position
    snake.move()


    ''' TODO Step 6: Write score on screen '''

    ''' 
        TODO Step 7: Check for the head colliding with body segments.
        Lose game if collision occurs.
    '''     
    collision = False

    # More code here

    if collision:
        lose()
        break # Exit the loop, ending the game
    
    game.update() # Go to next game tick
    time.sleep(game.delay)

turtle.done()