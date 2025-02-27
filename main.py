import time
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
# Turns of animation in the screen
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.update()

# We need the while loop to update the screen and display the items
game_is_on = True

while game_is_on:
    # This will delay our while sleep a little between each of the updates
    time.sleep(0.1)
    screen.update()
    game_ball.move()




screen.exitonclick()







