# Jucimar Jr 2019
# Version by Matheus Nielsen 2021
# pong using turtle python https://docs.python.org/3.3/library/turtle.html
# based on http://christianthompson.com/node/51
# Press Start 2P font https://www.fontspace.com/codeman38/press-start-2p
# score sound effect https://freesound.org/people/Kodack/sounds/258020/

import turtle
import winsound
import random

# draw background
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
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
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
ball.dy = 0

# score
score_1 = 0
score_2 = 0

# score's hud
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
        y += 30
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_2.sety(y)


def wall_collision():
    winsound.PlaySound('bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT)
    ball.dy *= -1


def paddle_collision():
    random_position = random.randrange(-7, 8)
    ball.dy = random_position / 10
    ball.dx *= -1
    winsound.PlaySound('bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT)


def scoring():
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    winsound.PlaySound('258020__kodack__arcade-bleep-sound.wav', winsound.SND_FILENAME)
    ball.goto(0, 0)
    ball.dx = -0.5
    ball.dy = 0
    paddle_1.sety(0)
    paddle_2.sety(0)


# key mapping
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

    # upper and lower wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        wall_collision()

    # left wall collision
    if ball.xcor() < -390:
        score_2 += 1
        scoring()
    
    # right wall collision
    if ball.xcor() > 390:
        score_1 += 1
        scoring()

    # paddle 1 collision
    if ball.xcor() == -350 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        paddle_collision()
    
    # paddle 2 collision
    if ball.xcor() == 350 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        paddle_collision()
