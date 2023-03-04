from tkinter import *
import random
import pandas

BACKGROUND = "#B1DDC6"
current_card = {}


try:
    data_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("./data/french_words.csv")
to_learn = data_file.to_dict(orient="records")

# flip_timer = None


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas_card.itemconfig(title_text, text="French", fill="black")
    canvas_card.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas_card.itemconfig(canvas_image, image=card_front_png)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas_card.itemconfig(title_text, text="English", fill="white")
    canvas_card.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas_card.itemconfig(canvas_image, image=card_back_png)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND)

flip_timer = window.after(3000, func=flip_card)

canvas_card = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
card_front_png = PhotoImage(file="./images/card_front.png")
card_back_png = PhotoImage(file="./images/card_back.png")
canvas_image = canvas_card.create_image(400, 263, image=card_front_png)
title_text = canvas_card.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word_text = canvas_card.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))
canvas_card.grid(row=0, column=0, columnspan=2)

wrong_png = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_png, highlightbackground=BACKGROUND, command=next_card)
button_wrong.grid(row=1, column=0)

right_png = PhotoImage(file="./images/right.png")
button_right = Button(image=right_png, highlightbackground=BACKGROUND, command=is_known)
button_right.grid(row=1, column=1)

next_card()

window.mainloop()
