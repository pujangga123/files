from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from member import Member

# dictionary 'database' untuk mensimulasikan database
database = {}
member_aktif = Member(database)

# kosongkan list
def list_clear():
    list1.delete(0,END)

# menambahkan/edit data di database
def db_update():
    member_aktif.id = id.get()
    member_aktif.nama = nama.get()
    member_aktif.jenis_keanggotaan = jenis_keanggotaan.get()    
    member_aktif.trainer = trainer.get()
    member_aktif.update()

    db_show()

    # menampilkan messagebox
    messagebox.showinfo("Info","Data berhasil ditambahkan")
    list_reload() # update tampilan list1

# fungsi menampilkan detail data sesuai parameter show_id
def db_show():

    id.delete(0,END) # hapus text id pada textbox
    id.insert(0,member_aktif.id)  # tampilkan id (var_id) pada textbox

    nama.delete(0,END)
    nama.insert(0,member_aktif.nama)

    jenis_keanggotaan.set(member_aktif.jenis_keanggotaan)

    kedatangan.config(text=member_aktif.kedatangan)
    iuran.config(text=member_aktif.iuran)
    tanggal_pembayaran.config(text=member_aktif.tanggal_pembayaran)

    trainer.delete(0,END)
    trainer.insert(0,member_aktif.trainer)

# fungsi yang di eksekusi ketika double klik
def list_doubleclick(event):
    var_id = list1.get(list1.curselection()[0]) # membaca ID yang di klik user pada list1
    member_aktif.load(var_id)
    db_show()


def db_new():
    id.delete(0,END)
    nama.delete(0,END)
    kedatangan.config(text="0")
    tanggal_pembayaran.config(text="")
    trainer.delete(0,END)
    iuran.config(text="")
    jenis_keanggotaan.set('reguler')

def db_bayar():
    member_aktif.bayar()

def db_tambah_kedatangan():
    member_aktif.tambah_kedatangan()

    db_show()

# refresh list
def list_reload():
    list_clear()  # bersihkan list1

    # masukan ulang setiap data pada database ke list1
    for i in database:
        list1.insert(END,i)

win = Tk()
win.geometry("300x600")     # set ukuran window
win.title("Data Mahasiswa") # set caption/judul window

list1 = Listbox(win)
list1.bind("<Double-1>",list_doubleclick)  # init function yang akan di eksekusi ketika double klik di list
list1.pack()

Label(win,text="ID").pack()
id = Entry(win)
id.pack()

Label(win,text="Nama").pack()
nama = Entry(win)
nama.pack()

Label(win,text="Jenis Keanggotaan").pack()
jenis_keanggotaan = Combobox(win, values=["reguler", "vip"], state="readonly")
jenis_keanggotaan.pack()

Label(win,text="Iuran").pack()
iuran = Label(win)
iuran.pack()

Label(win,text="Jumlah kedatangan").pack()
kedatangan = Label(win)
kedatangan.pack()

Label(win,text="Tanggal Pembayaran").pack()
tanggal_pembayaran = Label(win)
tanggal_pembayaran.pack()

Label(win,text="Trainer").pack()
trainer = Entry(win)
trainer.pack()

Button(win,text="New", command=db_new).pack()
Button(win,text="Update", command=db_update).pack()
Button(win,text="Tambah Kedatangan", command=db_tambah_kedatangan).pack()
Button(win,text="bayar", command=db_bayar).pack()

list_reload() # update tampilan list1

win.mainloop()