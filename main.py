from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    entry_p.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)

    entry_p.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_w.get().lower()
    email = entry_e.get()
    passw = entry_p.get()
    new_data = {
        website: {
            "email": email,
            "password": passw,
        }
    }

    if len(website) == 0 or len(passw) == 0:
        messagebox.showerror(title="Error", message="Fields can't be empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nWebsite: {website} \nEmail: {email} "
                                               f"\nPassword: {passw} \nSave to file?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            entry_w.delete(0, END)
            entry_p.delete(0, END)
            messagebox.showinfo(title="Success", message="Password saved to file")


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = entry_w.get().lower()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]
    except:
        messagebox.showerror(title="Error", message=f"Password for {website} not found")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator and Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

label_w = Label(text="Website:")
label_w.grid(column=0, row=1)

label_e = Label(text="Email/Username:")
label_e.grid(column=0, row=2)

label_p = Label(text="Password:")
label_p.grid(column=0, row=3)

entry_w = Entry(width=25)
entry_w.focus()
entry_w.grid(column=1, row=1)

entry_e = Entry(width=44)
entry_e.insert(0, "example@gmail.com")
entry_e.grid(column=1, row=2, columnspan=2)

entry_p = Entry(width=25)
entry_p.grid(column=1, row=3)

button_g = Button(text="Generate Password", width=15, command=generate)
button_g.grid(column=2, row=3)

button_a = Button(text="Add", width=37, command=save)
button_a.grid(column=1, row=4, columnspan=2)

button_s = Button(text="Search", width=15, command=search)
button_s.grid(column=2, row=1)

window.mainloop()
