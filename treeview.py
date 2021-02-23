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
    if q.get() == '':
        messagebox.showerror('Ooops!',  'Please input text to search!')
        return
    q2 = q.get()
    query = "Select employee_id, employee, branch, designation FROM tree WHERE employee LIKE '%"+q2+"%' OR branch LIKE '%"+q2+"%' OR designation LIKE '%"+q2+"%'"
    cur.execute(query)
    rows = cur.fetchall()
    update(rows)

def clear_text():
    query = "Select employee_id, employee, branch, designation FROM tree"
    cur.execute(query)
    rows = cur.fetchall()
    ent1.delete(0, END)
    update(rows)

def getrow(event):
    rowid = tree.identify_row(event.y)
    item = tree.item(tree.focus())
    e1.set(item['values'][0])
    e2.set(item['values'][1])
    e3.set(item['values'][2])
    e4.set(item['values'][3])


def update_employee():
    return True

def add_employee():
    if e1.get() == '' or e2.get() == '' or e3.get() == '' or e4.get() == '':
        messagebox.showerror('Ooops!',  'Please input all fields!')
        return
    employee_id = e1.get()
    employee = e2.get()
    branch = e3.get()
    designation = e4.get()
    query = "INSERT INTO tree(employee_id, employee, branch, designation) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (employee_id, employee, branch, designation))
    clear_text()
    conn.commit()
    return True



def delete_employee():
    if e1.get() == '' or e2.get() == '' or e3.get() == '' or e4.get() == '':
        messagebox.showerror('Ooops!',  'Please choose item to delete!')
        return
    employee_id = e1.get()
    if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this employee?"):
     query = "DELETE FROM tree WHERE employee_id = " +employee_id
     cur.execute(query)
     conn.commit()
     clear_text()
    else:
        return True
     

   
conn = psycopg2.connect(
            host = "localhost" ,  
            database = "sample",
            user = "postgres",
            password = "windel1325")


cur = conn.cursor()

win = Tk()
win.configure(bg='red')
q= StringVar()
e1= StringVar()
e2= StringVar()
e3= StringVar()
e4= StringVar()


wrapper1 = LabelFrame(win, text= "Employee List")
wrapper2 = LabelFrame(win, text= "Search")
wrapper3 = LabelFrame(win, text="Employee Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

tree_scroll = Scrollbar(wrapper1)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="6", yscrollcommand=tree_scroll.set)
tree.pack()

tree_scroll.configure(command=tree.yview)

tree.heading(1, text="Employee ID")
tree.heading(2, text="Employee Name")
tree.heading(3, text="Branch")
tree.heading(4, text="Designation")

tree.bind('<Double 1>', getrow)

query = "Select employee_id, employee, branch, designation from tree"
cur.execute(query)
rows = cur.fetchall()
update(rows)


label1 = Label(wrapper2, text="Search")
label1.pack(side=tk.LEFT, padx=10)
ent1 = Entry(wrapper2, textvariable=q)
ent1.pack(side=tk.LEFT, padx=6)
button1 = Button(wrapper2, text="Search", command=search)
button1.pack(side=tk.LEFT, padx=6)
button2 = Button(wrapper2, text="Clear Search", command=clear_text)
button2.pack(side=tk.LEFT, padx=6)

label2 = Label(wrapper3, text="Employee ID")
label2.grid(row=0, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=e1)
ent2.grid(row=0, column=1, padx=5, pady=3)

label3 = Label(wrapper3, text= "Employee Name")
label3.grid(row=1, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, textvariable=e2)
ent3.grid(row=1, column=1, padx=5, pady=3)

label4 = Label(wrapper3, text= "Branch")
label4.grid(row=2, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, textvariable=e3)
ent4.grid(row=2, column=1, padx=5, pady=3)

label5 = Label(wrapper3, text= "Designation")
label5.grid(row=3, column=0, padx=5, pady=3)
ent5 = Entry(wrapper3, textvariable=e4)
ent5.grid(row=3, column=1, padx=5, pady=3)

btn_update = Button(wrapper3, text="Update", command=update_employee)
btn_add = Button(wrapper3, text="Add New", command=add_employee)
btn_delete = Button(wrapper3, text="Delete", command=delete_employee)

btn_add.grid(row=4,column=0, padx=5, pady=3)
btn_update.grid(row=4, column=1, padx=5, pady=3)
btn_delete.grid(row=4, column=2, padx=5, pady=3)









win.title("Employee Table")
win.geometry("800x700")
























win.mainloop()
