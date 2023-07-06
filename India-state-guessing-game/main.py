import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("Indian states game")
#screen.setup(width=500, height=500)
image = "9671e6ba88f7b2ed4bea5941ffebf8ee (1).gif"

#def get_mouse_click_coor(x,y):
 #   print(x,y)

#turtle.onscreenclick(get_mouse_click_coor)

data = pd.read_csv("states.csv")
#print(data)
all_states = data['States'].to_list()
#print(all_states)
guessed_states = []

screen.addshape(image)
turtle.shape(image)

#answer_state = screen.textinput(title= "Guess the state", prompt= "Name a state!")

while len(guessed_states) < 30:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.States == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    #print(guessed_states)
    #print(missing_states)

turtle.mainloop()