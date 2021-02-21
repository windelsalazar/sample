import tkinter as tk
from tkinter import *
import psycopg2
from tkinter import messagebox 

conn = psycopg2.connect(
            host = "localhost" ,  
            database = "crud",
            user = "postgres",
            password = "windel1325")


cur = conn.cursor()

def add_employee():
     if ent.get() == '' or ent2.get() == '' or ent3.get() == '' or ent4.get() == '':
        messagebox.showerror('Ooops!',  'Please input all fields!')
        return

     ename = ent.get()
     branch = ent2.get()
     designation = ent3.get()
     salary = ent4.get()
     db = "INSERT INTO emp VALUES (%s, %s, %s, %s)"
     cur.execute(db, (ename, branch, designation, salary))
     print("Employee Added")
     conn.commit()
     return True


root = Tk()

frm1 = Frame(root)
frm1.pack(side=tk.LEFT, padx=20)

var1 = StringVar()
ename = StringVar()
var2 = StringVar()
branch = StringVar()
var3 = StringVar()
designation = StringVar()
var4 = IntVar()
salary = IntVar()

label1 = Label(frm1, textvariable=var1)
var1.set("Employee Name")
label1.grid(row=0, column=1)

ent = Entry(frm1, textvariable=ename)
ename.set("")
ent.grid(row=0, column=2)

label2 = Label(frm1, textvariable=var2)
var2.set("Branch Name")
label2.grid(row=1, column=1)

ent2 = Entry(frm1, textvariable=branch)
branch.set("")
ent2.grid(row=1, column=2)

label3 = Label(frm1, textvariable=var3)
var3.set("Designation")
label3.grid(row=2, column=1)

ent3 = Entry(frm1, textvariable=designation)
designation.set("")
ent3.grid(row=2, column=2)

label4 = Label(frm1, textvariable=var4)
var4.set("Salary")
label4.grid(row=3, column=1)

ent4 = Entry(frm1, textvariable=salary)
salary.set("")
ent4.grid(row=3, column=2)

btn = Button(frm1, text= "Add Employee", command=add_employee)
btn.grid(row=5, column=2)


root.title("Employee Form")
root.geometry("400x350")
root.resizable(False, False)

root.mainloop()
