import turtle
import time
import os

i = 0
j = 0

screen = turtle.Screen()
screen.title("Le Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.penup()
paddle_1.goto(-350, 0)
paddle_1.shapesize(5, 1)  # tamanho (altura, largura)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("blue")
paddle_2.penup()
paddle_2.goto(350, 0)
paddle_2.shapesize(5, 1)  # tamanho (altura, largura)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -1
ball.dy = 0

score_1 = 0
score_2 = 0

hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)  # x =0 , y=260
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Game:
    def __init__(self):
        self.state = "splash"  # Menu

    def start(self):
        self.state = "playing"  # the game itself

class CharacterPen:
    def __init__(self, color="white", scale=1.0):
        self.color = color
        self.scale = scale

        self.characters = {"1": ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10)),
                           "2": ((-5, 10), (5, 10), (5, 0), (-5, 0), (-5, -10), (5, -10)),
                           "3": ((-5, 10), (5, 10), (5, 0), (0, 0), (5, 0), (5, -10), (-5, -10)),
                           "4": ((-5, 10), (-5, 0), (5, 0), (2, 0), (2, 5), (2, -10)),
                           "5": ((5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10)),
                           "6": ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0)),
                           "7": ((-5, 10), (5, 10), (0, -10)),
                           "8": ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0)),
                           "9": ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0)),
                           "0": ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10)),
                           "A": ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0)),
                           "B": ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5, 0), (5, -10), (-5, -10)),
                           "C": ((5, 10), (-5, 10), (-5, -10), (5, -10)),
                           "D": ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10)),
                           "E": ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10)),
                           "F": ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10)),
                           "G": ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0)),
                           "H": ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10)),
                           "I": ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10)),
                           "J": ((5, 10), (5, -10), (-5, -10), (-5, 0)),
                           "K": ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10)),
                           "L": ((-5, 10), (-5, -10), (5, -10)), "M": ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10)),
                           "N": ((-5, -10), (-5, 10), (5, -10), (5, 10)),
                           "O": ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10)),
                           "P": ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0)),
                           "Q": ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11)),
                           "R": ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10)),
                           "S": ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8)),
                           "T": ((-5, 10), (5, 10), (0, 10), (0, -10)), "V": ((-5, 10), (0, -10), (5, 10)),
                           "U": ((-5, 10), (-5, -10), (5, -10), (5, 10)),
                           "W": ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10)),
                           "X": ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10)),
                           "Y": ((-5, 10), (0, 0), (5, 10), (0, 0), (0, -10)),
                           "Z": ((-5, 10), (5, 10), (-5, -10), (5, -10)), "-": ((-3, 0), (3, 0))}

    def draw_string(self, caneta, string, x, y):
        caneta.width(2)
        caneta.color(self.color)

        # Center text
        x -= 15 * self.scale * ((len(string) - 1) / 2)
        for character in string:
            self.draw_character(caneta, character, x, y)
            x += 15 * self.scale

    def draw_character(self, caneta, character, x, y):
        scale = self.scale

        if character in "abcdefghijklmnopqrstuvwxyz":
            scale *= 0.8

        character = character.upper()

        # Check if the character is in the dictionary
        if character in self.characters:
            caneta.penup()
            xy = self.characters[character][0]
            caneta.goto(x + xy[0] * scale, y + xy[1] * scale)
            caneta.pendown()
            for k in range(1, len(self.characters[character])):
                xy = self.characters[character][k]
                caneta.goto(x + xy[0] * scale, y + xy[1] * scale)
            caneta.penup()

# Splash Screen
character_pen = CharacterPen("red", 3.0)
character_pen.scale = 1.0
character_pen.draw_string(pen, "PRESS Z TO START", 0, 50)

screen.tracer(0)

class Moviments:

    def paddle_1_up(self):
        y = paddle_1.ycor()
        if y < 250:
            y += 30
        else:
            y = 250
        paddle_1.sety(y)

    def paddle_1_down(self):
        y = paddle_1.ycor()
        if y > -250:
            y += -30
        else:
            y = -250
        paddle_1.sety(y)

    def paddle_2_up(self):
        y = paddle_2.ycor()
        if y < 250:
            y += 30
        else:
            y = 250
        paddle_2.sety(y)

    def paddle_2_down(self):
        y = paddle_2.ycor()
        if y > -250:
            y += -30
        else:
            y = -250
        paddle_2.sety(y)

m = Moviments()  # creating Moviments object
g = Game()  # creating Game object

# Keyboard bindings
screen.listen()
screen.onkeypress(m.paddle_1_up, "w")
screen.onkeypress(m.paddle_1_down, "s")
# screen.onkeypress(m.paddle_2_up, "Up")
# screen.onkeypress(m.paddle_2_down, "Down")
screen.onkeypress(g.start, "z")

while g.state == "splash":
    screen.update()

def move_balls():
    pen.clear()

    global score_1, score_2, i, j

    # IA Player
    if paddle_2.ycor() < ball.ycor() and abs(paddle_2.ycor() - ball.ycor()) > 10:
        m.paddle_2_up()
    elif paddle_2.ycor() > ball.ycor() and abs(paddle_2.ycor() - ball.ycor()) > 10:
        m.paddle_2_down()

    screen.update()

    # s = so + dx
    ball.setx(ball.xcor() + ball.dx)  # pega a coordenada e soma ou decrementa
    ball.sety(ball.ycor() + ball.dy)

    # collision with top wall
    if ball.ycor() > 290:
        # playsound(bounce_sound)
        os.system("aplay bounce.wav")
        # winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # hit the bottom
    if ball.ycor() < -290:
        os.system("aplay bounce.wav")
        # winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.sety(-290)  # ajeitei colocando 290
        ball.dy *= -1

    # hits the left wall
    if ball.xcor() < -390:
        score_2 += 1
        os.system("aplay bons.wav")
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        # winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = -1
        ball.dy = 0
        paddle_1.goto(-350, 0)
        paddle_2.goto(350, 0)
        time.sleep(1)

    # hits the right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        os.system("aplay bons.wav")
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        # winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.goto(0, 0)
        aux = ball.dx
        ball.dx = aux
        ball.dy = 0
        paddle_1.goto(-350, 0)
        paddle_2.goto(350, 0)
        time.sleep(1)

    if (340 < ball.xcor() < 350) and (
            paddle_2.ycor() + 60 > ball.ycor() > paddle_2.ycor() - 60):
        os.system("aplay bounce.wav")
        # winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        ball.setx(340)
        n = ([0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5])
        ball.dx *= -1
        ball.dy = 1
        if i > len(n)-1:
            i = 0
        ball.dy *= n[i]
        if i % 2 == 0:
            ball.dy *= -1
        i += 1

    if (-340 > ball.xcor() > -350) and (
            paddle_1.ycor() + 60 > ball.ycor() > paddle_1.ycor() - 60):
        # winsound.PlaySound("pong_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        os.system("aplay bounce.wav")
        ball.setx(-340)
        n = ([0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5])
        ball.dx *= -1
        ball.dy = 1
        if j > len(n)-1:
            j = 0
        ball.dy *= n[j]
        if i % 2 == 0:
            ball.dy *= -1
        j += 1

    screen.ontimer(move_balls, 1)

move_balls()
screen.mainloop()
