


import os
import turtle as t

playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("pink")
window.setup(width=800, height=600)
window.tracer = 0

#Skapar vänstra sidan och spelet
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("red")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

#Skapar högra sidan av spelet . Den  högra spelaren .
rightpaddle =t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("red")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

#Skapar koden till bollen som ska studsa

ball= t.Turtle()
ball.speed(100)   #hastigheten på bollen
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5, 5)
ballxdirection = 3.5  #hur många pixlar den ska röra på sig
ballydirection = 3.5

#skapar delen där poängen uppdateras.
pen=t.Turtle()
pen.speed(0)
pen.color("Grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Spelare 1:                   Score                   Spelare 2:", align="center", font=('Arial', 24, 'normal'))


#definerar vänstra blocket, hur den ska röra på sig.
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+15
    leftpaddle.sety(y)


#definerar högra blocket som ska slå ifrån sig bollen

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-15
    leftpaddle.sety(y)


# definerar den högra blocket som ska slå ifrån sig
def rightpaddleup():
    y=rightpaddle.ycor()
    y = y + 90
    rightpaddle.sety(y)


def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)


# bestämmer vilka tanigenter som spelarna ska använda.
window.listen()  #rutan ska lyssna på kommander
window.onkeypress(leftpaddleup, 'w')  #spelare 1 tangenet som hen ska änvända för att köra upp
window.onkeypress(leftpaddledown, 's') # #spelare 1 tangenet som hen ska änvända för att köra nerr
window.onkeypress(rightpaddleup, 'i')  # #spelare 2 tangenet som hen ska änvända för att köra upp
window.onkeypress(rightpaddledown, 'k') # #spelare r tangenet som hen ska änvända för att köra ner

while True:
    window.update()
# få bollen röra på sig

    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

# setter upp platsen, begränsar höjden och längden på spelet

    # begränsar kanten av spelet alltså sidan (högra sidan av rutan så att spelaren förlorar päng)
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection=ballydirection *-1
        os.system("afplay wallhit.wav&")
 # begränsar vänstra kanten  av spelet alltså sidan så att andra spelaren kan få poäng.
    if ball.ycor() <-290:
        ball.sety(-290)
        ballydirection = ballydirection *-1
        os.system("afplay wallhit.wav&")

    # Skriver Score på högra sidan ( hur många poäng spelare 1 har fått)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection=ballxdirection *-1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Spelare 1:{}                   Score                    Spelare 2:{}".format(playerAscore,playerBscore),align="center",font=('Arial',24,"normal"))
        os.system("afplay wallhit.wav&")

# Skriver score på vänstra sidan ( skriver poäng antal spelare nummer 2 har fått)
    if ball.xcor() <-390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Spelare:{}                 Score                    Spelare 2:{}".format(playerAscore, playerBscore), align="center",
        font=('Arial', 24, "normal"))
        os.system("afplay wallhit.wav&")

    if (ball.xcor()>390)and(ball.xcor()< 350)and(ball.ycor() < rightpaddle.ycor()+ 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(390)
        ballxdirection=ballxdirection*-1
        os.system("afplay paddle.wav&")


    if (ball.xcor()< -390)and (ball.xcor() > -350)and(ball.ycor()< leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-390)
        ballxdirection = ballxdirection* -1
        os.system("afplay paddle.wav&")
