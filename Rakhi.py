import turtle
import random


# turtle screen
root = turtle.Screen()
# title of window
turtle.title("Happy Raksha Bandhan!!")
# bg picture
root.bgpic("rakhi (1).png")
root.setup(width=800,height=600)
#root.bgcolor("dark green")
root.tracer(0)
t1 = turtle.Turtle()    # creating a pen
t1.hideturtle()

pen_color = ["pink","blue","red","white","purple","yellow"]
fill_color = ["white","red","pink","purple","yellow","blue"]

t1.speed(0)    # speed of the writing pen

def make_stars():
    for i in range(15):
        p,q = random.randrange(-450, 450), random.randrange(-300, 350)
        t2 = turtle.Turtle()   # new pen
        t2.color(random.choice(pen_color))    # it will choose some random color for the pen
        t2.write("Happy Raksha Bandhan", font=("chiller", 80, "bold italic"), align="center")
        t2.clear()    # it will clear out the t2 pen

        t1.penup()
        t1.goto(p,q)
        t1.pendown()
        t1.begin_fill()
        t1.color(random.choice(pen_color))

        for i in range(6):
            t1.forward(30)
            t1.right(144)

        t1.end_fill()

while True:
    make_stars()
    t1.clear()

turtle.mainloop()