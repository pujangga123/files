from tkinter import *
from tkinter import messagebox

# dictionary 'database' untuk mensimulasikan database
database = {}

# kosongkan list
def list_clear():
    list1.delete(0,END)

# menambahkan/edit data di database
def db_add():
    var_nim = nim.get()    # .get() --> membaca text yang diinput user pada textbox
    var_nama = nama.get()
    var_nilai = nilai.get()

    # memasukan/update data dengan key var_nim
    database[var_nim] = {
        "nama":var_nama,
        "nilai":var_nilai
    }
    # menampilkan messagebox
    messagebox.showinfo("Info","Data berhasil ditambahkan")
    list_reload() # update tampilan list1

# fungsi yang di eksekusi ketika double klik
def list_doubleclick(event):
    var_nim = list1.get(list1.curselection()[0]) # membaca NIM yang di klik user pada list1

    var_nama = database[var_nim]['nama'] # ambil 'nama' untuk NIM yang sesuai var_nim
    var_nilai = database[var_nim]['nilai']

    nim.delete(0,END) # hapus text NIM pada textbox
    nim.insert(0,var_nim)  # tampilkan NIM (var_nim) pada textbox

    nama.delete(0,END)
    nama.insert(0,var_nama)

    nilai.delete(0,END)
    nilai.insert(0,var_nilai)

# hapus entry dari database
def db_del():
    var_nim = list1.get(list1.curselection()[0])  # ambil NIM yang dipilih user pada list1
    del database[var_nim]  # hapus data sesuai NIM (var_nim) dari database
    messagebox.showinfo("Info","Data berhasil dihapus")  # tampilkan messagebox
    list_reload()  # update tampilan list1

# refresh list
def list_reload():
    list_clear()  # bersihkan list1

    # masukan ulang setiap data pada database ke list1
    for i in database:
        list1.insert(END,i)

win = Tk()
win.geometry("300x400")     # set ukuran window
win.title("Data Mahasiswa") # set caption/judul window

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

list_reload() # update tampilan list1

win.mainloop()