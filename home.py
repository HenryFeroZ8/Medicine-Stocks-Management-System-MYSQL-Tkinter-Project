import sqlite3
from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')

reg_img = PhotoImage(file='homepik.png')

bg_label = Label(window,image=reg_img)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

window.title("Medicin Management System")
window.iconbitmap('logo.ico')

TopHeadingFrame = Frame(window, width= 700,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - Home',font=('Helvetica',18),fg='orange',bg='black')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame = Frame(window,width = 600,bd=1)
MidFrame.pack(side=TOP)

def add():
    window.destroy()
    import add_medicine

def view():
    window.destroy()
    import view_medicine

def search():
    window.destroy()
    import search_medicine

def delete():
    window.destroy()
    import delete_medicine

add_btn = Button(MidFrame,text="ADD MEDICINE",command=add,font=("helvetica",18),fg="black",bg="green")
add_btn.grid(row=0,column=1,padx=10,pady=10)

view_btn = Button(MidFrame,text="VIEW MEDICINE",command=view,font=("helvetica",18),fg="black",bg="green")
view_btn.grid(row=1,column=1,padx=10,pady=10)

search_btn = Button(MidFrame,text="SEARCH MEDICINE",command=search,font=("helvetica",18),fg="black",bg="green")
search_btn.grid(row=2,column=1,padx=10,pady=10)

delete_btn = Button(MidFrame,text="DELETE MEDICINE",command=delete,font=("helvetica",18),fg="black",bg="green")
delete_btn.grid(row=3,column=1,padx=10,pady=10)

def logout():
    window.destroy()
    import login

login_btn = Button(MidFrame,text="LOGOUT",command=logout,font=("helvetica",18),fg="black",bg="red")
login_btn.grid(row=4,column=2,padx=10,pady=10)

window.mainloop()