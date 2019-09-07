"""
Use recursion to print nested squares/diamonds
Precondition: Turtle starts facing east in bottom left
Postcondition: Correct shape/colors are drawn, turtle is in start position
"""

import turtle

def set_color(depth):
    """
    Sets the color of the squares
    If depth is even, shapes will be orange
    If depth is odd, shapes will be blue
    """
    colors = ['orange', 'blue']
    turtle.color(colors[depth % 2])


def recur(length, depth):
    """
    Does the actual drawing.
    Draws layered squares, which contain
    Diamonds arranged east-west, which contain
    Squares arranged NW-SE,
    ad infinitum

    Pre: nothing drawn, turtle in start position
    Post: squares drawn, turtle in start position
    """
    if depth > 0:
        for i in range(2):
            set_color(depth)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.backward(length/2)
            turtle.left(45)
            recur(length / (2 ** 1.5), depth - 1)
            turtle.right(45)
            turtle.up()
            turtle.forward(length/2)
            turtle.down()
            turtle.left(90)

def init():
    """
    Sets up the turtle to be in the bottom left

    Pre: Turtle is in default position (0,0)
    Post: Turtle is in bottom left of screen
    """
    turtle.up()
    turtle.setpos(-200,-200)
    turtle.down()

def main():
    """Gets input and calls init() and recur()"""
    init()
    depth = int(input('How many layers of recursion?\n'))
    length = 400
    recur(length, depth)
    turtle.mainloop()

if __name__ == '__main__':
    main()
