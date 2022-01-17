import tkinter
from tkinter import messagebox
from tkinter import *
import random

root = Tk()
root.geometry("700x700")
root.title("Jumbled Words")

words = ['anun', 'skauihk', 'tohypn', 'tgiubh', 'oolgeg', 'ebokofac', 'tiam', 'ruag', 'loco', 'remavl', 'mineme']
answers = ['nanu', 'kaushik', 'python', 'github', 'google', 'facebook', 'amit','gaur', 'cool', 'marvel', 'eminem']

num=random.randrange(0,len(words),1)
c=0
d=0
s = ""
l = Label(root)

def reset():
    global words, answers, num
    num=random.randrange(0,len(words),1)
    label.config(text = words[num])
    e1.delete(0, END)


def default():
    global words,answers,num
    label.config(text = words[num])


def checkans():
    global words, answers, num, c, d, s, l
    d=int(d)+1
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Congratulations", "It's the correct answer!!")
        c = int(c)+1
    else:
        messagebox.showerror("Sorry", "It's not the correct answer.")
    s = 'Score :' + str(c) + '/' + str(d)
    l.forget()
    l = Label(root, font=("Verdana", 20), text=s, bg="#000000", fg="#fff", )
    l.pack(side=LEFT)
    reset()


Label(root,text="JUMBLE WORD GAME", font=('arial', 40, 'bold'), bg = "yellow", fg = "green").pack()
label = Label(root, font = ('arial', 50, 'bold'), bg = "green", fg = "red")
label.pack(pady = 30,ipady=10,ipadx=10)

ans = StringVar() #defining that this is a string variable
e1 = Entry(root,font = ("Verdana",20),textvariable = ans,)
e1.pack(ipady=5,ipadx=5)

Button(root,text = "Check",font = ("Comic sans ms",20),width = 10,bg="#333945",fg="#45CE30",relief = GROOVE, command = checkans,).pack(pady = 40) #created a submit button
Button(root,text = "Reset",font = ("Comic sans ms",20),width = 10,bg="#777E8B",fg="#E1DA00",relief = GROOVE, command = reset).pack() #created a reset button
Button(root, text = "Exit", font=("Comic sans ms", 20), width=10, bg="black", fg="red", relief=GROOVE, command=root.quit).pack(pady = 40)

default()

root.mainloop()
