import sqlite3
from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

window = Tk()
window.geometry('900x600')

reg_img = PhotoImage(file='homepik.png')

bg_label = Label(window,image=reg_img)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

window.title("Medicin Management System")
window.iconbitmap('logo.ico')

TopHeadingFrame = Frame(window, width= 700,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text='Medicine Management System - View Medicine',font=('Helvetica',18),fg='red',bg='black')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame = Frame(window, width= 700,bd=1)
MidFrame.pack(side=TOP)

view_frame = Frame(window,bd=1)
view_frame.pack(side=TOP,fill=X)

tv = ttk.Treeview(view_frame,columns=('MedicineName','Medicineid','Brand','ChemicalComponent','MFG_Date','EFG_Date','Price'))
tv.heading('#1',text='MedicineName')
tv.heading('#2',text='MedicineID')
tv.heading('#3',text='Brand')
tv.heading('#4',text='Chemicals')
tv.heading('#5',text='MFG')
tv.heading('#6',text='EFG')
tv.heading('#7',text='Price')

tv.column('#0',width=0,stretch=0)
tv.column('#1',width=60)
tv.column('#2',width=60)
tv.column('#3',width=60)
tv.column('#4',width=60)
tv.column('#5',width=60)
tv.column('#6',width=60)
tv.column('#7',width=60)

tv.pack(fill=X)


conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("select * from 'medicine'")
data = cursor.fetchall()
for i in data:
      tv.insert("",'end',values=i)

def back():
    window.destroy()
    import home
conn.commit()
back_btn = Button(MidFrame,text='BACK',command=back,font=('Helvetica',18),fg='black',bg='red')
back_btn.grid(row=8,column=1,padx=10,pady=10)

window.mainloop()