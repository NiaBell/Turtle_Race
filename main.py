import random
from turtle import Turtle, Screen
screen=Screen()
screen.setup(width=500,height=400)
is_race_on=False
user_bet=screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors=["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles=[]

tim=Turtle(shape="turtle")
tim.penup()
tim.goto(x=-180,y= 150)
tim.color("green")
all_turtles.append(tim)

aisling=Turtle(shape="turtle")
aisling.penup()
aisling.goto(x=-180,y= 130)
aisling.color("purple")
all_turtles.append(aisling)

merlin=Turtle(shape="turtle")
merlin.penup()
merlin.goto(x=-180,y= 110)
merlin.color("blue")
all_turtles.append(merlin)

rantham=Turtle(shape="turtle")
rantham.penup()
rantham.goto(x=-180,y= 90)
rantham.color("orange")
all_turtles.append(rantham)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The winning turtle is {winning_color}")
            else:
                print(f"You lose. The winning turtle is {winning_color}")




        random_distance=random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()

