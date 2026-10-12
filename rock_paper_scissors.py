from tkinter import *
import random

player_score=0
comp_score=0
options=["rock","paper","scissors"]

def player_wins():
    global player_score, comp_score
    winner_lbl.config(text="Player Wins!")
    player_score+=1
    players_score_lbl.config(text=f"Your score: {player_score}")
    computer_score_lbl.config(text=f"Computer score: {comp_score}")

def comp_wins():
    global player_score,comp_score
    winner_lbl.config(text="Computer Wins!")
    comp_score+=1
    players_score_lbl.config(text=f"Your score: {player_score}")
    computer_score_lbl.config(text=f"Computer score: {comp_score}")

def tie():
    global player_score,comp_score
    winner_lbl.config(text="Tie!")
    players_score_lbl.config(text=f"Your score: {player_score}")
    computer_score_lbl.config(text=f"Computer score: {comp_score}")

def computer_choice():
    return random.choice(options)

def player_choice(player_input):
    global player_score,comp_score
    print(player_input)
    player_choice_lbl.config(text=f"You selected: {player_input}")

    computer_input=computer_choice()
    print(computer_input)
    computer_choice_lbl.config(text=f"Computer selected: {computer_input}")

    if player_input==computer_input:
        tie()

    if player_input=="rock":
        if computer_input=="scissors":
            player_wins()
        elif computer_input=="paper":
            comp_wins()

    if player_input=="paper":
        if computer_input=="scissors":
            comp_wins()
        elif computer_input=="rock":
            player_wins()

    if player_input=="scissors":
        if computer_input=="rock":
            comp_wins()
        elif computer_input=="paper":
            player_wins()


root=Tk()
root.geometry("700x450")
root.configure(bg="#493A63")
root.title("Rock Paper Scissor")


heading_lbl=Label(root,text="Rock Paper Scissor",bg="#493A63",fg="white",font=("Calibri",30,"bold"))
heading_lbl.pack(pady=10)

winner_lbl=Label(root,text="Let the game begin!",bg="#493A63",fg="#B6DC96",font=("Calibri",20,"normal"))
winner_lbl.pack()


frame=Frame(root,bg="#493A63")
frame.pack()

player_options_lbl=Label(frame,text="Your options: ",bg="#493A63",fg="#768458",font=("Calibri",20,"normal"))
player_options_lbl.grid(row=0,column=0,pady=8)

rock_btn=Button(frame,text="Rock",background="#137C67",fg="#B185DE",font=("Calibri",20,"bold"),width=5,height=2,command=lambda: player_choice(options[0]))
rock_btn.grid(row=1,column=1,padx=5,pady=5)

paper_btn=Button(frame,text="Paper",bg="#78AE62",fg="#B8A9FF",font=("Calibri",20,"bold"),width=5,height=2,command=lambda: player_choice(options[1]))
paper_btn.grid(row=1,column=2,padx=5,pady=5)

scissors_btn=Button(frame,text="Scissors",bg="#43592C",fg="#9483DA",font=("Calibri",20,"bold"),width=5,height=2,command=lambda: player_choice(options[2]))
scissors_btn.grid(row=1,column=3,padx=5,pady=5)


score_lbl=Label(frame,text="Score: ",bg="#493A63",fg="#768458",font=("Calibri",20,"normal"))
score_lbl.grid(row=2,column=0)

player_choice_lbl=Label(frame,text="You selected: ",bg="#493A63",fg="#64D36F",font=("Calibri",20,"normal"))
player_choice_lbl.grid(row=3,column=1,pady=5)

players_score_lbl=Label(frame,text="Your score: ",bg="#493A63",fg="#64D36F",font=("Calibri",20,"normal"))
players_score_lbl.grid(row=3,column=2,pady=5)

computer_choice_lbl=Label(frame,text="Computer selected: ",bg="#493A63",fg="#64D36F",font=("Calibri",20,"normal"))
computer_choice_lbl.grid(row=4,column=1,pady=5)

computer_score_lbl=Label(frame,text="Computer score: ",bg="#493A63",fg="#64D36F",font=("Calibri",20,"normal"))
computer_score_lbl.grid(row=4,column=2,pady=5)

root.mainloop()