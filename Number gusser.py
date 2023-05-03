from tkinter import *
from tkinter import messagebox
from tkinter import Button
def c():
    box=Tk()
    box.geometry('250x250')
    box.title('num guesser')
    return box

def evennum(box):
    box.destroy()
    box=c()
    main = Label(text="Is the number divisible by 4")
    main.place(x=60,y=50)
    yes=Button(box,text='yes',command=lambda:true([4,8],box),bd=5,width=4)
    yes.place(x=68,y=150)
    no=Button(box,text='no',command=lambda:true([2,6],box),bd=5,width=4)
    no.place(x=150,y=150)

def oddnum(box):
    box.destroy()
    box=c()
    box.geometry('300x250')
    main = Label(text="After adding 5 what does your number becomes")
    main.place(x=20,y=50)
    sing=Button(box,text='single digit',command=lambda:false([1,3],box),bd=5,width=10)
    sing.place(x=15,y=150)
    doub=Button(box,text='double digit',command=lambda:false([7,9],box),bd=5,width=10)
    doub.place(x=105,y=150)
    ten=Button(box,text="it's a 10",command=lambda:detect(5,box),bd=5,width=10)
    ten.place(x=195,y=150)

def true(n,box):
    box.destroy()
    box=c()
    box.geometry('300x250')
    main = Label(text="After multiplying with 2 your number is?")
    main.place(x=25,y=50)
    yes=Button(box,text='single digit',command=lambda:detect(n[0],box),bd=5,width=10)
    yes.place(x=50,y=150)
    no=Button(box,text='double digit',command=lambda:detect(n[1],box),bd=5,width=10)
    no.place(x=170,y=150)

def false(n,box):
    box.destroy()
    box=c()
    box.geometry('270x250')
    main = Label(text="remainder of your number after dividing by 3")
    main.place(x=20,y=50)
    yes=Button(box,text='0',command=lambda:detect(n[1],box),bd=5,width=4)
    yes.place(x=90,y=150)
    no=Button(box,text='1',command=lambda:detect(n[0],box),bd=5,width=4)
    no.place(x=150,y=150)

def detect(n,box):
    box.destroy()
    messagebox.showinfo('your number is',n)

messagebox.showinfo('Think of any number I will try to guess your number','shall we start')
messagebox.showwarning('number selection','your number should be a single digit real number')

box=c()

main = Label(text="square of your number is?")
main.place(x=63,y=40)
odd=Button(box,text="Even",command=lambda:evennum(box),bd=5,width=4)
odd.place(x=68,y=150)
even=Button(box,text='Odd',command=lambda:oddnum(box),bd=5,width=4)
even.place(x=150,y=150)

box.mainloop()
