import random
from turtle import Turtle, Screen

screen = Screen()

#define the game canvas
screen.setup(width=800, height=600)

#define a background image for the game
screen.bgpic('road.gif')

FONT = ("Courier", 28, "bold")
ALIGN = "right"


y_positions = [-260, -172, -85, 2, 85, 172, 260]
colors = ["Red", "Orange", "Yellow", "Pink", "Green", "Blue", "Violet" ]
all_turtle = []
user_bet = screen.textinput("Enter your bet", prompt="Which turtle (red, orange, yellow, pink, green, blue, or violet) ?: ")


#create turtle replicas with for loop
for i in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2)
    new_turtle.speed('fastest')
    new_turtle.penup()
    new_turtle.goto(x=-350, y=y_positions[i])
    new_turtle.color(colors[i].lower())
    all_turtle.append(new_turtle)

is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 330:
            is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                turtle.write(f'You won! {winner} turtle wins.', font=FONT, align=ALIGN)
            else:
                turtle.write(f'You lost! {winner} turtle wins.', font=FONT, align=ALIGN)
        random_pace = random.randint(0,7)
        turtle.forward(random_pace)

screen.exitonclick()

