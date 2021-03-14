import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile



root= tk.Tk()

canvas= tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3, rowspan=3)

logo= Image.open('image.jpg')
logo= ImageTk.PhotoImage(logo)
logo_label= tk.Label(image=logo)
logo_label.Image= logo
logo_label.grid(column=1, row=0)

instruction= tk.Label(text="Select a pdf file on your computer to extract all its text", font="Calibri")
instruction.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("loading....")
    file= askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("PDF File", "*.pdf")])
    if file:
       read_pdf= PyPDF2.PdfFileReader(file)
       page= read_pdf.getPage(0)
       page_content= page.extractText()
     
       text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
       text_box.insert(1.0, page_content)
       text_box.grid(column=1, row=3)
       text_box.tag_configure("center", justify="center")
       text_box.tag_add("center", 1.0, "end")
       text_box.grid(column=1, row=3)


browse_text= tk.StringVar()
browse_btn= tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Calibri", bg="#8b0000", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas= tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)



root.mainloop()
