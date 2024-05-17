
import os
import random
import turtle as t



playerAscore = 0
playerBscore = 0
ball_speed = 9.0
normal_speed = 3.0

window = t.Screen()
window.title("Pong Game")
window.bgpic("Spel loadbild.gif")
window.setup(width=800, height=600)
window.tracer = 0

window.addshape("Spel loadbild.gif")

window.update()
# Skapar vänstra sidan och spelet
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("red")
leftpaddle.shapesize(stretch_wid=6, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Skapar högra sidan av spelet . Den  högra spelaren.
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("red")
rightpaddle.shapesize(stretch_wid=6, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Skapar koden till bollen som ska studsa
ball = t.Turtle()
ball.speed(100)  # hastigheten på bollen
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(5, 5)
ballxdirection = 3.0  # hur många pixlar den ska röra på sig
ballydirection = 3.0

# skapar delen där poängen uppdateras.
pen = t.Turtle()
pen.speed(0)
pen.color("Grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Spelare 1:                   Score                   Spelare 2:", align="center", font=('Arial', 24, 'normal'))


# definerar vänstra blocket, hur den ska röra på sig uppåt
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y+30
    leftpaddle.sety(y)


# definerar vänstrablocket som ska slå ifrån sig bollen, hur den ska röra på sig neråt
def leftpaddledown():
    y = leftpaddle.ycor()
    y = y-30
    leftpaddle.sety(y)


# definerar den högra blocket som ska slå ifrån sig
def rightpaddleup():
    x = rightpaddle.ycor()
    x = x + 30
    rightpaddle.sety(x)


# definerar hur vänstra blocket ska röra på sig neråt
def rightpaddledown():
    x = rightpaddle.ycor()
    x = x - 30
    rightpaddle.sety(x)


# bestämmer vilka tangenter som spelarna ska använda.
window.listen()             # rutan ska lyssna på kommander.
window.onkeypress(leftpaddleup, 'w')  # spelare 1 tangenet som hen ska änvända för att köra upp
window.onkeypress(leftpaddledown, 's')   # #spelare 1 tangenet som hen ska änvända för att köra nerr
window.onkeypress(rightpaddleup, 'i')    # spelare 2 tangenet som hen ska änvända för att köra upp
window.onkeypress(rightpaddledown, 'k')    # #spelare r tangenet som hen ska änvända för att köra ner

def shake_screen():
    shake_amount = 5
    for _ in range(10):
        window.bgpic = "Spel loadbild.gif"
        window.update()
        t.delay(20)
        window.bgpic("nopic")
        window.update()
        t.delay(20)


while True:
    window.update()  # medan allt som händer ska sidan alltid updateras och följa med i varje poäng
    # få bollen röra på sig

    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # setter upp platsen, begränsar höjden och längden på spelet
    # begränsar kanten av spelet alltså sidan (högra sidan av rutan så att spelaren förlorar päng)
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * - 1

    # begränsar vänstra kanten  av spelet alltså sidan så att andra spelaren kan få poäng.
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * - 1

    # Skriver Score på högra sidan ( hur många poäng spelare 1 har fått)
    if ball.xcor() > 370:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * - 1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Spelare 1:{}                   Score                   Spelare 2:{}".format(playerAscore, playerBscore),
                  align="center", font=('Arial', 24, "normal"))
        os.system("afplay wallhit.wav&")



    if (ball.xcor()) < -370:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Spelare:{}            Score Spelare 2:{}".format(playerAscore, playerBscore), align="center",
                  font=('Arial', 24, "normal"))
        os.system(" afplay wallhit.wav&")
        shake_screen()

    # om bollen träffar högra paddeln
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50):
        ball_speed += 9
        ball.setx(340)
        ballxdirection = ballxdirection * (-1)
        os.system("afplay tennis-ball-hit-151257.wav&")


#IFALL BOLLEN TRÄFFAR VÄNSTRA PADDEL

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() >leftpaddle.ycor() - 50):
       ball_speed += 9
       ball.setx(-340)
       ballxdirection = ballxdirection * -1
       os.system("afplay tennis-ball-hit-151257.wav&")


       window.update()