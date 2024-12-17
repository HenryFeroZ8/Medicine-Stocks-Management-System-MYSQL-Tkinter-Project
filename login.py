import sqlite3
from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')

reg_img = PhotoImage(file='reg.png')

bg_label = Label(window,image=reg_img)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

window.title("Medicin Management System")

TopHeadingFrame = Frame(window, width= 700,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - Login',font=('Helvetica',18),fg='orange',bg='black')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(side=TOP)

username = StringVar()
username.set('')

UsernameLabel = Label(MidFrame,text='Username',font=('Helvetica',16),fg='yellow',bg='black')
UsernameLabel.grid(row=0,column=0,padx=10,pady=10)
UsernameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=username)
UsernameTextBox.grid(row=0,column=1,padx=10,pady=10)

password = StringVar()
password.set('')

PasswordLabel = Label(MidFrame,text='Password',font=('Helvetica',16),fg='yellow',bg='black')
PasswordLabel.grid(row=1,column=0,padx=10,pady=10)
PasswordTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=password)
PasswordTextBox.grid(row=1,column=1,padx=10,pady=10)

def register():
    window.destroy()
    import register

def login():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""select * from 'userdata' where 
     UserName = ? and Password = ?""",(username.get(),password.get()))

    if len(list(cursor.fetchall())) > 0:
        msg.showinfo("Login Confirmation",'Login Success',icon='info')
        window.destroy()
        import home
    else:
        msg.showinfo('Login Error','User not found',icon='warning')


submit_btn = Button(MidFrame,text='Register',command=register,font=('Helvetica',18),fg='black',bg='green')
submit_btn.grid(row=3,column=1,padx=10,pady=10)

NotUserLabel = Label(MidFrame,text='Not a User yet ?', font=('helvetica',16),fg='orange',bg='black')
NotUserLabel.grid(row=3,column=0,padx=10,pady=10)

login_btn = Button(MidFrame,text='Login',command=login,font=('Helvetica',18),fg='black',bg='red')
login_btn.grid(row=2,column=1,padx=10,pady=10)




window.mainloop()