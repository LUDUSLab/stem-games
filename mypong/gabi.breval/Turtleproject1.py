

import turtle
import os
import winsound
import random
import time
from random import randrange, uniform

i = 0
j = 0




# desenhar tela
screen = turtle.Screen()
screen.title("Le Pong")
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
ball.dx = -1
ball.dy = 0




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



# menu
'''
def menu():
    global screen
    contador = True


    while True:
        press = turtle.Turtle()
        press.speed(0)
        press.shape("square")
        press.color("white")
        press.penup()
        press.hideturtle()
        press.goto(0, 0)  # x =0 , y=260
        press.write("Le pong", align="center", font=("Courier", 30, "normal"))
        time.sleep(0.5)
        press.clear()


    press.clear()

'''






def move_balls():
    global score_1, score_2, i , j


    screen.update()

    # s = so + dx
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colisão com parede superior
    if ball.ycor() > 290:
        # os.system("afplay bounce.wav&")
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # colisão com parede inferior
    if ball.ycor() < -290:
        # os.system("afplay bounce.wav&")
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.sety(-290)  # ajeitei colocando 290
        ball.dy *= -1

    # colisão com parede esquerda
    # o Player 2 ganha ponto
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        # os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = -1
        ball.dy = 0
        paddle_1.goto(-350, 0)
        paddle_2.goto(350, 0)
        time.sleep(1)


    # colisão com parede direita
    # o jogador 1 ganha ponto
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        # os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.goto(0, 0)
        aux = ball.dx #1
        print(aux)
        ball.dx = aux
        ball.dy = 0
        paddle_1.goto(-350, 0)
        paddle_2.goto(350, 0)
        time.sleep(1)

    '''
        paddle == no 350 e -350
        a largura toda é 400
        entao teroiacmente
        tem ums D = 50 "coordenadas"
        x:
        entre 340 e 350 
        
        10 "coordenadas" de gordura
        
        
        
        y:
        
        1,2,3,4,5,6,7
        numero = len(lista)
        numero = 7
        
        

    '''



    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_2.ycor() + 60 and ball.ycor() > paddle_2.ycor() - 60):
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.setx(340)
        n = ([0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5])
        ball.dx *= -1
        ball.dy = 1
        if i > len(n)-1:
            i=0
        ball.dy *= n[i]
        if i%2==0:
            ball.dy *= -1
        i+=1
        print(i)




    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_1.ycor() + 60 and ball.ycor() > paddle_1.ycor() - 60):
        winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.setx(-340)
        n = ([0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5])
        ball.dx *= -1
        ball.dy = 1
        if j > len(n)-1:
            j=0
        ball.dy *= n[j]
        if i%2==0:
            ball.dy *= -1
        j+=1



    screen.ontimer(move_balls, 1)
    

#menu()
move_balls()
screen.mainloop()









