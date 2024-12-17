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

HeadingLabel = Label(TopHeadingFrame,text='Medicin Management System - Add Medicine',font=('Helvetica',18),fg='orange',bg='black')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)

MidFrame = Frame(window,width=600,bd=1)
MidFrame.pack(side=TOP)

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists 'medicine' (MedicineName text,MedicineID int,Brand text,ChemicalComponent text,MFG_Date int, EXP_Date text,Price int)""")
conn.commit()

medicine_name = StringVar()
medicine_name.set('')

medicine_nameLabel = Label(MidFrame,text='Medicine Name',font=('Helvetica',16),fg='yellow',bg='black')
medicine_nameLabel.grid(row=0,column=0,padx=10,pady=10)
medicine_nameTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=medicine_name)
medicine_nameTextBox.grid(row=0,column=1,padx=10,pady=10)

medicine_id = IntVar()
medicine_id.set('')

medicine_idLabel = Label(MidFrame,text='Medicine ID',font=('Helvetica',16),fg='yellow',bg='black')
medicine_idLabel.grid(row=1,column=0,padx=10,pady=10)
medicine_idTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=medicine_id)
medicine_idTextBox.grid(row=1,column=1,padx=10,pady=10)

brand = StringVar()
brand.set('')

brandLabel = Label(MidFrame,text='Brand Name',font=('Helvetica',16),fg='yellow',bg='black')
brandLabel.grid(row=2,column=0,padx=10,pady=10)
brandTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=brand)
brandTextBox.grid(row=2,column=1,padx=10,pady=10)

chemical = StringVar()
chemical.set('')

chemicalLabel = Label(MidFrame,text='Chemical Component',font=('Helvetica',16),fg='yellow',bg='black')
chemicalLabel.grid(row=3,column=0,padx=10,pady=10)
chemicalTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=chemical)
chemicalTextBox.grid(row=3,column=1,padx=10,pady=10)

mfg = StringVar()
mfg.set('')

mfgLabel = Label(MidFrame,text='MFG Date',font=('Helvetica',16),fg='yellow',bg='black')
mfgLabel.grid(row=4,column=0,padx=10,pady=10)
mfgTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=mfg)
mfgTextBox.grid(row=4,column=1,padx=10,pady=10)

exp = StringVar()
exp.set('')

expLabel = Label(MidFrame,text='EXP Date',font=('Helvetica',16),fg='yellow',bg='black')
expLabel.grid(row=5,column=0,padx=10,pady=10)
expTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=exp)
expTextBox.grid(row=5,column=1,padx=10,pady=10)

price = IntVar()
price.set('')

priceLabel = Label(MidFrame,text='Price',font=('Helvetica',16),fg='yellow',bg='black')
priceLabel.grid(row=6,column=0,padx=10,pady=10)
priceTextBox = Entry(MidFrame,font=('Helvetica',16),textvariable=price)
priceTextBox.grid(row=6,column=1,padx=10,pady=10)

def add():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute(
        """insert into 'medicine' 
        (MedicineName,MedicineID,Brand,ChemicalComponent,MFG_Date,EXP_Date,Price) values (?,?,?,?,?,?,?)""",
        (str(medicine_name.get()),str(medicine_id.get()),str(brand.get()),str(chemical.get()),str(mfg.get()),str(exp.get()),str(price.get())))
    conn.commit()
    if cursor.rowcount>0:
        msg.showinfo('ADD MEDICINE','New Medicine added',icon='info')
    else:
        msg.showinfo('Error','New Medicine not added',icon='warning')

def back():
    window.destroy()
    import home

add_btn = Button(MidFrame,text='ADD',command=add,font=('Helvetica',18),fg='black',bg='green')
add_btn.grid(row=7,column=1,padx=10,pady=10)


back_btn = Button(MidFrame,text='BACK',command=back,font=('Helvetica',18),fg='black',bg='red')
back_btn.grid(row=8,column=1,padx=10,pady=10)

window.mainloop()








window.mainloop()