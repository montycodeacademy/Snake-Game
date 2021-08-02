#DAY 4

import turtle
import time
import random

screen = turtle.Screen()
screen.title("Snake Game Plus")
screen.bgcolor("lightblue")

screen.screensize(600, 600)
#We can use this instead to use ratio of screen
#resolution instead of absolute values
#screen.setup(width = .75, height = 0.75)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

screen.tracer(0)

#Creating the snake head
head = turtle.Turtle()
head.shape("square")
head.speed(0)
head.color("black")
head.setpos(0,0)
head.penup()
head.direction = "stop"

#Create snake food
food = turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("red")
food.shapesize(0.5, 0.5)
food.penup()
food.setpos(0,100)

body_parts = [ ]


#function to move the snake
def move(snake, step):
    if snake.direction == "up":
        ycor = snake.ycor()
        snake.sety(ycor + step)  
    elif snake.direction == "down":
        ycor = snake.ycor()
        snake.sety(ycor - step)
    elif snake.direction == "right":
        xcor = snake.xcor()
        snake.setx(xcor + step)
    elif snake.direction == "left":
        xcor = snake.xcor()
        snake.setx(xcor - step)

#functions to change snake direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

#keyboard binding
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "s")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "d")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "a")
screen.onkey(go_left, "Left")



game_on = True
delay = 0.2
increment_val = 20

while game_on:
    move(head, increment_val)

    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.setpos(x,y)
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("grey")
        new_part.penup()
        body_parts.append(new_part)
   
        
    screen.update()
    time.sleep(delay)
    
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].setpos(x,y)

    for index in range(len(body_parts) - 1 , 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].setpos(x,y)

