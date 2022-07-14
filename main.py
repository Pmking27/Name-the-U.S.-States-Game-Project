from turtle import Turtle,Screen
import pandas as pd

timmy = Turtle()
screen =Screen()
image ="blank_states_img.gif"
screen.addshape(image)
timmy.shape(image)

gussed_state = []
data =pd.read_csv("50_states.csv")
all_state=data.state.to_list()

while len(gussed_state)<50:
    answer_state=screen.textinput(title=f"{len(gussed_state)}/50 State Corrent",
                                  prompt="What is another state's name ").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in gussed_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break        
    if answer_state in all_state:
        gussed_state.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["state"]==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
   
