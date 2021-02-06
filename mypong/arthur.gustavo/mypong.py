# Jucimar Jr 2019
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# based on http://christianthompson.com/node/51
# font Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# score sound https://freesound.org/people/Kodack/sounds/258020/

import turtle
import winsound
from random import uniform


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


def artificial_intelligence():
    if ball.dx > 0:
        if 250 > ball.ycor() > -250:
            if (ball.dy < 0 and ball.ycor() > paddle_2.ycor()) or (ball.dy > 0 and ball.ycor() > paddle_2.ycor()):
                paddle_2.sety(paddle_2.ycor() + 1)

            if (ball.dy < 0 and ball.ycor() < paddle_2.ycor()) or (ball.dy > 0 and ball.ycor() < paddle_2.ycor()):
                paddle_2.sety(paddle_2.ycor() - 1)

        if paddle_2.ycor() == 250:
            paddle_2.sety(250)

        if paddle_2.ycor() == -250:
            paddle_2.sety(-250)


# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
screen.delay(0)

# map key
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeyrelease(paddle_1_up, "w")
screen.onkeyrelease(paddle_1_down, "s")

# draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.shape("square")
paddle_1.shapesize(5, 0.5)
paddle_1.color("white")
paddle_1.penup()
paddle_1.speed(0)
paddle_1.goto(-350, 0)

# draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.shape("square")
paddle_2.shapesize(5, 0.5)
paddle_2.color("white")
paddle_2.penup()
paddle_2.speed(0)
paddle_2.goto(350, 0)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball.dy = 1

# score
score_1 = score_2 = 0

# head-up display of score
hud = turtle.Turtle()
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.speed(0)
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# sounds
bounce = 'C:/Users/arthu/Documents/STEM/stem-games/mypong/assets/bounce.wav'
score = 'C:/Users/arthu/Documents/STEM/stem-games/mypong/assets/258020__kodack__arcade-bleep-sound.wav'

while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    artificial_intelligence()

    # collision with upper wall
    if ball.ycor() > 290:
        winsound.PlaySound(bounce, winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy = -1 * uniform(0.57, 1.73)

    # collision with bottom wall
    if ball.ycor() < -290:
        winsound.PlaySound(bounce, winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy = 1 * uniform(0.57, 1.73)

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound(score, winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = 1

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound(score, winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = -1

    # collision with paddle 1
    if -342 <= ball.xcor() <= -340 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.setx(-340)
        ball.dx = 1 * uniform(0.57, 1.73)
        winsound.PlaySound(bounce, winsound.SND_ASYNC)

    # collision with paddle 2
    if 344 >= ball.xcor() >= 340 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.setx(340)
        ball.dx = -1 * uniform(0.57, 1.73)
        winsound.PlaySound(bounce, winsound.SND_ASYNC)
