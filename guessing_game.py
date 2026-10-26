from tkinter import *
import tkinter.messagebox
import random

root=Tk()
root.geometry("450x300")
root.title("Guessing Game")
root.configure(bg="#FF6F85")

heading_lbl=Label(root, text="Guess the number", bg="#FF6F85", fg="#E1EFE6", font=("Calibri",25,"bold"))
heading_lbl.pack()

frame=Frame(root,bg="#FF6F85")
frame.pack()

name_lbl=Label(frame, text="Enter your name: ", bg="#FF6F85", fg="#333D2A", font=("Calibri",16))
name_lbl.grid(row=0,column=0,pady=20)

name_box=Entry(frame, justify="center")
name_box.grid(row=1,column=0)

ok_btn=Button(frame, text="OK", bg="#5E2450", fg="white", font=("Calibri",16))
ok_btn.grid(row=1,column=1,padx=20)

guess_lbl=Label(frame, text="Guess the number: ", bg="#FF6F85", fg="#333D2A", font=("Calibri",16))
guess_lbl.grid(row=3,column=0,pady=20)

guess_box=Entry(frame, justify="center")
guess_box.grid(row=4,column=0)

guess_btn=Button(frame, text="guess", bg="#5E2450", fg="white", font=("Calibri",16))
guess_btn.grid(row=4,column=1,padx=20)

root.mainloop()