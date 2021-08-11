import turtle

def triangle(side_length, colour):
    angle = 120

    turtle.color(colour, colour)
    turtle.begin_fill()

    for triangle in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()

triangle(100, 'blue')
triangle(200, 'green')
triangle(500, 'pink')

turtle.done()