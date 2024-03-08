import os
import turtle as t

playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("pink")
window.setup(width=800, height=600)
window.tracer = 0

# Skapar vänstra sidan och spelet
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("red")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Skapar högra sidan av spelet . Den  högra spelaren .
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("red")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Skapar koden till bollen som ska studsa

ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5, 5)
ballxdirection = 0, 2
ballydirection = 0, 2

# skapar delen där poängen uppdateras.
pen = t.Turtle()
pen.speed(0)
pen.color("Grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

pen.write('score', align='center', font=('Arial', 24, 'normal'))


# definerar vänstra blocket, hur den ska röra på sig.
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 90
    leftpaddle.sevty(y)


# definerar högra blocket som ska slå ifrån sig bollen

def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 90
    leftpaddle.sevty(y)


# definerar den högra blocket som ska slå ifrån sig
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 90
    rightpaddle.sevty(y)


def rightpaddledown():
    y = rightpaddle.ycor()
    y = y - 90
    rightpaddle.sevty(y)


# assign key to play

window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()
# få bollen röra på sig
ball.setx(ball.xcor() + ballxdirection)
ball.sety(ball.ycor() + ballydirection)

# setter upp platsen
if ball.ycor() > 290:
    ball.sety(290)
    ballydirection = ballydirection * -1
if ball.ycor() > 290:
    ball.sety() > -290
    ball.sety(-290)
    ballydirection = ballydirection * -1

if ball.xcor() > 390:
    ball.goto(0, 0)
    ballxdirection = ballxdirection
    playerAscore = playerAscore + 1
    pen.clear()
    pen.write("player A:{}        player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

if (ball.xcore()>340)and(ball.xcor()> 350)and(ball.ycor() < rightpaddle.ycor()+ 40 and ball.ycor() > rightpaddle.ycor() - 40):
    ball.setx(340)
    ball_dx = ball_dx * -1
    os.system("afplay paddle.wav&")



if (ball.xcor() < -340) and (ball.ycor() > -350) and (
    ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
    ball.setx(-340)
    ball_dx = ball_dx * -1
    os.system("afplay paddle.wav&")

window.update()
