import turtle
import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', seconds=10)
def flash_message():
    '''
    Things for you to add:
        - More messages
        - Different fonts
        - What else can you think of?
    '''
    screen = turtle.Screen()
    screen.setup(width=400, height=200)
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.color("white")
    pen.goto(-100, 0)
    pen.write("You look nice today!")
    time.sleep(2)
    turtle.bye()

    # https://stackoverflow.com/questions/44249534/re-open-turtle-after-turtle-bye
    turtle.Turtle._screen = None
    turtle.TurtleScreen._RUNNING = True

scheduler.start()