import turtle

wn = turtle.Screen()
wn.title("My new window")
wn.bgcolor("black")
wn.setup(width= 800, height = 600 )
wn.tracer(0)

# Score
score_a= 0
score_b=0

#paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# paddle B
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
dx = 0.2
dy = 0.2

# Pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font= ("Courier", 20, "normal"))


# function
def paddle_a_up():
    y= paddle_a.ycor()
    y+=20
    paddle_a.goto(paddle_a.xcor(), y)

def paddle_a_down():
    y= paddle_a.ycor()
    y-=20
    paddle_a.goto(paddle_a.xcor(), y)

def paddle_b_up():
    y= paddle_b.ycor()
    y+=20
    paddle_b.goto(paddle_b.xcor(), y)

def paddle_b_down():
    y= paddle_b.ycor()
    y-=20
    paddle_b.goto(paddle_b.xcor(), y)


# Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    #border checking
    if ball.ycor()> 290:
        #ball.sety(290)
        dy *= -1

    if ball.ycor()< -290:
        #ball.sety(-290)
        dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font= ("Courier", 20, "normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font= ("Courier", 20, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        dx *=-1
