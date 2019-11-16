import turtle
import os

window = turtle.Screen()
window.title('Pong by Knyght')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer()


# score

score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4


def paddle_a_up():
    # ycor is in turtle module and
    # returns the y coordinate
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    # ycor is in turtle module and
    # returns the y coordinate
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def quit_game():
    window.bye()


window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')
window.onkeypress(quit_game, 'q')
window.listen()


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=('courier', 24, 'normal'))

# main game loop

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boundary checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * (-1)
        os.system('afplay bounce.wav&')
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * (-1)
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('courier', 24, 'normal'))
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * (-1)
        os.system('afplay bounce.wav&')
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * (-1)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('courier', 24, 'normal'))

    # paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx = ball.dx * (-1)
        os.system('afplay bounce.wav&')

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx = ball.dx * (-1)
        os.system('afplay bounce.wav&')

window.mainloop()
