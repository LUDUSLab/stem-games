# Jucimar Jr 2019
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# based on http://christianthompson.com/node/51
# font Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# score sound https://freesound.org/people/Kodack/sounds/258020/

import turtle
import winsound
from random import uniform

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_1.penup()
paddle_1.goto(-350, 0)

# draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_2.penup()
paddle_2.goto(350, 0)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# score
score_1 = 0
score_2 = 0

# head-up display of score
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 40
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -40
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 40
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -40
    else:
        y = -250
    paddle_2.sety(y)


# map key
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with upper wall
    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy = -1 * uniform(0.57, 1.73)

    # collision with bottom wall
    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy = 1 * uniform(0.57, 1.73)

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = -1

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = -1

    # collision with paddle 1
    if -342 <= ball.xcor() <= -340 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.setx(-340)
        ball.dx = 1 * uniform(0.57, 1.73)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # collision with paddle 2
    if 342 >= ball.xcor() >= 340 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.setx(340)
        ball.dx = -1 * uniform(0.57, 1.73)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
