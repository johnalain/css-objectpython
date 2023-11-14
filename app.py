# https://www.youtube.com/watch?v=xzuguCSizWw
import turtle

wind = turtle.Screen()
wind.title("ping pong by code")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)

madras1 = turtle.Turtle()
madras1.speed(0)
madras1.shape("square")
madras1.color("blue")
madras1.shapesize(stretch_wid=5,stretch_len=1)
madras1.penup()
madras1.goto(-350,0)

while True:
    wind.update()
    #time 21:24
    

