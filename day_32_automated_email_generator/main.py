import smtplib
import random
import datetime as dt
import pandas

sender_email = "pythonkarla@gmail.com"
sender_password = "smna fygs oaar fxmt"
letter_options = ["letter1", "letter2"]
letter_template = ""


def send_email(receiver_email, message):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(sender_email, sender_password)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=message)


def generate_letter(receiver_name):
    global letter_template
    pick_letter = random.choice(letter_options)

    if pick_letter == "letter1":
        with open("letter_templates/letter1.csv") as data:
            letter_template = data.read()
    else:
        with open("letter_templates/letter2.csv") as data:
            letter_template = data.read()

    new_letter = letter_template.replace("[NAME]", receiver_name)

    return new_letter


birthday_info = pandas.read_csv("birthdays.csv").to_dict(orient="records")

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

for person in birthday_info:
    if person["month"] == current_month:
        if person["day"] == current_day:
            finished_letter = f"Subject: HAPPY BIRTHDAY!! \n\n {generate_letter(person['name'])}"
            send_email(receiver_email=person["email"], message=finished_letter)
