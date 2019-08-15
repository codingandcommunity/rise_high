import turtle                    # import turtle library  

window = turtle.Screen()      # create graphics window
window.bgcolor("blue")        # set background color

pen = turtle.Turtle()         # create new Turtle object
pen.shape("turtle")           # give the object a turtle shape

pen.forward(100)              # move forward 100
pen.left(120)                  # rotate 120 degrees to the left
pen.forward(100)
pen.left(120)
pen.forward(100)

turtle.done()                    # keep window up until programmer exits