from tkinter import *
from tkinter import ttk

def generate_drink():
    order=f"Brewing a {end_val.get()} {drink_var.get()} with {end_value.get()} sugar"
    display_lbl.configure(text=order)



root=Tk()
root.title("Coffee Machine")
root.geometry("500x500")
root.configure(bg="#B4E4E4")


drink_lbl=Label(root,text="Drink: ",bg="#B4E4E4",fg="black",font=("Arial",18))
drink_lbl.place(x=20,y=20)

drink_val=["Cappuccino","Coffee","Tea","Latte","Americano","Expresso"]
drink_var=StringVar()
drink_box=ttk.Combobox(root,textvariable=drink_var,value=drink_val,width=6,state="readonly")
drink_box.place(x=80,y=20)


sugar_lbl=Label(root,text="Sugar: ",bg="#B4E4E4",fg="black",font=("Arial",18))
sugar_lbl.place(x=20,y=80)

end_value=StringVar()
opt1=Radiobutton(root,text="None",variable=end_value,value="None",bg="#B4E4E4",fg="black")
opt1.place(x=80,y=80)
opt2=Radiobutton(root,text="Low",variable=end_value,value="Low",bg="#B4E4E4",fg="black")
opt2.place(x=140,y=80)
opt3=Radiobutton(root,text="High",variable=end_value,value="High",bg="#B4E4E4",fg="black")
opt3.place(x=200,y=80)
end_value.set("None")


milk_lbl=Label(root,text="Milk: ",bg="#B4E4E4",fg="black",font=("Arial",18))
milk_lbl.place(x=20,y=140)

end_val=StringVar()
option1=Radiobutton(root,text="Dairy",variable=end_val,value="Dairy",bg="#B4E4E4",fg="black")
option1.place(x=80,y=140)
option2=Radiobutton(root,text="Soy",variable=end_val,value="Soy",bg="#B4E4E4",fg="black")
option2.place(x=140,y=140)
option3=Radiobutton(root,text="Almond",variable=end_val,value="Almond",bg="#B4E4E4",fg="black")
option3.place(x=200,y=140)
end_val.set("Dairy")


brew_btn=Button(root,text="BREW",bg="black",fg="black",font=("Arial","18"),command=generate_drink)
brew_btn.place(x=200,y=200)


display_lbl=Label(root,text="",bg="#B4E4E4",fg="#6587D2",font=("Arial","20","bold"))
display_lbl.place(x=50,y=250)

root.mainloop()
