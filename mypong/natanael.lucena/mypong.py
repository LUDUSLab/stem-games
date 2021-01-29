# Jucimar Jr 2019
# Adaptado por Natanael Lucena de Medeiros
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# baseado em http://christianthompson.com/node/51
# fonte Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# som pontuação https://freesound.org/people/Kodack/sounds/258020/

import functools
import turtle
import winsound
from random import choice
from pathlib import Path
# import os

# desenhar tela
screen = turtle.Screen()
screen.delay(0)
screen.tracer(0)
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

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

# desenhar raquetes
paddle_1 = turtle.Turtle()
paddle_2 = turtle.Turtle()
paddle_draw(paddle_1, 1)
paddle_draw(paddle_2, -1)

# desenhar bola
ball = turtle.Turtle()
general_constructor(ball)
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# pontuação
score_1 = 0
score_2 = 0

# contorno da tela
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

# head-up display da pontuação
hud = turtle.Turtle()
general_constructor(hud)
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

#Menu inicial piscando
eraseable = turtle.Turtle()
eraseable.color("white")
eraseable.hideturtle()
eraseable.up()
eraseable.setposition(0, 0)
ball.hideturtle()
def blink_on():
    if not start:
        eraseable.write("Press Enter to start", align="center", font=("Press Start 2P", 20, "normal"))
        screen.ontimer(blink_off, 300)
    else:
        eraseable.undo()

def blink_off():
    eraseable.undo()
    if not start:
        screen.ontimer(blink_on, 450)

screen.ontimer(blink_on, 1)

#vincular tecla para iniciar
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

# mapeando as teclas
screen.listen()
screen.onkeypress(functools.partial(paddle_up, 1), "w")
screen.onkeypress(functools.partial(paddle_down, 1), "s")
screen.onkeypress(functools.partial(paddle_up, 2), "Up")
screen.onkeypress(functools.partial(paddle_down, 2), "Down")

#path do arquivo de som
s1path = str(Path().absolute()) + "\\arcade-bleep-sound"
s2path = str(Path().absolute()) + "\\bounce.wav"

def collision_treatment_x():
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    # os.system("afplay arcade-bleep-sound.wav&")
    winsound.PlaySound(s1path, winsound.SND_ASYNC)
    ball.goto(0, 0)
    # aleatoriedade na direção da bola
    n = choice([-1, -1.5, -2, 1, 1.5, 2])
    ball.dx *= -1
    ball.dy = n

def collision_treatment_y():
    winsound.PlaySound(s2path, winsound.SND_ASYNC)
    if ball.ycor() < -280:
        ball.sety(-280)
    if ball.ycor() > 290:
        ball.sety(290)
    ball.dy *= -1

def paddle_collision_treatment():
    ball.dx *= -1
    # os.system("afplay bounce.wav&")
    winsound.PlaySound(s2path, winsound.SND_ASYNC)

def move_ball():
    global score_1, score_2
    screen.update()
    point = False
    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colisão com paredes inferior e superior
    if ball.ycor() > 290 or ball.ycor() < -290:
        collision_treatment_y()

    # colisão com parede esquerda
    if ball.xcor() < -390:
        point = True
        score_2 += 1
        collision_treatment_x()

    # colisão com parede direita
    if ball.xcor() > 390:
        point = True
        score_1 += 1
        collision_treatment_x()

    # colisão com raquetes
    if not point:
        if ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
            ball.setx(330)
            paddle_collision_treatment()
        elif ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
            ball.setx(-330)
            paddle_collision_treatment()

    #sincronização de tempo de desenho e movimento
    screen.ontimer(move_ball, 1)

move_ball()

#loop da tela para dinâmica de movimento
screen.mainloop()