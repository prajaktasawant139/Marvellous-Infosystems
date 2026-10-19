import tkinter as tk

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("400x300")

# Predefined credentials
USERNAME = "admin"
PASSWORD = "admin123"

tk.Label(root, text="Login Form",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
entryUser = tk.Entry(root)
entryUser.pack()

tk.Label(root, text="Password").pack()
entryPass = tk.Entry(root, show="*")
entryPass.pack()


def Login():
    if entryUser.get() == USERNAME and entryPass.get() == PASSWORD:
        labelResult.config(text="Login Successful", fg="green")
    else:
        labelResult.config(text="Invalid Username or Password", fg="red")


tk.Button(root, text="Login", command=Login).pack(pady=15)

labelResult = tk.Label(root, text="", font=("Arial", 14))
labelResult.pack()

root.mainloop()