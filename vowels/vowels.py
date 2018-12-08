import turtle


def drawBar(t, height, vowel):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(15)
    t.write(vowel, font=("Calibri", 14))
    t.forward(10)
    t.write(str(height), font=("Calibri", 14))
    t.forward(15)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


vowels = []
a = 0
e = 0
i = 0
o = 0
u = 0
with open("vowels.txt", "r") as file:
    for line in file:
        for character in line:
            if character == "a" or character == "A":
                a += 1
            elif character == "e" or character == "E":
                e += 1
            elif character == "i" or character == "I":
                i += 1
            elif character == "o" or character == "O":
                o += 1
            elif character == "u" or character == "U":
                u += 1

vowels.append(a)
vowels.append(e)
vowels.append(i)
vowels.append(o)
vowels.append(u)
maxheight = max(vowels)
numbars = len(vowels)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")
wn.delay(None)
wn.tracer(4, None)

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

counter = 0
for letter in vowels:
    if counter == 0:
        vowel = "a"
    elif counter == 1:
        vowel = "e"
    elif counter == 2:
        vowel = "i"
    elif counter == 3:
        vowel = "o"
    else:
        vowel = "u"
    drawBar(tess, letter, vowel)
    counter += 1

wn.exitonclick()
