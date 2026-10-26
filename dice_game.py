from tkinter import *
import random

def roll():
    number=random.randint(1,6)
    number_lbl.config(text=number)
    if number=="6":
        number_lbl.config(fg="red")
    else:
        number_lbl.config(fg="#E1EFE6")

root=Tk()
root.geometry("400x450")
root.configure(bg="#151782")
root.title("Dice Roller")

heading_lbl=Label(root, text="Roll the dice", bg="#2E3D72", fg="#E1EFE6", font=("Calibri",25,"bold"))
heading_lbl.pack()

number_lbl=Label(root, text="-", bg="#2E3D72", fg="#E1EFE6", font=("Calibri",45,"bold"))
number_lbl.pack(padx=5, pady=5)

button=Button(root, text="Roll", bg="#78BDD0", fg="#E1EFE6", font=("Calibri",20,"bold"), command=roll)
button.pack()

root.mainloop()