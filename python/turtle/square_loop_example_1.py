import turtle                    # import turtle library  

window = turtle.Screen()      # create graphics window
window.bgcolor("blue")        # set background color

pen = turtle.Turtle()         # create new Turtle object
pen.shape("turtle")           # give the object a turtle shape

for i in range(0,4):
    pen.forward(100)              # move forward 100
    pen.left(90)                  # rotate 90 degrees to the left

turtle.done()                    # keep window up until programmer exits