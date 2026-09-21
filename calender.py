from tkinter import *
import calendar

def show_cal():
    new_root=Tk()
    new_root.geometry("550x600")
    new_root.config(background="white")
    root.title("CALENDAR")

    year=int(year_input.get())
    cal_content=calendar.calendar(year)
    cal_lbl=Label(new_root,text=cal_content)
    cal_lbl.pack()

    new_root.mainloop()

root=Tk()
root.geometry("400x250")
root.config(background="#8DCCAD")
root.title("Calendar App")

heading_lbl=Label(root,text="Calendar",bg="#8DCCAD",fg="#CC6677",font=("Calibri",25,"bold"))
heading_lbl.pack()

year_lbl=Label(root,text="Enter your year: ",bg="#8DCCAD",fg="#FF597A",font=("Calibri",20,"bold"))
year_lbl.pack(padx=5,pady=5)

year_input=Entry(root,justify="center")
year_input.pack(padx=5,pady=5)

show_btn=Button(root,text="Show",bg="#F0AEC2",fg="#5A1E4A",font=("Calibri",20,"bold"),command=show_cal)
show_btn.pack(padx=5,pady=5)

exit_btn=Button(root,text="Exit",bg="#F6A39E",fg="#2A044A",font=("Calibri",20,"bold"),command=exit)
exit_btn.pack(padx=5,pady=5)

root.mainloop()