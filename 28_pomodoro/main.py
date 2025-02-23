from tkinter import *
import math

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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    label_timer.config(text="TIMER")
    label_checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    shortbreak_sec = SHORT_BREAK_MIN*60
    longbreak_sec = LONG_BREAK_MIN*60
    reps += 1

    if reps%2 == 1:
        count_down(shortbreak_sec)
        label_timer.config(text="WORK TIME", fg=GREEN)


    elif reps%2 == 0 and reps<=6:
        label_timer.config(text="SHORT BREAK", fg=PINK)
        count_down(longbreak_sec)

    elif reps % 8 == 0:
        label_timer.config(text="LONG BREAK", fg=RED)
        count_down(48)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    canvas.itemconfig(timer_text, text=f"{"{:02d}".format(count_min)}:{"{:02d}".format(count_sec)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = "      ✔"
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        print(marks)
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP -------------------------------

window = Tk()
window.title("POMODORO")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50, bg=YELLOW)
window.eval('tk::PlaceWindow . right')   # to place a window on the screen center in Tkinter

image = PhotoImage(file="tomato.png")

canvas = Canvas(width=205, height=226, )
canvas.config(bg=YELLOW)
canvas.config(highlightthickness=0)               # to remove border of an image
canvas.create_image(104, 114, image=image)
timer_text = canvas.create_text(104, 138, text="00:00", font=("New Roman", 20, 'bold'))
canvas.grid(row=1, column=1)
label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Courier", 25,'bold'))
label_timer.grid(row=0, column=1)
label_checkmark = Label(text="", bg=YELLOW, fg="#FF6969", font=("Ariel", 25,'bold'))
label_checkmark.grid(row=3, column=1)

start_btn = Button(text="Start", bg="#3572EF", font=("Ariel", 10), command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", bg="#3572EF", font=("Ariel", 10), command=reset_timer)
reset_btn.grid(row=2, column=2)


window.mainloop()
