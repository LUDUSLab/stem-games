# Jucimar Jr 2019
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# baseado em http://christianthompson.com/node/51
# fonte Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# som pontuação https://freesound.org/people/Kodack/sounds/258020/

import turtle
import os
import winsound
from random import randrange, uniform
import time

# espera = 0.0000000005

# desenhar tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# desenhar raquete 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.penup()
paddle_1.goto(-350, 0)
paddle_1.shapesize(5, 1)  # tamanho (altura, largura)

# desenhar raquete 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("blue")
paddle_2.penup()
paddle_2.goto(350, 0)
paddle_2.shapesize(5, 1)  # tamanho (altura, largura)

# desenhar bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1
print(ball.dx)
# pontuação
score_1 = 0
score_2 = 0

# head-up display da pontuação
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)  # x =0 , y=260
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

'''
Em um mapa cartografico, o maximo em y é 290 a -290
e o maximo em x é 350 a -350 



'''

# Contador
i = 0


# goto  -  posicao de determinada coisa

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


# mapeando as teclas
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colisão com parede superior
    if ball.ycor() > 290:
        # os.system("afplay bounce.wav&")
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= (-1) * (uniform(0, 1))

    # colisão com parede inferior
    if ball.ycor() < -290:
        # os.system("afplay bounce.wav&")
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.sety(-290)  # ajeitei colocando 290
        ball.dy *= (-1) * (uniform(0, 1))

    # colisão com parede esquerda
    # o Player 2 ganha ponto
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        # os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1 * (uniform(0, 1))

    screen.update()

    # colisão com parede direita
    # o jogador 1 ganha ponto
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        # os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = -1 * (uniform(0, 1))


    '''
    Explicando: 



    '''

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_2.ycor() + 60 and ball.ycor() > paddle_2.ycor() - 60):
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= (-1)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_1.ycor() + 60 and ball.ycor() > paddle_1.ycor() - 60):
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= (-1)

    '''
     time.sleep(max(0, espera))
     espera -= 0.000000000001

    '''






