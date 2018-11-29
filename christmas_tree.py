import turtle

wn = turtle.Screen()
tree = turtle.Turtle()
wn.delay(None)
wn.tracer(4, None) # count how many executions there are, divide by biggest number
wn.bgcolor("white")

# Green Tree Part
tree.up()
tree.goto(-500, -350)
tree.down()
tree.color("green", "green")
tree.begin_fill()
for i in range(3):
    tree.forward(1000)
    tree.lt(120)
tree.end_fill()

# Brown Trunk
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

# Need to add bulbs

wn.exitonclick()
