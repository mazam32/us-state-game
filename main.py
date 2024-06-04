import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
df = pandas.read_csv("50_states.csv")
states = df.state
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title= f"{len(correct_guesses)}/50 States Correct", prompt= "What's another state's name?")
    answer_state = answer_state.title()
    
    if answer_state == "Exit":
        break
    if len(df[df.state == answer_state]) != 0:
        state_series = df[df.state == answer_state]
        idx = state_series.index[0]
        name_of_the_state = state_series.state[idx]

        if name_of_the_state not in correct_guesses:
            correct_guesses.append(name_of_the_state)
            
            x_cor = state_series.x[idx]
            y_cor = state_series.y[idx]
            
            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.goto(x_cor, y_cor)
            
            state_name.write(name_of_the_state)

all_states = states.to_list()
states_to_learn = []
for pros in all_states:
    if pros not in correct_guesses:
        states_to_learn.append(pros)

df_to_use = pandas.DataFrame(states_to_learn)
df_to_use.to_csv("states_to_learn.csv")