"""
Use recursion to print nested squares/diamonds
Precondition: Turtle starts facing east in bottom left
"""

import turtle

"""
Does the actual drawing.
Draws layered squares, which contain
Diamonds arranged east-west, which contain
Squares, arranged NW-SE, etc.
If depth is odd, shapes will be blue
If depth is even, shapes will be orange
"""
def draw_squares(depth):
    if depth % 2 == 1:
        turtle.color('blue')
    else:
        turtle.color('orange')

    if depth > 0:
        pass

"""Sets up the turtle to be in the bottom left"""
def init():
    turtle.up()
    turtle.setpos(-240,-220)
    turtle.down()

"""Gets input and calls init() and draw_squares()"""
def main():
    init()
    depth = int(input('How many layers of recursion?\n'))
    draw_squares(depth)
    turtle.mainloop()

if __name__ == '__main__':
    main()
