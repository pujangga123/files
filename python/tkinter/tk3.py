from tkinter import *
from tkinter import messagebox

# dictionary 'database' untuk mensimulasikan database
database = {}

# kosongkan list
def list_clear():
    list1.delete(0,list1.size())

# menambahkan/edit data di database
def db_add():
    var_nim = nim.get()
    var_nama = nama.get()
    var_nilai = nilai.get()
    database[var_nim] = {
        "nama":var_nama,
        "nilai":var_nilai
    }
    messagebox.showinfo("Info","Data berhasil ditambahkan")
    list_reload()

# fungsi yang di eksekusi ketika double klik
def list_doubleclick(event):
    var_nim = list1.get(list1.curselection()[0])
    var_nama = database[var_nim]['nama']
    var_nilai = database[var_nim]['nilai']

    nim.delete(0,END)
    nim.insert(0,var_nim)

    nama.delete(0,END)
    nama.insert(0,var_nama)

    nilai.delete(0,END)
    nilai.insert(0,var_nilai)

# hapus entry dari database
def db_del():
    var_nim = list1.get(list1.curselection()[0])
    del database[var_nim]    
    messagebox.showinfo("Info","Data berhasil dihapus")
    list_reload()

# refresh list
def list_reload():
    list_clear()
    for i in database:
        list1.insert(END,i)

win = Tk()
win.geometry("400x500")

list1 = Listbox(win)
list1.bind("<Double-1>",list_doubleclick)  # init function yang akan di eksekusi ketika double klik di list
list1.pack()

Label(win,text="NIM").pack()
nim = Entry(win)
nim.pack()

Label(win,text="Nama").pack()
nama = Entry(win)
nama.pack()

Label(win,text="Nilai").pack()
nilai = Entry(win)
nilai.pack()

Button(win,text="Clear", command=list_clear).pack()
Button(win,text="Add", command=db_add).pack()
Button(win,text="Delete", command=db_del).pack()

list_reload()

win.mainloop()