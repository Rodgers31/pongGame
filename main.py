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

    #  Detect collision with wall
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        # need to bounce
        game_ball.bounce_y()
    # Detect collision with r_paddle
    if (game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320
            or game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320):
        game_ball.bounce_x()
    # Detect R paddle miss of all
    if game_ball.xcor() > 380:
        game_ball.reset_position()

    # Detect L paddle miss of all
    if game_ball.xcor() < -380:
        game_ball.reset_position()


screen.exitonclick()
