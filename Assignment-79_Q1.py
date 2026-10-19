import tkinter as tk

root = tk.Tk()
root.title("Addition of Two Numbers")
root.geometry("400x300")

tk.Label(root, text="Addition of Two Numbers",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter first number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack()
entry2 = tk.Entry(root)
entry2.pack()


def Add():
    try:
        no1 = float(entry1.get())
        no2 = float(entry2.get())
        result = no1 + no2
        labelResult.config(text="Addition is : " + str(result))
    except ValueError:
        labelResult.config(text="Please enter valid numbers")


tk.Button(root, text="Add", command=Add).pack(pady=15)

labelResult = tk.Label(root, text="", font=("Arial", 14))
labelResult.pack()

root.mainloop()