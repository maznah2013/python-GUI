from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("500x800")
root.configure(bg="white")
root.title("Multiplication Table")


heading_lbl=Label(root, text="Multiplication Table",bg="white",fg="#1C2130",font=("Arial","20","bold"))
heading_lbl.pack(pady=10)

number_lbl=Label(root,text="Number Range: ",bg="white",fg="#1C2130",font=("Arial",18))
number_lbl.place(x=20,y=50)

#combo box creation
num=IntVar()
number_box=ttk.Combobox(root,textvariable=num,width=6,state="readonly")
number_box.place(x=200,y=50)
number_box["values"]=tuple(range(101))

#radio button creation
end_val=IntVar()
r10=Radiobutton(root,text="10",variable=end_val,value=10,bg="white",fg="black")
r10.place(x=350,y=50)
r20=Radiobutton(root,text="20",variable=end_val,value=20,bg="white",fg="black")
r20.place(x=350,y=100)
r30=Radiobutton(root,text="30",variable=end_val,value=30,bg="white",fg="black")
r30.place(x=350,y=150)
end_val.set(10)

generate_btn=Button(root,text="GENERATE",bg="#3027BA",fg="black",font=("Arial","18"))
generate_btn.place(x=200,y=200)

display_lbl=Label(root,text="",bg="white",fg="black",font=("Arial","18"))
display_lbl.place(x=200,y=250)

root.mainloop()