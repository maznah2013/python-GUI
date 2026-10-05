from tkinter import *

def convert():
    miles=float(text_box.get())
    km=miles*1.6
    display_lbl.config(text=f"{miles}miles is equal to {km}km")

root=Tk()
root.geometry("450x300")
root.configure(bg="#E7A2D8")
root.title("Distance Convertor")

heading_lbl=Label(root,text="Distance Convertor",bg="#E7A2D8",fg="#E872AD",font=("Verdana",25,"bold"))
heading_lbl.pack()

input_lbl=Label(root,text="Enter the distance in miles: ",bg="#E7A2D8",fg="#C14282",font=("Verdana",18,"normal"))
input_lbl.pack(pady=20)

text_box=Entry(root,font=("Verdana",20,"normal"),justify="center")
text_box.pack(pady=10)

convert_btn=Button(root,text="Convert",background="white",foreground="black",font=("Verdana",20,"bold"),command=convert)
convert_btn.pack(pady=10)

display_lbl=Label(root,text="",background="#E7A2D8",fg="#C14282",font=("Verdana",18,"normal"))
display_lbl.pack(pady=10)

root.mainloop()