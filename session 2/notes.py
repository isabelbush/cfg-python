# User Input
name = input('What is your name? ')
print('Hello, {}'.format(name))

animal = input('What is your favourite animal? ')
pet_name = input('What would you name your pet? ')
print('Your favourite animal is {0} and you would name your pet {1}'.format(animal, pet_name))

# Type Conversion
friends = input('How many friends are at your house? ')
pizzas = int(friends) * 0.5
print('You need {} pizzas for {} friends'.format(pizzas, friends))

# Modules and Loops
import turtle

sides = int(input('Number of sides: '))

turtle.speed('fastest')

angle = 360 / sides
side_length = 60

for side in range(sides):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done

# Functions
def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area

circle = circle_area(10)

print(circle)

