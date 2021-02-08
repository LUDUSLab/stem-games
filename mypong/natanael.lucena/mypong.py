# Jucimar Jr 2019
# powered by Natanael Lucena de Medeiros
# pong in turtle python https://docs.python.org/3.3/library/turtle.html
# based on http://christianthompson.com/node/51
# Press Start 2P font https://www.fontspace.com/codeman38/press-start-2p
# score sound https://freesound.org/people/Kodack/sounds/258020/

# (For Windows) import winsound
import functools as ft
import turtle
import simpleaudio as sa
from random import choice

# screen draw
screen = turtle.Screen()
screen.delay(0)
screen.tracer(0)
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# scores
score_1 = 0
score_2 = 0


def general_constructor(a):
    a.speed('fastest')
    a.shape("square")
    a.color("white")
    a.penup()


def paddle_draw(p, aux):
    general_constructor(p)
    p.shapesize(stretch_wid=5, stretch_len=1)
    p.penup()
    p.goto(-350 * aux, 0)


# paddle draw
paddle_1 = turtle.Turtle()
paddle_2 = turtle.Turtle()
paddle_draw(paddle_1, 1)
paddle_draw(paddle_2, -1)

# ball draw
ball = turtle.Turtle()
general_constructor(ball)
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# screen outline
space = turtle.Turtle()
space.color("white")
space.penup()
space.goto(400, 300)
space.pendown()
space.pensize(4)
for i in range(8):
    if i % 2 != 0:
        if i != 3 and i != 7:
            space.fd(600)
        else:
            space.fd(800)
    else:
        space.rt(90)
space.hideturtle()

# score head-up display
hud = turtle.Turtle()
general_constructor(hud)
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# initial menu blink
erasable = turtle.Turtle()
erasable.color("white")
erasable.hideturtle()
erasable.up()
erasable.setposition(0, 0)
ball.hideturtle()

wave_obj1 = sa.WaveObject.from_wave_file("../assets/bounce.wav")
wave_obj2 = sa.WaveObject.from_wave_file("../assets/258020__kodack__arcade-bleep-sound.wav")


def blink_on():
    if not start:
        erasable.write("Press Enter to start", align="center", font=("Press Start 2P", 20, "normal"))
        screen.ontimer(blink_off, 300)
    else:
        erasable.undo()


def blink_off():
    erasable.undo()
    if not start:
        screen.ontimer(blink_on, 450)


screen.ontimer(blink_on, 1)

# key bind to start
start = False


def start_pressed():
    global start
    start = True


turtle.listen()
turtle.onkeypress(start_pressed, "Return")
while not start:
    screen.update()
ball.showturtle()


def paddle_up(n1):
    if n1 == 1:
        p = paddle_1
    else:
        p = paddle_2
    y = p.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    p.sety(y)


def paddle_down(n1):
    if n1 == 1:
        p = paddle_1
    else:
        p = paddle_2
    y = p.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    p.sety(y)


# binding keys
screen.listen()
screen.onkeypress(ft.partial(paddle_up, 1), "w")
screen.onkeypress(ft.partial(paddle_down, 1), "s")

n = choice([2, 1, 1.5, -1, -1.5, -2])


def collision_treatment_x():
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    ball.goto(0, 0)
    # ball random direction
    global n
    n = choice([-1, -1.5, -2, 1, 1.5, 2])
    ball.dx *= -1
    ball.dy = n
    wave_obj2.play()
    # (For windows)winsound.PlaySound("../assets/258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)


def collision_treatment_y():
    if ball.ycor() < -280:
        ball.sety(-280)
    if ball.ycor() > 290:
        ball.sety(290)
    ball.dy *= -1
    wave_obj1.play()
    # (For windows)winsound.PlaySound("../assets/bounce.wav", winsound.SND_ASYNC)


def paddle_collision_treatment():
    # paddle random collision
    global n
    n = choice([-1, -1.5, -2, 1, 1.5, 2])
    ball.dx *= -1
    ball.dy = n
    wave_obj1.play()
    # (For windows)winsound.PlaySound("../assets/bounce.wav", winsound.SND_ASYNC)


# IA movement
def ia_move():
    if ball.dx > 0:
        if 250 > ball.ycor() > -250:
            if paddle_2.ycor() < ball.ycor():
                paddle_2.sety(paddle_2.ycor() + 1.7)
            if paddle_2.ycor() > ball.ycor():
                paddle_2.sety(paddle_2.ycor() - 1.7)
        if paddle_2.ycor() == 250:
            paddle_2.sety(250)

        if paddle_2.ycor() == -250:
            paddle_2.sety(-250)
    else:
        if paddle_2.ycor() > 0:
            paddle_2.sety(paddle_2.ycor() - 1.5)
        if paddle_2.ycor() < 0:
            paddle_2.sety(paddle_2.ycor() + 1.5)


def move_ball():
    global score_1, score_2
    screen.update()
    point = False
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # lower and upper walls collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        collision_treatment_y()

    # left wall collision
    if ball.xcor() < -390:
        point = True
        score_2 += 1
        collision_treatment_x()

    # right wall collision
    if ball.xcor() > 390:
        point = True
        score_1 += 1
        collision_treatment_x()

    # paddle collision
    if not point:
        if ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
            ball.setx(330)
            paddle_collision_treatment()
        elif ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
            ball.setx(-330)
            paddle_collision_treatment()

    ia_move()
    # draw and movement sync
    screen.ontimer(move_ball, 3)


move_ball()

screen.listen()
screen.onkey(exit, "q")
# screen loop for movement dynamic
screen.mainloop()
