import json
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

    # Creates the dictionary that is going to be appended into the dictionary
    # that will be used to create the Json file
    new_data = {
        get_website: {
            "email": get_username_email,
            "password": get_password
        }
    }

    if len(get_website) == 0 or len(get_password) == 0 or len(get_username_email) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any of the fields empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading the Json file and convert the reading into a dictionary
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating the data dictionary by appending the new_data dictionary
            data.update(new_data)

            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_label_entry.delete(0, "end")
            password_entry.delete(0, "end")


def search_password():
    try:
        get_website = website_label_entry.get().title()
        with open("data.json", mode="r") as file:
            website_password = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="File doesn't exist")
    else:
        if get_website in website_password:
            email = website_password[get_website]["email"]
            password = website_password[get_website]["email"]

            messagebox.showinfo(title=get_website,
                                message=f"Email: {email}.\nPassword: {password}")
        else:
            messagebox.showinfo(title=get_website, message="Website is empty or that password does not exist")


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
website_label_entry.grid(column=1, row=1)

search_button = Button(text="Search", command=search_password)
search_button.config(width=10)
search_button.grid(column=2, row=1)

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
