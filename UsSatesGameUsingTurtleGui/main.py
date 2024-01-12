import turtle
import pandas
from guessing_mechanism import GuessingMechanism

screen = turtle.Screen()
screen.title("U.S. States Game.")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

guessing_mechanism = GuessingMechanism()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

answered_states = []
while len(answered_states) < 50:
    guessed_state = screen.textinput(title="Guess the State?", prompt="What's another state's name? ").title()
    answered_states.append(guessed_state)
    if guessed_state == "Exit":
        unanswered_states = [state for state in states_list if state not in answered_states]
        pandas.DataFrame(unanswered_states).to_csv("unanswered_states.csv")
        break
    if guessed_state in states_list:
        state_data = data[data.state == guessed_state]
        guessing_mechanism.place(guessed_state, int(state_data.x), int(state_data.y))



