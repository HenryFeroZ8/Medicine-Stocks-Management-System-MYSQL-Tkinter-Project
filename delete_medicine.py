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

HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - Delete Medicine ',font=('Helvetica',18),fg='orange',bg='black')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)