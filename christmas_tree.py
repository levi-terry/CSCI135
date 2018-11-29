import turtle

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
tree.color("green", "green")
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
tree.color("brown", "brown")
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

wn.exitonclick()
