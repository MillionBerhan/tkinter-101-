import tkinter as tk

root = tk.Tk()
root.title("Hello!")
root.geometry("200x200")
root.configure(bg="Grey")

box1 = tk.Label(
    root,
    text="Hello Tkinter!",
    bg = "green",
    fg = "blue"
    )

box1.pack(
    ipadx=20,
    ipady=20
)


root.mainloop()