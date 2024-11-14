from tkinter import *
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
TIMER_START = 5
timer = None

# ---------------------------- LOAD THE DATA ------------------------------- #
data = pd.read_csv("data/hi_en_words.csv")

try:
    to_learn = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    # Save full dataframe to 'to_learn.csv' if file doesn't exist
    data.to_csv("data/to_learn.csv", index=False)
    to_learn = data.copy()
finally:
    Hindi_list = to_learn["Hindi"].to_list()

is_front_displayed = True

HINDI_WORD = ""
ENGLISH_WORD = ""

# ---------------------------- WORD SELECTION ------------------------------- #
def change_word():
    global HINDI_WORD, ENGLISH_WORD, Hindi_list
    if Hindi_list:
        HINDI_WORD = random.choice(Hindi_list)
        ENGLISH_WORD = data[data["Hindi"] == HINDI_WORD]["English"].values[0]
    else:
        HINDI_WORD = "Finished!"
        ENGLISH_WORD = "All words\nlearned."

# ---------------------------- RIGHT AND WRONG ------------------------------- #
def right():
    global timer, to_learn, Hindi_list
    if timer:
        window.after_cancel(timer)
    if HINDI_WORD in Hindi_list:
        to_learn = to_learn[to_learn['Hindi'] != HINDI_WORD]
        to_learn.to_csv("data/to_learn.csv", index=False)
        Hindi_list = to_learn["Hindi"].to_list()  # Update list after removal
    if Hindi_list:
        show_next_card()
    else:
        finish_session()

def wrong():
    global timer
    if timer:
        window.after_cancel(timer)
    back_card()
    if Hindi_list:
        window.after(2000, show_next_card)
    else:
        window.after(2000, finish_session)

# ---------------------------- CARD DISPLAY ------------------------------- #
def front_card():
    global is_front_displayed
    is_front_displayed = True
    canvas.itemconfig(timer_text, text=f"00:{TIMER_START:02d}", fill='red')
    canvas.itemconfig(front_title, text="Hindi", fill="black")
    canvas.itemconfig(front_word, text=HINDI_WORD, fill="black")
    canvas.itemconfig(front_image, image=front)
    if Hindi_list:
        count_down(TIMER_START)
    else:
        canvas.itemconfig(timer_text, text="")

def back_card():
    global is_front_displayed
    is_front_displayed = False
    canvas.itemconfig(front_title, text="English", fill="white")
    canvas.itemconfig(front_word, text=ENGLISH_WORD, fill="white")
    canvas.itemconfig(front_image, image=back)
    canvas.itemconfig(timer_text, text="")  # Hide the timer text

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    if not is_front_displayed or not Hindi_list:
        return  # Exit if back side is showing or no words left
    if count > 0:
        canvas.itemconfig(timer_text, text=f"00:{count:02d}", fill="red")
        timer = window.after(1000, count_down, count - 1)
    else:
        canvas.itemconfig(timer_text, text="00:00", fill="red")
        back_card()
        if Hindi_list:
            window.after(2000, show_next_card)
        else:
            window.after(2000, finish_session)

def show_next_card():
    change_word()
    front_card()

def finish_session():
    # Disable buttons and show finished message
    right_btn.config(state=DISABLED)
    wrong_btn.config(state=DISABLED)
    canvas.itemconfig(front_title, text="Congratulations!", fill="green")
    canvas.itemconfig(front_word, text="You've learned\nall the words!", fill="green")
    canvas.itemconfig(front_image, image=front)
    canvas.itemconfig(timer_text, text="")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyFlashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    front = PhotoImage(file="images/card_front.png")
    back = PhotoImage(file="images/card_back.png")
except Exception as e:
    raise FileNotFoundError("Image files not found. Please ensure images are in the 'images' folder.") from e

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = canvas.create_image(400, 263, image=front)
front_title = canvas.create_text(400, 110, text="", font=(FONT_NAME, 40, 'italic'))
front_word = canvas.create_text(400, 280, text="", font=(FONT_NAME, 60, 'bold'))
timer_text = canvas.create_text(100, 50, text="", font=(FONT_NAME, 30), fill="red")
canvas.grid(row=0, column=0, columnspan=3)

try:
    right_img = PhotoImage(file="images/right.png").subsample(2, 2)
    wrong_img = PhotoImage(file="images/wrong.png").subsample(2, 2)
except Exception as e:
    raise FileNotFoundError("Button image files not found.") from e

# Button positions: Right on right, Wrong on left
right_btn = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
right_btn.grid(row=1, column=2, pady=30)

wrong_btn = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong)
wrong_btn.grid(row=1, column=0, pady=30)

# Initialize app
change_word()
front_card()

window.mainloop()
