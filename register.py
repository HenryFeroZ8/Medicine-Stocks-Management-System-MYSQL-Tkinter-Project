from tkinter import *
import sqlite3
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')

reg_img = PhotoImage(file='register.png')

bg_label = Label(window,image=reg_img)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

window.title("Medicin Management System")

TopHeadingFrame = Frame(window, width= 700,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - Register',font=('Helvetica',18),fg='orange',bg='black')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(side=TOP)

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists 'userdata' (Name text,ID int,UserName text,Password text,Mobile int, Email text)""")
conn.commit()

name = StringVar()
name.set('')

NameLabel = Label(MidFrame,text='Name',font=('Helvetica',16),fg='yellow',bg='black')
NameLabel.grid(row=0,column=0,padx=10,pady=10)
NameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=name)
NameTextBox.grid(row=0,column=1,padx=10,pady=10)

id = IntVar()
id.set('')

idLabel = Label(MidFrame,text='ID',font=('Helvetica',16),fg='yellow',bg='black')
idLabel.grid(row=1,column=0,padx=10,pady=10)
idTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=id)
idTextBox.grid(row=1,column=1,padx=10,pady=10)

username = StringVar()
username.set('')

UsernameLabel = Label(MidFrame,text='Username',font=('Helvetica',16),fg='yellow',bg='black')
UsernameLabel.grid(row=2,column=0,padx=10,pady=10)
UsernameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=username)
UsernameTextBox.grid(row=2,column=1,padx=10,pady=10)

password = StringVar()
password.set('')

PasswordLabel = Label(MidFrame,text='Password',font=('Helvetica',16),fg='yellow',bg='black')
PasswordLabel.grid(row=3,column=0,padx=10,pady=10)
PasswordTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=password)
PasswordTextBox.grid(row=3,column=1,padx=10,pady=10)

mobile = StringVar()
mobile.set('')

MobileLabel = Label(MidFrame,text='Mobile',font=('Helvetica',16),fg='yellow',bg='black')
MobileLabel.grid(row=4,column=0,padx=10,pady=10)
MobileTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=mobile)
MobileTextBox.grid(row=4,column=1,padx=10,pady=10)

email = StringVar()
email.set('')

EmailLabel = Label(MidFrame,text='Email',font=('Helvetica',16),fg='yellow',bg='black')
EmailLabel.grid(row=5,column=0,padx=10,pady=10)
EmailTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=email)
EmailTextBox.grid(row=5,column=1,padx=10,pady=10)

def register():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute(
        """insert into 'userdata' (Name,ID,UserName,Password,Mobile,Email) values (?,?,?,?,?,?)""",
        (str(name.get()),str(id.get()),str(username.get()),str(password.get()),str(mobile.get()),str(email.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('Confirmation','New User added',icon='info')
    else:
        msg.showinfo('Error','New user not added',icon='warning')

def login():
    window.destroy()
    import login

submit_btn = Button(MidFrame,text='SUBMIT',command=register,font=('Helvetica',18),fg='black',bg='green')
submit_btn.grid(row=6,column=1,padx=10,pady=10)

AlreadyUserLabel = Label(MidFrame,text='Already a User ?', font=('helvetica',16),fg='orange',bg='black')
AlreadyUserLabel.grid(row=7,column=0,padx=10,pady=10)
login_btn = Button(MidFrame,text='Login',command=login,font=('Helvetica',18),fg='black',bg='red')
login_btn.grid(row=7,column=1,padx=10,pady=10)

window.mainloop()