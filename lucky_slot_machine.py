
from tkinter import *
import tkinter.messagebox
import random

root=Tk()
root.title("Lucky Slots")
root.geometry("400x300")
root.configure(bg="#325C58")


heading_lbl=Label(root,text="LUCKY SLOTS",bg="#325C58",fg="#C29899",font=("Arial",20,"bold"))
heading_lbl.pack(pady=10)


frame=Frame(root,bg="#325C58")
frame.pack()


number1=Label(frame,text="0",bg="#356A65",fg="white",font=("Arial",30))
number1.grid(row=0,column=0,padx=5)

number2=Label(frame,text="0",bg="#356A65",fg="white",font=("Arial",30))
number2.grid(row=0,column=1,padx=5)

number3=Label(frame,text="0",bg="#356A65",fg="white",font=("Arial",30))
number3.grid(row=0,column=2,padx=5)


spin_button=Button(root,text="SPIN",font=("Arial", 16, "bold"),)
spin_button.pack(pady=20)


root.mainloop()
