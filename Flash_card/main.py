from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy Cards")


def flip_card():
    canvas.itemconfig(background_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


flip_timer = window.after(3000, func=flip_card)


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    random_dict = random.choice(to_learn)
    current_card.update(random_dict)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(background_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


canvas = Canvas(width=800, height=526)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
background_img = canvas.create_image(400, 263, image=card_front_img)
word_text = canvas.create_text(400, 263, font=("Arial", 50, "bold"))
title_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
