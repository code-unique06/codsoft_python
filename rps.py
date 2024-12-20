from tkinter import *
import random

window = Tk()
window.title("Rock Paper Scissors game")
window.geometry("540x540")
window.maxsize(545,545)

window.config(bg = "Antiquewhite")

l1 = Label(window,text="Rock Paper Scissors Game",font=("Times New Roman",20),fg = "Blue",justify="center",bg = "Aqua",width = 20,height=2)
l1.place(x=100,y=30)

l6 = Label(window,text="Choose either of 3 choices in player choice",font = ("Calibri",12),fg = 'black')
l7 = Label(window,text="Based upon your choice and computer choice , winner will be decided",font = ("Calibri",12),fg = 'black')

l6.place(x=5,y=120)
l7.place(x=5,y=150)

l1 = Label(window,text="Your Choice :",font = ("Arial",15),fg = "Black")
l1.place(x=5,y=200)

b1 = Button(window,text="Rock",font  = ("Arial",15),bg = "blue",fg = "yellow",bd=1,command=lambda:determine_winner("Rock"))
b1.place(x=60,y=270)

b2 = Button(window,text="Paper",font=("Arial",15),bg = "blue",fg="yellow",bd =1,command=lambda:determine_winner("Paper"))
b2.place(x=210,y=270)

b3 = Button(window,text="Scissors",font=("Arial",15),bg= "blue",fg = "yellow",bd=1,command=lambda:determine_winner("Scissors"))
b3.place(x=360,y=270)


l3 = Label(window,text="Computer choice :",font = ("Arial",15),fg = "Black")
l3.place(x=5,y=350)

l5 = Label(window,font=("arial",15),fg = "yellow",bg = "blue")
l5.place(x=200,y=380)


l4  = Label(window,font = ("Arial",15),fg = "Black",bg = "antiquewhite")
l4.place(x=180,y=450)



def determine_winner(p_choice):
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)
    l5.config(text=comp_choice)
    
    if p_choice == comp_choice:
        l4.config(text="It's a tie!")
    elif (p_choice == "Rock" and comp_choice == "Scissors") or \
         (p_choice == "Paper" and comp_choice == "Rock") or \
         (p_choice == "Scissors" and comp_choice == "Paper"):
        l4.config(text ="You win!")
    else:
        l4.config(text="Computer wins!")  
    

window.mainloop()