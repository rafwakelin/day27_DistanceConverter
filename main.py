import tkinter

window = tkinter.Tk()
window.title("Distance Converter")
window.config(padx=30, pady=30)


def convert():
    """Take km as input and convert to miles"""
    m = float(miles_to_covert.get())
    convert_km = round(m * 1.609344, 1)
    in_km = tkinter.Label(text=f"{convert_km}")
    in_km.grid(column=1, row=1)


miles_to_covert = tkinter.Entry(width=5)
miles_to_covert.grid(column=1, row=0)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)

km = tkinter.Label(text="kilometers")
km.grid(column=2, row=1)

calculate = tkinter.Button(text="Calculate", relief="raised", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()
