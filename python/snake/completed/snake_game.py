'''
    Helper classes for use with Snake game with Python
    Turtle.
'''
import turtle
import random

class Game(object):
    '''
        Helper class controlling the game's high-level settings,
        screen, and frame-by-frame updating.
    '''
    def __init__(self, wn_len, wn_height, wn_color="grey", delay=0.1):
        ''' Initialize a game instance '''
        # Set constants
        self.wn_len = wn_len
        self.wn_height = wn_height
        self.delay = delay
        self.wn_color = wn_color
        
        # Set up screen
        self.screen = turtle.Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor(self.wn_color)
        self.screen.setup(width=self.wn_len, height=self.wn_height)
        self.screen.tracer(0)
        self.screen.listen()

    
    def is_oob(self, xcor, ycor):
        ''' Check if coordinates are within window '''
        return abs(xcor) > self.wn_len - 10 or abs(ycor) > self.wn_height - 10
    
    def update(self):
        ''' Simple wrapper for screen.update() '''
        self.screen.update()
    
    def set_control(self, key, func):
        ''' 
            Map keyboard input to a function.

            e.g. set_control('w', move_up)
            When 'w' key is pressed, move_up is called with no parameters
        '''

        # Really just a wrapper for the screen class method
        self.screen.onkeypress(func, key)

class Snake(object):
    ''' 
        Class controlling the Snake character in the game,
        including the head and body segments
    '''

    def __init__(self, game, color="green", shape="square"):
        ''' Initialize a new Snake object '''
        # Connect with game object
        self.game = game

        # Save these for making body segments
        self.color = color
        self.shape = shape
        self.body = list() # Empty list, snake starts as one segment

        # Set up head parameters
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape(shape)
        self.head.color(color)
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"
    
    def get_head_position(self):
        ''' Return 2-tup of snake head's position '''
        return (self.head.xcor(), self.head.ycor())

    def get_direction(self):
        ''' Return snake's head direction '''
        return self.head.direction
    
    def set_direction(self, dir):
        ''' 
            Set snake's head direction WITHOUT checking for 180 degree turns
            validity 
        '''

        if dir not in ["up", "down", "left", "right", "stop"]:
            raise ValueError("Invalid direction given: " + dir)
        else:
            self.head.direction = dir
    
    def move(self):
        ''' Update snake position using current direction '''

        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + 20)
        else:
            pass  # Do nothing, direction is "stop"
    
    def head_distance_from(self, obj):
        ''' Wrapper for turtle method to find distance between elements '''
        return self.head.distance(obj)
    
    def make_new_segment(self):
        ''' Set up and return new turtle object for a body segment '''
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape(self.shape)
        new_seg.color(self.color)
        new_seg.penup()

        return new_seg
    
    def add_new_segment(self, seg):
        ''' Append turtle to body '''
        self.body.append(seg)

    def is_oob(self):
        ''' Pass coordinates to game object, check if out of bounds '''
        x, y = self.head.xcor(), self.head.ycor()
        return self.game.is_oob(x, y)

    def get_body(self):
        ''' Gives access to body segments '''
        return self.body

class Food(object):
    ''' 
        Helper class handling the placement of the food object
        on screen.
    '''
    def __init__(self, game, color="red", shape="circle"):
        # Connect with game object to access window params
        self.game = game

        # Set up turtle objdect
        self.turt = turtle.Turtle()
        self.turt.speed(0)
        self.turt.shape(shape)
        self.turt.color(color)
        self.turt.penup()
        self.turt.goto(100, 100)
        self.turt.direction = "stop"
    
    def place_random(self):
        x = random.randint(-self.game.wn_len / 2, self.game.wn_len / 2)
        y = random.randint(-self.game.wn_height / 2, self.game.wn_height / 2)
        self.turt.goto(x, y)

class Scoreboard(object):
    ''' Wrapper for turtle that writes the score on screen '''

    def __init__(self, game, font="Courier New", fntsize=24, fntstyle="normal"):
        # Connect with game object
        self.game = game
        self.font = font
        self.fntsize = fntsize
        self.fntstyle = fntstyle

        # Set up turtle
        self.pen = turtle.Turtle()
        self.pen.color("white")
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(0, self.game.wn_height / 2 - 40)
    
    def write_score(self, scr):
        ''' Write score on screen. Called every game tick. '''
        self.pen.clear() # Remove previous score
        self.pen.write("Score: {}".format(scr), 
                       align="center", 
                       font=(self.font, self.fntsize, self.fntstyle))