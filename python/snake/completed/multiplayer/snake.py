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
import sys
import os
import random  # For placing fruits
from snake_game import Game, Snake, Snake_Other, Food, Scoreboard

# Resource locations on disk
jungle_bg = "bg.gif"
apple = "apple.gif"

# add scores path
high_scores_path = "high_scores.txt"

# Initialize helper objects
game = Game(512, 512, delay=0.1)
snake = Snake(game, color="blue", shape="turtle")
snake_2 = Snake_Other(game, color="red", shape="turtle")
food = Food(game, color="red")
scoreboard = Scoreboard(game)

# Counter for tracking the player's score
score = 0
score_2 = 0 

# List of colors and index to track iteration
color_list = ["red", "orange", "yellow", "green", "blue", "violet"]
color_index = 0

# STEP 1: LOAD HIGH SCORE

high_score = None
# Load in high score
with open(high_scores_path) as file:
    for line in file:
        high_score = int(line.strip())

# Make sure something loaded
assert(high_score is not None)

# Functions to set movement direction
def go_left_2():
    if snake_2.get_direction() != "right": 
        snake_2.set_direction("left")

def go_right_2():
    if snake_2.get_direction() != "left": 
        snake_2.set_direction("right")

def go_up_2():
    if snake_2.get_direction() != "down": 
        snake_2.set_direction("up")
    

def go_down_2():
    if snake_2.get_direction() != "up": 
        snake_2.set_direction("down")

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
game.set_control('i', go_up_2)
game.set_control('k', go_down_2)
game.set_control('j', go_left_2)
game.set_control('l', go_right_2)

# Write a You Lose! message

def lose():
    # Check if a new high score was set
    snake.set_direction("stop")
    snake_2.set_direction("stop")
    turtle.color("white")
    turtle.write("You Lose!", align="center", font=("Arial", 16, "normal"))
    # turtle.reset()
    time.sleep(1)


    # STEP 2: REPLACE HIGH SCORE
    if score > high_score or score_2 > high_score:
        turtle.clear()
        turtle.write("New High Score!!", align="center", font=("Arial", 16, "normal"))
        # Write new score to file
        with open(high_scores_path, "w+") as file: # 'w+' enables overwriting
            if score > high_score:
                file.write(str(score))
            if score_2 > high_score:
                file.write(str(score_2))
        
        time.sleep(3)


def reset(turt):
    pass

# Main game loop
while True:
    # Check if player is out of bounds
    if snake.is_oob() or snake_2.is_oob():
        lose()
        break

    if snake.is_oob():
        lose()
        break

    # Check if food was hit
    if snake.head_distance_from(food.turt) < 20:
       
        # Put the food somewhere else
        food.place_random()
       
        # Extend body
        new_segment = snake.make_new_segment(color=color_list[color_index])
        snake.add_new_segment(new_segment)
       
        # Update color index
        color_index = (color_index + 1) % len(color_list)
       
        # Update score counter
        score += 10

        # If score hits a multiple of 50, increase the speed
        if score % 50 == 0:
            game.delay = max(game.delay - 0.015, 0)


     # Check if food was hit
    if snake_2.head_distance_from(food.turt) < 20:
       
        # Put the food somewhere else
        food.place_random()
       
        # Extend body
        new_segment = snake_2.make_new_segment(color=color_list[color_index])
        snake_2.add_new_segment(new_segment)
       
        # Update color index
        color_index = (color_index + 1) % len(color_list)
       
        # Update score counter
        score_2 += 10

        # If score hits a multiple of 50, increase the speed
        if score_2 % 50 == 0:
            game.delay = max(game.delay - 0.015, 0)


    # Move all but first segments in reverse order
    body = snake.get_body()
    body_2 = snake_2.get_body()

    for index in range(len(body) - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    for index in range(len(body_2) - 1, 0, -1):
        x = body_2[index - 1].xcor()
        y = body_2[index - 1].ycor()
        body_2[index].goto(x, y)

    # Move segment 0 to where head is
    if len(body) > 0:
        x, y = snake.get_head_position()
        body[0].goto(x, y)

     # Move segment 0 to where head is
    if len(body_2) > 0:
        x, y = snake_2.get_head_position()
        body_2[0].goto(x, y)

    snake.move()
    snake_2.move()

    # STEP 3: WRITE HIGH SCORE TO SCREEn
    scoreboard.write_score(score, score_2, high_score)

    # Check for head collisions with body segments
    collision_1 = False
    for i in range(len(body)):
        if snake.head_distance_from(body[i]) < 20:
            collision_1 = True

    if collision_1:
        snake.remove_segment()
        body = snake.get_body() 

    collision_2 = False
    for i in range(len(body_2)):
        if snake.head_distance_from(body_2[i]) < 20:
            collision_2 = True

    if collision_2:
        snake_2.remove_segment()
        body2 = snake_2.get_body()
    
   
    collision_3 = False
    for i in range(len(body_2)):
        if snake_2.head_distance_from(body_2[i]) < 20:
            collision_3 = True

    if collision_3:
        snake_2.remove_segment()
        body_2 = snake_2.get_body() 

    collision_4 = False
    for i in range(len(body)):
        if snake_2.head_distance_from(body[i]) < 20:
            collision_4 = True

    if collision_4:
        snake.remove_segment()
        body = snake.get_body()
   
    game.update()
    time.sleep(game.delay)

turtle.done()
