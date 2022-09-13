from tkinter import *


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


def convert():
    miles = int(input.get())
    kilo = round(miles * 1.60934, 2)
    km_label.config(text=kilo)


label = Label(text="is equal to")
label.config(padx=5, pady=5)
label.grid(column=0, row=1)

input = Entry()
input.config(width=15)
input.grid(column=1, row=0)

km_label = Label(text=0)
km_label.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

miles_label = Label(text="Miles")
miles_label.config(padx=5, pady=5)
miles_label.grid(column=2, row=0)

km_label2 = Label(text="KM")
km_label2.config(padx=5, pady=5)
km_label2.grid(column=2, row=1)



window.mainloop()


