import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1000,1000)
t.hideturtle()
screen.bgcolor("medium blue")
t.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)
t.color("white")
t.penup()
t.goto(0,75)
t.pendown()
t.write("All About Me", font=("Arial", 65, "bold"), align="center")
t.penup()
t.goto(0,0)
t.pendown()
t.write("By Xavier Stocke", font=("Arial", 24, "bold"), align="center")
t.penup()
t.goto(0,-20)
t.pendown()
t.write("Press 1 to Continue!", font=("Arial",10, "bold"), align="center")
t3.penup()
t3.goto(-325, 0)
t3.pendown()
t2.penup()
t2.goto(10, 0)
t2.pendown()
t4.penup()
t4.goto(325, 0)
t4.pendown()

def screen():

    t.clear()
    t.penup()
    t.goto(0, 300)
    t.pendown()
    t.write("These are my Favorite Foods!", font=("Arial", 50, "bold"), align="center")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    turtle.addshape("pizza.gif")
    t2.shape("pizza.gif")
    turtle.addshape("burger.gif")
    t3.shape("burger.gif")
    turtle.addshape("lomein.gif")
    t4.shape("lomein.gif")

turtle.listen()
turtle.onkey(screen, 1)

turtle.mainloop()