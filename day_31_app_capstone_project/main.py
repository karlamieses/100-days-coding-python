import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card, window_timer
    window.after_cancel(window_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=front_image)
    window_timer = window.after(3000, flip_card)


def user_know_word():
    global to_learn
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    english_word = current_card["English"]
    canvas.itemconfig(card_text, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=back_image)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window_timer = window.after(3000, flip_card)

## Front Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 35, "italic"))
card_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))

## Wrong Button
unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

## Right Button
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=user_know_word)
known_button.grid(column=1, row=1)

# TODO: Create functionality that moves every 3 seconds


# TODO: Create functionality that if I know the answer don't show it again
next_card()
window.mainloop()
