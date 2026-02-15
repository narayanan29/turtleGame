import random
from turtle import Turtle,Screen

is_race_on=False
screen =Screen()
screen.setup(width=800,height=600)
user_bet=screen.textinput(title="Enter your option to bet" ,prompt="Which color turtle did you bet? Enter a color")
colors=["red","orange","blue","black","yellow","green"]
y_position=[-120,-80,-40,10,50,90]
all_turtles=[]

# Create 6 turtles
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-280,y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        #230 is 250 -half the width turtle
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you won! The winner is {winning_color} turtle is the winner")
            else:
                print(f"You Lose!The winner is {winning_color} turtle is the winner")
         # Make random move for a turtle
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()