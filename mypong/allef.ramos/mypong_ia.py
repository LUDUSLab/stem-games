#Jucimar Jr
#Allef edited
# pong in turtle python https://docs.python.org/3.3/library/turtle.html
# based on http://christianthompson.com/node/51
# font Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# punctuation sound https://freesound.org/people/Kodack/sounds/258020/

import turtle
import winsound
from random import choice

# draw screen
screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("My Pong")
screen.bgcolor("black")

# draw paddle A
paddle_1 = turtle.Turtle()
paddle_1.color("white")
paddle_1.shape("square")
paddle_1.speed(0)
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# draw paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# draw Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

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


def up_paddle():
    if paddle_1.ycor() < 210:
        u = paddle_1.ycor()
        u = u + 20
        paddle_1.sety(u)


def down_paddle():
    if paddle_1.ycor() > -210:
        d = paddle_1.ycor()
        d -= 20
        paddle_1.sety(d)


# mapping keyboard
screen.listen()
screen.onkeypress(up_paddle, "w")
screen.onkeypress(down_paddle, "s")

while True:
    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    screen.update()

    # hit the top wall
    if ball.ycor() > 290:
        winsound.PlaySound("../assets/bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # hit the bottom wall
    if ball.ycor() < -280:
        winsound.PlaySound('../assets/bounce.wav', winsound.SND_ASYNC)
        ball.sety(-280)
        ball.dy *= -1

    # hit the left wall
    if ball.xcor() < -390:
        score_2 = score_2 + 1
        hud.clear()
        hud.write("{}   {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("../assets/258020__kodack__arcade-arcade-bleep-sound.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= choice([-0.95, -1, -1.05])

    # hit the right wall
    if ball.xcor() > 390:
        hud.clear()
        score_1 += 1
        winsound.PlaySound("../assets/258020__kodack__arcade-arcade-bleep-sound.wav", winsound.SND_ASYNC)
        hud.write("{}   {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= choice([-0.95, -1, -1.05])

    # hit the paddle A
    if ball.xcor() < -330 and (paddle_1.ycor() - 50) <= ball.ycor() <= (paddle_1.ycor() + 50):
        if (paddle_1.ycor() - 15) <= ball.ycor() <= (paddle_1.ycor() + 15):
            ball.setx(-330)
            ball.dy = choice([0.1, -0.1])
            ball.dx *= -1
            winsound.PlaySound("../assets/bounce.wav", winsound.SND_ASYNC)
        else:
            ball.setx(-330)
            ball.dy = 0.3 * choice([-1.01, 1.01, -0.8, 0.8, -0.9, 0.9])
            ball.dx *= -1
            winsound.PlaySound("../assets/bounce.wav", winsound.SND_ASYNC)

    # hit the paddle B
    if ball.xcor() > 330 and (paddle_b.ycor() - 50) <= ball.ycor() <= (paddle_b.ycor() + 50):
        if (paddle_b.ycor() - 15) <= ball.ycor() <= (paddle_b.ycor() + 15):
            ball.setx(330)
            ball.dy = choice([0.1, -0.1])
            ball.dx *= -1
            winsound.PlaySound("../assets/bounce.wav", winsound.SND_ASYNC)
        else:
            ball.setx(330)
            ball.dy = 0.3 * choice([-1.01, 1.01, -0.8, 0.8, -0.9, 0.9])
            ball.dx *= -1
            winsound.PlaySound("../assets/bounce.wav", winsound.SND_ASYNC)

    # Move paddle 2
    if (paddle_b.ycor() < ball.ycor()) and ((paddle_b.ycor() + 50) < 270):
        y = paddle_b.ycor()
        y += 0.2
        paddle_b.sety(y)

    if (paddle_b.ycor() > ball.ycor()) and ((paddle_b.ycor() - 50) > -270):
        y = paddle_b.ycor()
        y -= 0.2
        paddle_b.sety(y)
