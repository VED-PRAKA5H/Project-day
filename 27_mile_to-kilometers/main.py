from tkinter import *

# Window
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)


# Labels
label_miles = Label(text="Miles", font=("New Roman", 20))
label_miles.grid(row=0, column=2)
label_miles.config(pady=20, padx=20)

label_is = Label(text="is equal to", font=("New Roman", 20))
label_is.grid(row=1, column=0)
label_is.config(pady=20, padx=20)

label_km = Label(text="KM", font=("New Roman", 20))
label_km.grid(row=1, column=2)
label_km.config(pady=20, padx=20)

label_ans = Label(text="0", font=("New Roman", 20))
label_ans.grid(row=1, column=1)
label_ans.config(pady=20, padx=20)


def calc():
    x = int(entry.get())
    label_ans.config(text=str("{:.2f}".format(x*1.60934)))


# Button
button = Button(text="calculate", command=calc)
button.grid(row=2, column=1)


# Entry
entry = Entry(width=15,)
entry.grid(row=0, column=1)
entry.focus()

window.mainloop()
