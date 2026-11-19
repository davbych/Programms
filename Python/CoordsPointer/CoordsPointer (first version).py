from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Координаты курсора")
root.attributes("-topmost", True)
root.attributes("-alpha", 0.5)
root.geometry("200x50+825+550")

label = Label(root, text=f"X: 0, Y: 0", font=("Arial", 14, "bold"))
label.pack(expand=True)

def update_coords():
    x, y = root.winfo_pointerxy()
    label.config(text=f"X: {x}, Y: {y}")
    root.after(16, update_coords)

update_coords()
root.mainloop()