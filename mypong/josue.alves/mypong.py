# Josué Alves 2021
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# baseado em http://christianthompson.com/node/51
# fonte Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# som pontuação https://freesound.org/people/Kodack/sounds/258020/

import turtle
import winsound
import random

aux = [-1, 1]

# sound path
bounce = 'C:/Users/Josué/Documents/STEM/stem-games/mypong/assets/bounce.wav'
bleep = 'C:/Users/Josué/Documents/STEM/stem-games/mypong/assets/258020__kodack__arcade-bleep-sound.wav'

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw racquet 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# draw racquet 2
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
ball.dx = 0.4
ball.dy = 0.4

# score
score_1 = 0
score_2 = 0

# score display
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
        y -= 30
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 5
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y -= 5
    else:
        y = -250
    paddle_2.sety(y)


# mapping keys
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
        winsound.PlaySound(bounce, winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # collision with bottom wall
    if ball.ycor() < -280:
        winsound.PlaySound(bounce, winsound.SND_ASYNC)
        ball.sety(-280)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound(bleep, winsound.SND_ASYNC)
        ball.clear()
        ball.goto(0, 0)
        ball.dx *= random.choice(aux)
        ball.dy *= random.choice(aux)

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound(bleep, winsound.SND_ASYNC)
        ball.clear()
        ball.goto(0, 0)
        ball.dx *= random.choice(aux)
        ball.dy *= random.choice(aux)

    # collision with racquet 1
    if (-330 > ball.xcor() > -340) \
            and (ball.ycor() < paddle_1.ycor() + 50) \
            and (ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        ball.dy *= random.choice(aux)
        winsound.PlaySound(bounce, winsound.SND_ASYNC)

    # collision with racquet 2
    if (330 < ball.xcor() < 340) \
            and (ball.ycor() < paddle_2.ycor() + 50) \
            and (ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        ball.dy *= random.choice(aux)
        winsound.PlaySound(bounce, winsound.SND_ASYNC)

# AI player
    if paddle_2.ycor() < ball.ycor() - 60:
        paddle_2_up()
    elif paddle_2.ycor() > ball.ycor() + 60:
        paddle_2_down()
