# Jucimar Jr 2019
# Version by Matheus Nielsen 2021
# pong using turtle python https://docs.python.org/3.3/library/turtle.html
# based on http://christianthompson.com/node/51
# font Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# score sound effect https://freesound.org/people/Kodack/sounds/258020/
import turtle
import winsound
from threading import Thread

# render background
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# render paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# render paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# render ball
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

# score's heads up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def sound():
    winsound.PlaySound('bounce.wav', winsound.SND_ALIAS)





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


def terminate(self):
    self._running = False


# key mapping
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    sound = Thread(target=sound)
    screen.update()


    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # upper wall collision

    if ball.ycor() > 290:
        sound.start()
        ball.sety(290)
        ball.dy *= -1
    
    # lower wall collision
    if ball.ycor() < -280:
        #winsound.PlaySound('bounce.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        ball.sety(-280)
        ball.dy *= -1

    # left wall collision
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        #winsound.PlaySound('258020__kodack__arcade-bleep-sound.wav', winsound.SND_ALIAS)
        ball.goto(0, 0)
        ball.dx *= -1
    
    # right wall collision
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        #winsound.PlaySound('258020__kodack__arcade-bleep-sound.wav', winsound.SND_ALIAS)
        ball.goto(0, 0)
        ball.dx *= -1

    # paddle 1 collision
    if ball.xcor() < -330 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1     
        #winsound.PlaySound('bounce.wav', winsound.SND_ALIAS)
    
    # paddle 2 collision
    if ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        #winsound.PlaySound('bounce.wav', winsound.SND_ALIAS)