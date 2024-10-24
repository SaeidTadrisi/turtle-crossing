import time
from turtle import Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.exitonclick()
