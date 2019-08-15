import turtle                    # import turtle library  

window = turtle.Screen()      # create graphics window
window.bgcolor("light blue")        # set background color

pen = turtle.Turtle()         # create new Turtle object
pen.shape("turtle")           # give the object a turtle shape

x = -150                     # define x coordinate
y = -150                     # define y coordinate
move_forward = 300           # define how far you want your turtle to move
size = 40                    # define pen size

for i in range(0,4):

    pen.penup() 
    pen.pensize(size)                                        # pick up pen
    pen.goto(x, y)                                           # move pen to the right position
    pen.pendown()
    pen.pencolor("yellow")
    pen.fillcolor("violet")
    pen.begin_fill()                                         # put pen down

    for i in range(0,4):
        pen.forward(move_forward)                            # move forward
        pen.left(90)                                         # rotate 90 degrees to the left

    pen.end_fill()

    x = int(x - (x/2))                                      # divide x by 2, make sure it's an integer
    y = int(y - (y/2))                                      # divide y by 2, make sure it's an integer   
    move_forward = int(move_forward - (move_forward/2))     # divide move_forward by 2, make sure it's an integer
    size = size - 10                                        # shrink size of pen


turtle.done()                                               # keep window up until programmer exits