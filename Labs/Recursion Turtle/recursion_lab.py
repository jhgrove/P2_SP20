"""
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)
2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)
3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion.
Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)

Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

Have fun!
"""

import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_turtle.speed(0)
my_screen = turtle.Screen()
my_screen.bgcolor('white')

'''
# PART 1 - H Tree


def h_tree(x, y, height, width, depth):
    if depth > 0:
        for i in range(2):
            my_turtle.up()
            my_turtle.goto(x, y)
            my_turtle.down()
            my_turtle.goto(x + width / 4, y)
            my_turtle.goto(x + width / 4, y + height / 4)
            my_turtle.goto(x + width / 4, y - height / 4)
            h_tree(x + width / 4, y - height / 4, height / 2, width / 2, depth - 1)
            h_tree(x + width / 4, y + height / 4, height / 2, width / 2, depth - 1)
            height, width = - height, - width


h_tree(0, 0, my_screen.window_height(), my_screen.window_width(), 5)

my_screen.exitonclick()
'''
'''
endpoints = [[0, 300], [-300, -150], [300, -150]]
triangle_num = 5


def big_triangle(endpoints, my_turtle):
    my_turtle.up()
    my_turtle.goto(endpoints[0][0], endpoints[0][1])
    my_turtle.down()
    my_turtle.goto(endpoints[1][0], endpoints[1][1])
    my_turtle.goto(endpoints[2][0], endpoints[2][1])
    my_turtle.goto(endpoints[0][0], endpoints[0][1])


def halfway(x2, y2):
    return [(x2[0] + y2[0]) / 2, (x2[1] + y2[1]) / 2]


def small_triangles(endpoints, triangle_num, my_turtle):
    big_triangle(endpoints, my_turtle)
    if triangle_num > 0:
        small_triangles([endpoints[0], halfway(endpoints[0], endpoints[1]), halfway(endpoints[0], endpoints[2])], triangle_num - 1, my_turtle)
        small_triangles([endpoints[1], halfway(endpoints[0], endpoints[1]), halfway(endpoints[1], endpoints[2])], triangle_num - 1, my_turtle)
        small_triangles([endpoints[2], halfway(endpoints[2], endpoints[1]), halfway(endpoints[0], endpoints[2])], triangle_num - 1, my_turtle)


small_triangles(endpoints, triangle_num, my_turtle)
'''
'''
def draw(length, depth):
    if depth == 0:
        for i in range(0, 3):
            my_turtle.forward(length)
            my_turtle.left(120)
    else:
        draw(length / 2, depth - 1)
        my_turtle.forward(length / 2)
        draw(length / 2, depth - 1)
        my_turtle.back(length / 2)
        my_turtle.left(60)
        my_turtle.forward(length / 2)
        my_turtle.right(60)
        draw(length / 2, depth - 1)
        my_turtle.left(60)
        my_turtle.back(length / 2)
        my_turtle.right(60)


draw(300, 5)
'''




my_screen.exitonclick()
