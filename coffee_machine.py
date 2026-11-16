from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Coffee Machine")
root.geometry("500x800")
root.configure(bg="white")


drink_lbl=Label(root,text="Drink: ",bg="white",fg="black",font=("Arial",18))
drink_lbl.pack()

drink_val=["Cappiccino","Coffee","Tea","Latte","Americano","Expresso"]
drink_var=StringVar()
drink_box=ttk.Combobox(root,textvariable=drink_var,value=drink_val,width=3,state="readonly")
drink_box.pack()


sugar_lbl=Label(root,text="Sugar: ",bg="white",fg="black",font=("Arial","18"))
sugar_lbl.pack()

end_val=StringVar()
opt1=Radiobutton(root,text="None",variable=end_val,value="None",bg="white",fg="black")
opt1.pack()
opt2=Radiobutton(root,text="Low",variable=end_val,value="Low",bg="white",fg="black")
opt2.pack()
opt3=Radiobutton(root,text="High",variable=end_val,value="Hidh",bg="white",fg="black")
opt3.pack()


milk_lbl=Label(root,text="Milk: ",bg="white",fg="#1C2130",font=("Arial",18))
milk_lbl.pack()

end_val=StringVar()
option1=Radiobutton(root,text="Dairy",variable=end_val,value="Dairy",bg="white",fg="black")
option1.pack()
option2=Radiobutton(root,text="Soy",variable=end_val,value="Soy",bg="white",fg="black")
option2.pack()
option3=Radiobutton(root,text="Almond",variable=end_val,value="Almond",bg="white",fg="black")
option3.pack()


brew_btn=Button(root,text="BREW",bg="red",fg="black",font=("Arial","18"))
brew_btn.pack()


display_lbl=Label(root,text="",bg="white",fg="black",font=("Arial","18"))
display_lbl.pack()

root.mainloop()
