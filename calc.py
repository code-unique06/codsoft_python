from tkinter import *

window = Tk()
window.geometry("360x540")
window.configure(bg = "white")
window.maxsize(360,540)
window.title("Calculator")

# fucntions

calc = ""

def clear():
    global calc
    calc=""
    e1.config(text=calc)

def show(value):
    global calc 
    calc = calc+value
    e1.config(text=calc)

def result():
    global calc
    res = ""
    if calc != "":
            res = eval(calc)
    else:
            res = "error"
            calc=""
    e1.config(text=res)

#space for presenting teh result of required operation
e1 = Label(window,font=("Calibri",32),bg="grey",fg="black",width=15,bd=0)
e1.place(x=6,y=20)

#row 1

b1 = Button(window,text="C",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:clear())
b1.place(x=3,y=88)

b2 = Button(window,text="/",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("/"))
b2.place(x=90,y=88)


b3 = Button(window,text="%",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("%"))
b3.place(x=180,y=88)


b4 = Button(window,text="x",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("*"))
b4.place(x=268,y=88)


#row 2
b5 = Button(window,text="7",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("7"))
b5.place(x=3,y=178)

b6 = Button(window,text="8",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("8"))
b6.place(x=90,y=178)

b7 = Button(window,text="9",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("9"))
b7.place(x=180,y=178)

b8 = Button(window,text="+",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("+"))
b8.place(x=268,y=175)


#row 4

b9 = Button(window,text="4",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("4"))
b9.place(x=3,y=266)

b10 = Button(window,text="5",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("5"))
b10.place(x=90,y=266)

b11 = Button(window,text="6",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("6"))
b11.place(x=180,y=266)

b18 = Button(window,text="-",font=15,bg="yellow",fg="red",width=7,height=3,command=lambda:show("-"))
b18.place(x=268,y=266)


#row 4


b12 = Button(window,text="1",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("1"))
b12.place(x=3,y=358)

b13 = Button(window,text="2",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("2"))
b13.place(x=90,y=358)

b14 = Button(window,text="3",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("3"))
b14.place(x=180,y=358)

b15 = Button(window,text="=",width=7,height=7,font=15,bg="yellow",fg="red",bd=1,command=lambda:result())
b15.place(x = 268,y=358)


#row 5
b16 = Button(window,text="0",width=15,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("0"))
b16.place(x=3,y=450)

b17 = Button(window,text=".",width=7,height=3,font=15,bg="yellow",fg="red",bd=1,command=lambda:show("."))
b17.place(x=180,y=450)
window.mainloop()