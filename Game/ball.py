from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move =  10
        self.y_move =  10
        self.time = 0.029
    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor,new_y_cor)

    def bounce_in_y(self):
        self.y_move *= -1
    def bounce_in_x(self):
        self.x_move *= -1
    def reset_position(self):
        self.hideturtle()
        self.time = 0.029
        self.goto(0,0)
        self.showturtle()
        self.x_move *= -1
    def speed_up(self):
        self.time *= 0.99