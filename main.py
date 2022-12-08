import pandas
import turtle
screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image) #here we inserted this shape into our screen and is now ready to be used by our turtle
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
print(all_states)
guessed_states=[]
number=0
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states Correct",prompt="What's another guess").title()
    if answer_state=="Exit":
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # df = pandas.DataFrame(missing_states)
        # df.to_csv("states_to_learn.csv")
        # break
        missing_states=[state for state in all_states  if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states: #we can use the in here not a complete loop
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        xcor = int(data[data.state == answer_state].x)
        ycor = int(data[data.state == answer_state].y)
        t.goto(xcor,ycor)
        t.write(answer_state)










screen.exitonclick()




