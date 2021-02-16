from tkinter import *
from tkinter import messagebox
from psycopg2 import *

#Create window object
project = Tk()

def populate_list():
   print('Populate')



def add_item():
    if employee_text.get() == '' or branch_text.get() == '' or designation_text.get() == '' or salary_text.get() == '':
        messagebox.showerror('Ooops!',  'Please input all fields!')
        return
    project_list.delete(0, END)
    project_list.insert(END, (employee_text.get(), branch_text.get(), designation_text.get(), salary_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    global selected_item
    index = project_list.curselection()[0]
    selected_item = project_list.get(index)
  
    employee_entry.delete(0, END)
    employee_entry.insert(END, selected_item[0])
    branch_entry.delete(0, END)
    branch_entry.insert(END, selected_item[1])
    designation_entry.delete(0, END)
    designation_entry.insert(END, selected_item[2])
    salary_entry.delete(0, END)
    salary_entry.insert(END, selected_item[3])

def remove_item():
    delt = messagebox.askquestion("Confirm", "Do you want to remove this?")
    project_list.delete(0, END)
   

    

def update_item():
    print('Update')

def clear_text():
    employee_entry.delete(0, END)
    branch_entry.delete(0, END)
    designation_entry.delete(0, END)
    salary_entry.delete(0, END)

    
    
project.title("CRUD")
project.geometry("700x350")


#Employee Label
employee_text = StringVar()
employee_label = Label(project, text= 'Employee Name', font= ('bold', 10), pady=20)
employee_label.grid (row=0, column=0)
employee_entry = Entry(project, textvariable= employee_text)
employee_entry.grid (row=0, column=1)

#Branch Label
branch_text = StringVar()
branch_label = Label(project, text= 'Branch Name', font= ('bold', 10))
branch_label.grid (row=1, column=0)
branch_entry = Entry(project, textvariable= branch_text)
branch_entry.grid (row=1, column=1)

#Designation Label
designation_text = StringVar()
designation_label = Label(project, text= 'Designation', font= ('bold', 10))
designation_label.grid (row=0, column=3, sticky=W)
designation_entry = Entry(project, textvariable= designation_text)
designation_entry.grid (row=0, column=4)

#Salary Label
salary_text = StringVar()
salary_label = Label(project, text= 'Salary', font= ('bold', 10))
salary_label.grid (row=1, column=3, sticky=W)
salary_entry = Entry(project, textvariable= salary_text)
salary_entry.grid (row=1, column=4)

#Listbox
project_list = Listbox(project, height= 10, width= 60, border=0)
project_list.grid (row=3, column=0, columnspan=3, rowspan=6, padx=20, pady=20)

project_list.bind('<<ListboxSelect>>', select_item)

#Create Scrollbox
scrollbar= Scrollbar(project)
scrollbar.grid(row=3, column=3)

#Set scroll to listbox
project_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=project_list.yview)

#Create Buttons
button_add= Button (project, text='Add',  width=12, command=add_item)
button_add.grid(row=2, column=0, pady=20)

button_remove= Button (project, text='Remove', width=12, command=remove_item)
button_remove.grid(row=2, column=1)

button_update= Button (project, text='Update', width=12, command=update_item)
button_update.grid(row=2, column=2)

button_clear= Button (project, text='Clear Input', width=12, command=clear_text)
button_clear.grid(row=2, column=3)




populate_list()


#Start program
project.mainloop()
