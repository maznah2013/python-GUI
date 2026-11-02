from tkinter import *
import tkinter.messagebox
import random

number=random.randint(1,100)

def name_confirm():
    name=name_entry.get()
    tkinter.messagebox.showinfo("name", f"Hello {name}. I have thought of a number, can you guess whether it is odd or even?")

def guess_confirm():
    guess=guess_entry.get()
    if number%2==0 and guess=="even":
        tkinter.messagebox.showinfo("even", "You have made a correct guess, it's an even number!")
    elif number%2!=0 and guess=="odd":

root=Tk()
root.geometry("450x300")
root.title("ODD OR EVEN")
root.configure(bg="#aa95bd")

heading_lbl=Label(root,text="Odd or Even Guess",bg="#aa95bd",fg="#033649",font=("Calibri",25,"bold"))
heading_lbl.pack()

name_lbl=Label(root,text="Enter your name: ",bg="#aa95bd",fg="#16162C",font=("Calibri",18,"normal"))
name_lbl.place(x=10,y=60)

name_entry=Entry(root,justify="center")
name_entry.place(x=160,y=60)

name_btn=Button(root,text="OK",bg="#aa95bd",fg="#16162C",font=("Calibri",18,"normal"),command=name_confirm)
name_btn.place(x=360,y=60)


guess_lbl=Label(root,text="Choose your guess: ",bg="#aa95bd",fg="#16162C",font=("Calibri",18,"normal"))
guess_lbl.place(x=10,y=130)

odd_btn=Button()

root.mainloop()