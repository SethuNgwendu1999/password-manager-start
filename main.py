from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list_1 = [choice(letters) for x in range(randint(8, 10))]
    password_list_2 = [choice(symbols) for x in range(randint(2, 4))]
    password_list_3 = [choice(numbers) for x in range(randint(2, 4))]

    password_list = password_list_1 + password_list_2 + password_list_3
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def Add():
    web = web_entry.get()
    emails = email_entry.get()
    passwords = pass_entry.get()
    new_data = {web: {
        "email": emails,
        "password": passwords,
    }}

    if web and passwords:
        question = messagebox.askokcancel(title=web,
                                          message=f"These are the details entered: \nEmail: {emails}\nPassword: {passwords}"
                                                  f"\nIs it okay to save? ")
        if question:
            try:

                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            web_entry.delete(0, END)
            pass_entry.delete(0, END)

        else:
            pass


    else:
        messagebox.showerror(title="Empty Field", message="Please don't leave any fields empty")


def find_password():
    web_name = web_entry.get()
    emails = email_entry.get()
    passwords = pass_entry.get()
    new_data = {web_name: {
        "email": emails,
        "password": passwords,
    }}
    try:
        with open("data.json", "r") as file:
            read = json.load(file)
            if web_entry.get() in read:
                web = web_entry.get()
                email_pass = read[web]
                email_pass2 = []
                for ep in email_pass:
                    first = f"{ep}: {email_pass[ep]}"
                    email_pass2.append(first)
                messagebox.showinfo(title=f"{web}", message=f"{email_pass2[0]} \n {email_pass2[1]}")

            else:
                messagebox.showinfo(title="Error", message=f"No detail for {web_entry.get()} exists")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password-Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# Label's
website = Label(text="Website:")
website.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entry's
web_entry = Entry(width=18)
web_entry.grid(column=1, row=1)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.delete(0, END)
email_entry.insert(0, "angela@gmail.com")
pass_entry = Entry(width=18)
pass_entry.grid(column=1, row=3)

# Buttons
gene_pass = Button(text="Generate Password", command=Password)
gene_pass.grid(column=2, row=3)
add = Button(text="Add", width=36, command=Add)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", width=17, command=find_password)
search.grid(column=2, row=1)

window.mainloop()
