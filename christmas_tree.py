import turtle
import random
wn = turtle.Screen()
tree = turtle.Turtle()
wn.delay(None)
wn.tracer(4, None)  # Use this to draw much faster, save time
wn.bgcolor("blue")
wn.screensize(1200, 1300)

# Green Tree Part
tree.up()
tree.goto(-500, -350)
tree.down()
tree.color("black", "green")
tree.begin_fill()
for i in range(3):
    tree.forward(1000)
    tree.lt(120)
    print(tree.pos())
tree.end_fill()

# Draw Brown Trunk
tree.up()
tree.goto(-100, -350)
tree.down()
tree.color("black", "brown")
tree.begin_fill()
tree.rt(90)
tree.forward(200)
tree.left(90)
tree.forward(200)
tree.left(90)
tree.forward(200)
tree.end_fill()

# Draw Star
tree.up()
tree.goto(0, 455)
tree.down()
tree.color("black", "yellow")
tree.begin_fill()
tree.seth(324)
for i in range(5):
    tree.forward(50)
    tree.rt(252)
    tree.forward(50)
    tree.lt(324)
tree.end_fill()

# Make some random bulbs
colors = ["red", "blue", "yellow", "purple", "orange"]
count = 0
while count <= 20:
    x = 0
    y = 0
    if count < 7:
        x = random.randint(-500, 500)
        y = -340
    elif count < 13:
        x = random.randint(-300, 300)
        y = -100
    elif count < 18:
        x = random.randint(-200, 200)
        y = 150
    else:
        x = random.randint(-100, 100)
        y = 300
    tree.up()
    # Pick random x,y within tree? or iterate?
    # Tree corners = (-500, -350) (500, -350) (0, 516)
    tree.color("black", random.choice(colors))
    tree.goto(x, y)
    tree.down()
    tree.begin_fill()
    tree.circle(40)
    tree.end_fill()
    count += 1

# Write Merry Christmas at top
tree.up()
tree.goto(0, 570)
tree.color("black", "black")
tree.write("Merry Christmas!", True, align="center", font=("Calibri", 30, "bold"))

wn.exitonclick()
