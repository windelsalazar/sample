from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2


def update(rows):
    tree.delete(*tree.get_children())
    for i in rows:
        tree.insert('', 'end', values=i)

def search():
    q2 = q.get()
    query = "Select employee_id, employee, branch, designation FROM tree WHERE employee LIKE '%"+q2+"%' OR branch LIKE '%"+q2+"%' OR designation LIKE '%"+q2+"%'"
    cur.execute(query)
    rows = cur.fetchall()
    update(rows)



conn = psycopg2.connect(
            host = "localhost" ,  
            database = "sample",
            user = "postgres",
            password = "windel1325")


cur = conn.cursor()

win = Tk()
win.configure(bg='red')
q= StringVar()

wrapper1 = LabelFrame(win, text= "Employee List")
wrapper2 = LabelFrame(win, text= "Search")
wrapper3 = LabelFrame(win, text="Employee Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

tree = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="6")
tree.pack()

tree.heading(1, text="Employee ID")
tree.heading(2, text="Employee Name")
tree.heading(3, text="Branch")
tree.heading(4, text="Designation")

query = "Select employee_id, employee, branch, designation from tree"
cur.execute(query)
rows = cur.fetchall()
update(rows)


label1 = Label(wrapper2, text="Search")
label1.pack(side=tk.LEFT, padx=10)
ent1 = Entry(wrapper2, textvariable=q)
ent1.pack(side=tk.LEFT, padx=6)
button1 = Button(wrapper2, text="Search", command=search)
button1.pack(side=LEFT, padx=6)








win.title("Employee Table")
win.geometry("800x700")
























win.mainloop()
