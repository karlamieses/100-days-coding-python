import tkinter

window = tkinter.Tk()
window.config(padx=30, pady=30)
window.title("Mile to KM Converter")

font = ("Arial", 15)
label_equal_to = tkinter.Label(text="Is equal to", font=font)
label_equal_to.grid(column=0, row=1)

miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles", font=font)
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)

label_km_result = tkinter.Label(text="0", font=font)
label_km_result.grid(column=1, row=1)

label_km = tkinter.Label(text="Km", font=font)
label_km.grid(column=2, row=1)


def calculate():
    user_mile_entry = miles_entry.get()
    convert_to_km = round(float(user_mile_entry) * 1.60)
    label_km_result["text"] = convert_to_km


button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
