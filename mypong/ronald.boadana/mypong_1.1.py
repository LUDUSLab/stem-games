# By Jucimar Jr 2019 and adapted by Ronald Boadana
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# Based on http://christianthompson.com/node/51
# Font: Press Start 2P https://www.fontspace.com/code88man38/press-start-2p
# Score sound https://freesound.org/people/Kodack/sounds/258020/
# powered by Ronald Boadana

# import required library
import turtle
import winsound  # for Windows
import random
# import os (only for macOS)

# draw the screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# how to draw the left paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=3, stretch_len=0.5)
paddle_1.penup()
paddle_1.goto(-360, 0)

# how to draw the right paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=3, stretch_len=0.5)
paddle_2.penup()
paddle_2.goto(360, 0)

# how to draw the ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(1, 1)
ball.dx, ball.dy = 0.5, 0.5

# player's score
score_1 = 0
score_2 = 0

# How to show the scoreboard
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))
hud.hideturtle()


# left paddle going up
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 50
    else:
        y = 250
    paddle_1.sety(y)


# left paddle going down
def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -50
    else:
        y = -250
    paddle_1.sety(y)


# right paddle going up
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 50
    else:
        y = 250
    paddle_2.sety(y)


# right paddle going down
def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -50
    else:
        y = -250
    paddle_2.sety(y)


# ball randomness
def ale_ball():
    randomness = (random.randrange(-20, 22)) / 20
    return randomness


# mapping the keyboard
# can move the right paddle with two options
screen.listen()
screen.onkeypress(paddle_1_up, 'w')
screen.onkeypress(paddle_1_down, 's')
screen.onkeypress(paddle_2_up, "8")
screen.onkeypress(paddle_2_up, 'Up')
screen.onkeypress(paddle_2_down, '2')
screen.onkeypress(paddle_2_down, 'Down')

while True:
    screen.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball collision with the borders
    # upper
    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # bottom
    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    # left
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)
        # os.system("afplay 258020__Kodak__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy = ale_ball()  # ball randomness

    # right
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)
        # os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy = ale_ball()  # ball randomness

    # ball collision with the left paddle
    if ball.xcor() == -350 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        ball.dy = ale_ball()  # any randomness for ball angle
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        # os.system("afplay bounce.wav&")

    # ball collision with the right paddle
    if ball.xcor() == 350 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        ball.dy = ale_ball()  # any randomness for ball angle
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        # os.system("afplay bounce.wav&")