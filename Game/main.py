from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()

scoreboard = Scoreboard()

paddle_right = Paddle(350,0)
paddle_left = Paddle(-350,0)


screen.listen()
screen.onkey(paddle_right.go_up,"w")
screen.onkey(paddle_right.go_down,"s")
screen.onkey(paddle_left.go_up,"Up")
screen.onkey(paddle_left.go_down,"Down")

isGame = True
while isGame:
    screen.update()
    ball.move()
    time.sleep(ball.time)

    #Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_in_y()
    #Detect Collision with paddles
    if (ball.distance(paddle_right) < 50 and paddle_right.xcor() > 330) or (ball.distance(paddle_left) < 50 and paddle_left.xcor() < -330):
        ball.bounce_in_x()
        ball.speed_up()
    #Detect Right Paddle when misses
    if ball.xcor() > 400 :
        ball.reset_position()
        scoreboard.add_score_to_left()
    #Detect Left Paddle when misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.add_score_to_right()
    scoreboard.update_score()

screen.exitonclick()