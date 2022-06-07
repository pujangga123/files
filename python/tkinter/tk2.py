from tkinter import *

def salam_klik():
    text_pesan = "Halo " + nama.get()
    pesan.config(text=text_pesan)

win = Tk()

win.geometry("300x200") 
win.title("Form Utama") 

Label(win,text="Nama").pack()
nama = Entry(win)
nama.pack()

Label(win,text="Umur").pack()
umur = Entry(win)
umur.pack()

tombol = Button(win, text="Salam", command=salam_klik)
tombol.pack()

pesan = Label(win)
pesan.pack()

win.mainloop()
