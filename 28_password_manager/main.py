import random
from tkinter import *
from tkinter import messagebox
YELLOW = "#f7f5dd"
FONT_NAME = "Ariel"
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = ""
    for i in range(20):
        password += chr(random.randint(33, 126))
    entry3.delete(0, END)
    entry3.insert(0, password)
    entry3.clipboard_clear()
    entry3.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    """Saves the password in a text file"""
    if len(entry2.get()) == 0 or len(entry3.get()) == 0 or len(entry1.get()) == 0:
        messagebox.showinfo(title="Oops🚫", message="Left something!!")

    else:
        yes = messagebox.askyesno(title="Confirmation!!",
                                  message=f"Do you want to save following credentials?\nWebsite: {entry1.get()}"
                                          f"\nEmail: {entry2.get()}\nPassword: {entry3.get()}")
        if yes:
            new_data = {entry1.get(): {"email": entry2.get(), "password": entry3.get()}}
            try:
                with open("passwords.json", "r") as file:
                    # Reading the old data
                    data = json.load(file)
                    # Updating old data
                    data.update(new_data)
                with open('passwords.json', "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump({entry1.get(): {"email": entry2.get(), "password": entry3.get()}}, file, indent=4)

            finally:
                entry3.delete(0, END)
                entry1.delete(0, END)

# ---------------------------- SHOW PASSWORD ------------------------------- #


def show_password():
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            if entry1.get() in data:
                messagebox.showinfo(title=entry1.get(), message=f"email: {data[entry1.get()]["email"]}\n"
                                                                      f"password: {data[entry1.get()]["password"]}")
            else:
                messagebox.showinfo(title="Oops", message="Password not found")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Password found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=250)

image = PhotoImage(file="logo.png")
canvas.create_image(150, 125, image=image)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
entry1 = Entry(width=49)
entry1.insert(0, "groww.com")
entry1.focus()    # send cursor to entry box
entry1.grid(row=1, column=1)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
entry2 = Entry(width=70)
entry2.insert(0, "ved@gmail.com")
entry2.grid(row=2, column=1, columnspan=3)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)
entry3 = Entry(width=49)
entry3.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", bg="#3572EF", font=("Ariel", 10), command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", bg="#9bdeac", font=("Ariel", 10), width=52, command=save_password)
add_btn.grid(row=4, column=1, columnspan=3)

search_btn = Button(text="Search", bg="#9bdeac", font=("Ariel", 10), width=13, command=show_password)
search_btn.grid(row=1, column=2)

window.mainloop()
