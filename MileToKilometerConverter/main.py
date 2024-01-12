from tkinter import *

window = Tk()
window.title("Mile to KM converter.")
window.config(padx=20, pady=20)

label1 = Label(text="Miles", font=("normal", 10, "bold"))
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("normal", 10, "bold"))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("normal", 10, "bold"))
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=("normal", 10, "bold"))
label4.grid(column=2, row=1)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)


def button():
    distance = int(entry.get())
    distance_in_km = round(distance*1.609344)
    label3.config(text=distance_in_km)


calculate = Button(text="Calculate", command=button)
calculate.grid(column=1, row=2)

window.mainloop()
