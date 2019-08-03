"""
Snake game in Python Turtle

By K. Ganz
https://codingandcommunity.org/

Loosely based off of this tutorial:
 https://www.youtube.com/watch?v=rrOqlfMujqQ&ab_channel=ChristianThompson

July 2019
"""

import turtle  # Graphics module
import time # For delay
import random  # For placing fruits
from snake_game import Game, Snake, Food, Scoreboard

# Initialize helper objects
game = Game(600, 600, wn_color='black', delay=0.1)
snake = Snake(game, color="white")
food = Food(game, color="white")
scoreboard = Scoreboard(game)

# Counter for tracking the player's score
score = 0


# Functions to set movement direction
def go_left():
    if snake.get_direction() != "right": 
        snake.set_direction("left")

def go_right():
    if snake.get_direction() != "left": 
        snake.set_direction("right")

def go_up():
    if snake.get_direction() != "down": 
        snake.set_direction("up")

def go_down():
    if snake.get_direction() != "up": 
        snake.set_direction("down")

# Map above functions to keyboard input
game.set_control('w', go_up)
game.set_control('s', go_down)
game.set_control('a', go_left)
game.set_control('d', go_right)

# Write a You Lose! message
def lose():
    snake.set_direction("stop")
    turtle.color("white")
    turtle.write("You Lose!", align="center", font=("Arial", 16, "normal"))
    time.sleep(game.delay * 10)


# Main game loop
while True:
    # Check if player is out of boundss
    if snake.is_oob():
        lose()
        break

    # Check if food was hit
    if snake.head_distance_from(food.turt) < 20:
        # Put the food somewhere else
        food.place_random()
        # Extend body
        new_segment = snake.make_new_segment()
        snake.add_new_segment(new_segment)
        # Update score counter
        score += 10

    # Move all but first segments in reverse order
    body = snake.get_body()

    for index in range(len(body) - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    # Move segment 0 to where head is
    if len(body) > 0:
        x, y = snake.get_head_position()
        body[0].goto(x, y)

    snake.move()
    scoreboard.write_score(score)

    # Check for head collisions with body segments
    if any(snake.head_distance_from(segment) < 20 for segment in body):
        lose()
        break
    
    
    game.update()
    time.sleep(game.delay)
