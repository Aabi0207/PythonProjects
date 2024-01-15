from tkinter import *
import pandas
import random
import pyttsx3


engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 135)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# engine.say("The quick brown fox jumped over the lazy dog.")
# engine.runAndWait()

volume = engine.getProperty('volume')
engine.setProperty('volume',1.5)

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("C:/Users/abhis/OneDrive/Desktop/PythonProjects/EnglishVocabulary/data/words_to_learn.csv", encoding="utf-8", delimiter=",", engine='python')
except FileNotFoundError:
    original_data = pandas.read_csv("C:/Users/abhis/OneDrive/Desktop/PythonProjects/EnglishVocabulary/data/new_data.csv", encoding="UTF-8", delimiter=":;", engine='python')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy Cards")


def flip_card():
    canvas.itemconfig(background_img, image=card_back_img)
    canvas.itemconfig(title_text, text=current_card["meaning"], fill="white")
    canvas.itemconfig(word_text, text=current_card["example"], fill="white")


flip_timer = window.after(3000, func=flip_card)


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    random_dict = random.choice(to_learn)
    current_card.update(random_dict)
    canvas.itemconfig(word_text, text=current_card["word"], fill="black")
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(background_img, image=card_front_img)
    engine.say(current_card["word"])
    engine.runAndWait()
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("C:/Users/abhis/OneDrive/Desktop/PythonProjects/EnglishVocabulary/data/words_to_learn.csv", index=False)
    next_card()


canvas = Canvas(width=800, height=526)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="C:/Users/abhis/OneDrive/Desktop/PythonProjects/EnglishVocabulary/images/card_front.png")
card_back_img = PhotoImage(file="C:/Users/abhis/OneDrive/Desktop/PythonProjects/EnglishVocabulary/images/card_back.png")
background_img = canvas.create_image(400, 263, image=card_front_img)
word_text = canvas.create_text(400, 250, font=("Arial", 25, "bold"), width=750)
title_text = canvas.create_text(400, 70, font=("Arial", 30, "italic"), width=750)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="C:/Users/abhis/OneDrive/Desktop/PythonProjects/EnglishVocabulary/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="C:/Users/abhis/OneDrive/Desktop/PythonProjects/EnglishVocabulary/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
