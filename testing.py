from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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

    if web and passwords:
        question = messagebox.askokcancel(title=web,
                                          message=f"These are the details entered: \nEmail: {emails}\nPassword: {passwords}"
                                                  f"\nIs it okay to save? ")
        if question:
            with open("data.txt", "a") as file:
                file.write(web + ' | ' + emails + ' | ' + passwords + '\n')
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
        else:
            pass
    else:
        messagebox.showerror(title="Empty Field", message="Please don't leave any fields empty")


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
web_entry = Entry(width=30)  # Reduced width
web_entry.grid(column=1, row=1, padx=(0, 10), pady=5, sticky="w")  # Adjusted padx and sticky
web_entry.focus()
email_entry = Entry(width=30)  # Reduced width
email_entry.grid(column=1, row=2, padx=(0, 10), pady=5, sticky="w")  # Adjusted padx and sticky
email_entry.delete(0, END)
email_entry.insert(0, "angela@gmail.com")
pass_entry = Entry(width=18)
pass_entry.grid(column=1, row=3, padx=(0, 10), pady=5, sticky="w")  # Adjusted padx and sticky

# Buttons
gene_pass = Button(text="Generate Password", command=Password)
gene_pass.grid(column=2, row=3, pady=5)  # Adjusted pady
add = Button(text="Add", width=30, command=Add)  # Reduced width
add.grid(row=4, column=1, columnspan=2, padx=10, pady=5)  # Adjusted padx and pady

window.mainloop()
