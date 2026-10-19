import tkinter as tk

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("450x320")

tk.Label(root, text="Voting Eligibility Checker",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter name").pack()
entryName = tk.Entry(root)
entryName.pack()

tk.Label(root, text="Enter age").pack()
entryAge = tk.Entry(root)
entryAge.pack()


def CheckEligibility():
    name = entryName.get()
    try:
        age = int(entryAge.get())
        if age >= 18:
            labelResult.config(text=name + " is eligible to vote")
        else:
            labelResult.config(text=name + " is not eligible to vote")
    except ValueError:
        labelResult.config(text="Please enter a valid age")


tk.Button(root, text="Check Eligibility", command=CheckEligibility).pack(pady=15)

labelResult = tk.Label(root, text="", font=("Arial", 14))
labelResult.pack()

root.mainloop()