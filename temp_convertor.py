from tkinter import *

def convert():
    celsius=float(text_box.get())
    f=(celsius*9/5)+32
    display_lbl.config(text=f"{celsius}°C is equal to {f}°F")

root=Tk()
root.geometry("450x300")
root.configure(bg="#A2D3E7")
root.title("Temperature Convertor")

heading_lbl=Label(root,text="Temperature Convertor",bg="#A2D3E7",fg="#5052A3",font=("Verdana",25,"bold"))
heading_lbl.pack()

input_lbl=Label(root,text="Enter the temperature in celsius: ",bg="#A2D3E7",fg="#4242C1",font=("Verdana",18,"normal"))
input_lbl.pack(pady=20)

text_box=Entry(root,font=("Verdana",20,"normal"),justify="center")
text_box.pack(pady=10)

convert_btn=Button(root,text="Convert",background="white",foreground="black",font=("Verdana",20,"bold"),command=convert)
convert_btn.pack(pady=10)

display_lbl=Label(root,text="",background="#A2D3E7",fg="#5052A3",font=("Verdana",18,"normal"))
display_lbl.pack(pady=10)

root.mainloop()