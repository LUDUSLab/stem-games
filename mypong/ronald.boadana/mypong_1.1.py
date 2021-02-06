# By Jucimar Jr 2019
# Pong in turtle python https://docs.python.org/3.3/library/turtle.html
# Based on http://christianthompson.com/node/51
# Font: Press Start 2P https://www.fontspace.com/code88man38/press-start-2p
# Score sound https://freesound.org/people/Kodack/sounds/258020/
# Powered by Ronald Boadana

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

# draw the left paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=2)
paddle_1.penup()
paddle_1.goto(-360, 0)

# draw the 'A.I.' paddle
paddle_ai = turtle.Turtle()
paddle_ai.speed(0)
paddle_ai.shape("square")
paddle_ai.color("white")
paddle_ai.shapesize(stretch_wid=5, stretch_len=2)
paddle_ai.penup()
paddle_ai.goto(360, 0)

# draw the ball
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
hud.write("0 x 0", align="center", font=("Press Start 2P", 24, "normal"))
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


# 'A.I.' paddle going up
def paddle_ai_up():
    y = paddle_ai.ycor()
    if y < 250:
        y += 50
    else:
        y = 250
    paddle_ai.sety(y)


# 'A.I.' paddle going down
def paddle_ai_down():
    y = paddle_ai.ycor()
    if y > -250:
        y += -50
    else:
        y = -250
    paddle_ai.sety(y)


# ball randomness
def ale_ball():
    randomness = (random.randrange(-20, 22)) / 20
    return randomness


# mapping the keyboard
screen.listen()
screen.onkeypress(paddle_1_up, 'w')
screen.onkeypress(paddle_1_down, 's')

while True:
    screen.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # any random loss of concentration of 'A.I.'
    if ball.ycor() > paddle_ai.ycor() + 10 and random.randrange(21) == 10:
        paddle_ai_up()
    if ball.ycor() < paddle_ai.ycor() - 10 and random.randrange(21) == 10:
        paddle_ai_down()

    # ball collision with the borders
    # upper
    if ball.ycor() > 290:
        winsound.PlaySound("C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # bottom
    if ball.ycor() < -290:
        winsound.PlaySound("C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    # left
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} x {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/258020__kodack__arcade-bleep"
                           "-sound.wav", winsound.SND_ASYNC)
        # os.system("afplay 258020_Kodak_arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= 1
        ball.dy = ale_ball()  # ball randomness

    # right
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} x {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        winsound.PlaySound("C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/258020__kodack__arcade-bleep"
                           "-sound.wav", winsound.SND_ASYNC)
        # os.system("afplay 258020_kodack_arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= 1
        ball.dy = ale_ball()  # ball randomness

    # ball collision with the left paddle
    if ball.xcor() == -340 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        ball.dy = ale_ball()  # any randomness for ball angle
        winsound.PlaySound("C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/bounce.wav", winsound.SND_ASYNC)
        # os.system("afplay bounce.wav&")

    # ball collision with the right paddle
    if ball.xcor() == 340 and paddle_ai.ycor() + 50 > ball.ycor() > paddle_ai.ycor() - 50:
        ball.dx *= -1
        ball.dy = ale_ball()  # any randomness for ball angle
        winsound.PlaySound("C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/bounce.wav", winsound.SND_ASYNC)
        # os.system("afplay bounce.wav&"
