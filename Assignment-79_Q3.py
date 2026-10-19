import tkinter as tk
import math

root = tk.Tk()
root.title("Area of Circle")
root.geometry("400x300")

tk.Label(root, text="Area of Circle",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter radius of the circle").pack()
entry1 = tk.Entry(root)
entry1.pack()


def CalculateArea():
    try:
        radius = float(entry1.get())
        if radius < 0:
            labelResult.config(text="Radius cannot be negative")
            return
        area = math.pi * radius * radius
        labelResult.config(text="Area of circle is : " + str(round(area, 2)))
    except ValueError:
        labelResult.config(text="Please enter a valid number")


tk.Button(root, text="Calculate Area", command=CalculateArea).pack(pady=15)

labelResult = tk.Label(root, text="", font=("Arial", 14))
labelResult.pack()

root.mainloop()