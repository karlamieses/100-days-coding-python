import random
import string
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choices, randint


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a new password when clicking on generate password and copy the password to the keyboard"""
    special_characters = "!@#$%^&*()_+"
    alphabet = string.ascii_letters
    numbers = "123456789"

    password = choices(special_characters + numbers + alphabet, k=randint(8, 20))
    password_string = "".join(password)

    password_entry.insert(0, string=f"{password_string}")
    pyperclip.copy(password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    """Saves the password into a csv file named data and validate if there are empty fields"""
    get_website = website_label_entry.get()
    get_username_email = email_username_entry.get()
    get_password = password_entry.get()

    print(len(get_website))
    print(len(get_password))
    print(len(get_username_email))

    if len(get_website) == 0 or len(get_password) == 0 or len(get_username_email) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any of the fields empty")

    else:
        is_ok = messagebox.askokcancel(title=get_website, message=f"These are the details entered: \n"
                                                                  f"Email: {get_username_email}\n"
                                                                  f"Password: {get_password} \n"
                                                                  f"Is this ok to save? ")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{get_website} | {get_username_email} | {get_password}\n")

            website_label_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_label_entry = Entry()
website_label_entry.focus()
website_label_entry.config(width=38)
website_label_entry.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry()
email_username_entry.insert(0, string="mypasswordmanager@gmail.com")
email_username_entry.config(width=38)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_password)
add_button.config(width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
