#Allef O. Ramos 2020
# pong in turtle python https://docs.python.org/3.3/library/turtle.html
# based on http://christianthompson.com/node/51
# font Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# punctuation sound https://freesound.org/people/Kodack/sounds/258020/

import turtle
import winsound
from random import choice

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw paddle A
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-360, 0)

# draw paddle B
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# draw Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# Score
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
hud.write("0   0", align="center", font=("Press Start 2P", 24, "normal"))

# divider
divider = turtle.Turtle()
divider.speed(0)
divider.color('white')
divider.hideturtle()
divider.penup()
divider.goto(0, 260)

for i in range(13):
    divider.dy = -50
    divider.write('|', align='center', font=("Press Start 2P", 20, "normal"))
    divider.sety(divider.ycor() + divider.dy)


def up_paddle_1():
    if paddle_1.ycor() < 220:
        y = paddle_1.ycor()
        y = y + 20
        paddle_1.sety(y)


def down_paddle_1():
    if paddle_1.ycor() > -210:
        y = paddle_1.ycor()
        y -= 20
        paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 220:
        y += 20
    else:
        y = 220
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -220:
        y += -20
    else:
        y = -220
    paddle_2.sety(y)


# mapping keyboard
screen.listen()
screen.onkeypress(up_paddle_1, "w")
screen.onkeypress(down_paddle_1, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # hit the top wall
    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= choice([-0.9, -1])

    # hit the bottom wall
    if ball.ycor() < -280:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.sety(-280)
        ball.dy *= choice([-0.9, -1])

    # hit the left wall
    if ball.xcor() < -390:
        score_2 = score_2 + 1
        hud.clear()
        hud.write("{}   {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("arcade-bleep-sound.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1

    # hit the right wall
    if ball.xcor() > 390:
        hud.clear()
        score_1 += 1
        winsound.PlaySound("arcade-bleep-sound.wav", winsound.SND_ASYNC)
        hud.write("{}   {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # hit the paddle A
    if -331 > ball.xcor() < -330 and (paddle_1.ycor() - 50) < ball.ycor() < (paddle_1.ycor() + 50):
        ball.setx(-330)
        ball.dx *= choice([-0.9, -1, -1.05])
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # hit the paddle B
    if 331 < ball.xcor() > 330 and (paddle_2.ycor() - 50) < ball.ycor() < (paddle_2.ycor() + 50):
        ball.setx(330)
        ball.dx *= choice([-0.9, -1, -1.05])
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if score_1 == 10:
        ball.clear()
        hud.goto(0, 0)
        hud.write('PLAYER I WON!!!', align='center', font=("Press Start 2P", 30, "normal"))

    if score_2 == 10:
        hud.goto(0, 0)
        ball.clear()
        hud.write('PLAYER II WON!!!', align='center', font=("Press Start 2P", 30, "normal"))
