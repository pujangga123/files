from tkinter import *

database = ["PHP","C++","Pascal","C#","Python","Java"]

def list_clear():
    list1.delete(0,list1.size())

def list_add():
    list1.insert(END,"Helo")

def list_del():
    list1.delete(list1.curselection()[0])

def list_reload():
    list_clear()
    for row in database:
        list1.insert(END,row)

def update():
    
    list_reload()

win = Tk()
win.geometry("400x500")

list1 = Listbox(win)
list1.pack()

Button(win,text="Clear", command=list_clear).pack()
Button(win,text="Add", command=list_add).pack()
Button(win,text="Delete", command=list_del).pack()

list_reload()

win.mainloop()