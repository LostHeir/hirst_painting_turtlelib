import colorgram
import random
import turtle

DOT_SIZE = 20
SCREEN_WIDTH = 420
SCREEN_HEIGHT = 400

colors = colorgram.extract('dots.jpg', 25)
turtle.colormode(255)
turtle.Screen().setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT,)
myTurtle = turtle.Turtle()
myTurtle.speed(10)


def random_color():
    """"Returns random color as a tuple (r, g , b). Color is one of the color samples from image,
     which were taken by colorgram module"""
    ret_color = random.choice(colors)
    while ret_color.rgb.r > 240 and ret_color.rgb.g > 240 and ret_color.rgb.b > 240:
        ret_color = random.choice(colors)

    r = ret_color.rgb.r
    g = ret_color.rgb.g
    b = ret_color.rgb.b
    rgb_tuple = (r, g, b)
    return rgb_tuple




def set_ini_pos():
    """Set turtle in the left-down corner"""
    myTurtle.penup()
    myTurtle.setpos(-(SCREEN_WIDTH//2-DOT_SIZE), -(SCREEN_HEIGHT//2-DOT_SIZE))
    myTurtle.pendown()


def painting():
    """Paints dots depending on how big is teh screen 'SCREEN_HEIGHT, SCREEN_WIDTH' is and how what 'DOT_SIZE' is. """
    for __ in range(0, SCREEN_HEIGHT // (DOT_SIZE * 2)):
        for _ in range(1, SCREEN_WIDTH // (DOT_SIZE * 2)):
            myTurtle.dot(DOT_SIZE, random_color())
            myTurtle.penup()
            myTurtle.forward(DOT_SIZE*2)
            myTurtle.pendown()
            myTurtle.dot(DOT_SIZE, random_color())
        myTurtle.setheading(90)
        myTurtle.penup()
        myTurtle.forward(DOT_SIZE * 2)
        myTurtle.pendown()
        if __ % 2 == 0:
            myTurtle.setheading(180)
        else:
            myTurtle.setheading(0)


set_ini_pos()
painting()


turtle.Screen().exitonclick()
