from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S State Game")

screen.setup(width=800, height=700)

screen.bgpic("blank_states_img.gif")

states_all_data = pandas.read_csv("50_states.csv")

us_states_list = states_all_data.state.to_list()

guesses_state = []

while len(guesses_state) < 50:
    user_input = screen.textinput(title=f"{len(guesses_state)}/50 States Correct",
                                  prompt="What states do you know?").title()

    if user_input == "Exit":
        _ = [us_states_list.remove(state) for state in guesses_state if state in us_states_list]

        missing_state_csv = pandas.DataFrame(us_states_list)
        missing_state_csv.to_csv("missing_states.csv")
        break

    if user_input in us_states_list:
        guesses_state.append(user_input)
        state_data = states_all_data[states_all_data.state == user_input]
        print(state_data)
        state = Turtle()
        state.penup()
        state.hideturtle()
        state.goto(int(state_data.x), int(state_data.y))
        state.write(f"{user_input}", align="center", font=("Arial", 10, "bold"))




