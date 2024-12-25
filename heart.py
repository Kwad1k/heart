import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("<3")


t = turtle.Turtle()
t.speed(0)  


def draw_heart():
    t.begin_fill()
    t.fillcolor("red")
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()    

def write_text():
    t.penup()
    t.goto(0, -150)  
    t.color("white")
    t.write("Зай", align="center", font=("Arial", 24, "bold"))

draw_heart()

write_text()

screen.exitonclick()
