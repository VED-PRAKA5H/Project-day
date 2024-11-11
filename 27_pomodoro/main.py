from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, timer
    if timer:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    label_timer.config(text="Timer")
    label_checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps, timer

    # Cancel the existing timer if one is running
    if timer:
        window.after_cancel(timer)

    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_timer.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_timer.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label_timer.config(text="WORK TIME", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = "✔" * (reps // 2)
        label_checkmark.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP -------------------------------

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

image = PhotoImage(file="tomato.png")

canvas = Canvas(width=205, height=226, bg=YELLOW, highlightthickness=0)
canvas.create_image(104, 114, image=image)
timer_text = canvas.create_text(104, 138, text="00:00", font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=1, column=1)

label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, 'bold'))
label_timer.grid(row=0, column=1)

label_checkmark = Label(text="", bg=YELLOW, fg="#FF6969", font=("Ariel", 25, 'bold'))
label_checkmark.grid(row=3, column=1)

start_btn = Button(text="Start", bg="#3572EF", font=("Ariel", 10), command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", bg="#3572EF", font=("Ariel", 10), command=reset_timer)
reset_btn.grid(row=2, column=2)

window.mainloop()
