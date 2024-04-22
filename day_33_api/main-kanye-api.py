from tkinter import *
import requests
import datetime as dt

kanye_url = "https://api.kanye.rest"


def generate_quote():
    response = requests.get(url=kanye_url).json()
    response.raise_for_status()
    quote = response["quote"]
    return quote


def get_quote():
    quote = generate_quote()
    canvas.itemconfig(quote_text, text=quote)


kanye_quote = generate_quote()

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=kanye_quote, width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()

url="https://api.sunrise-sunset.org/json"
request_parameters = {
    "lat": 51.52004282729549,
    "lng": -0.12692751123848423,
    "formatted": 0
}
response = requests.get(url=url, params=request_parameters).json()
sunrise = response["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)

current_date = dt.datetime.now()
print(current_date.hour)