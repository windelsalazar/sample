from tkinter import *
from PIL import Image, ImageTk

win= Tk()
win.option_add("*Font", "30")
win.title("Login System")
win.geometry("550x500")
win.resizable(False, False)


label_member= Label(win, text="MEMBER LOGIN")
label_member.pack(side=TOP, padx=15)

label_user= Label(win, text="USERNAME")





win.mainloop()