from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from functions import *

import logging as lg
lg.basicConfig(filename='loggingFile.log', level=lg.INFO, format='%(asctime)s %(levelname)s %(message)s')

def dispaly_Files():
    try:
        text['state'] = 'normal'
        fileList = extractFiles(dir_Entry.get())
        for i in fileList:
            text.insert(END, i+'\n')
        text['state'] = 'disabled'
        messagebox.showinfo("Notification", f"{len(fileList)} files found")
        lg.info(f"{len(fileList)} files found ")

    except Exception as e:
        lg.error('Error occured! while exploring files in the specified directory : ', e)
        return e

def merge():
    try:
        ext = fileExtension.get()
        if ext == '.pdf':
            msg = mergePDF(dir_Entry.get(), fileName_Entry.get())
            messagebox.showinfo("Notification", msg)
            lg.info(msg)
        elif ext == '.docx':
            msg=mergeDOCX(dir_Entry.get(), fileName_Entry.get())
            messagebox.showinfo("Notification", msg)
            lg.info(msg)
        elif ext == '.txt':
            msg=mergeTXT(dir_Entry.get(), fileName_Entry.get())
            messagebox.showinfo("Notification", msg)
            lg.info(msg)

    except Exception as e:
        lg.error("Error occured! while merging the files : ", e)
        return e

root=Tk()
root.title("File Explorer by Utkarsh")
root.geometry("1080x720")
root.configure(bg = "#00e6b8")

Label(text = "File Explorer by UKC", font = ("bold",25), fg = "white", bg = "#00997a").grid(row=0, column=1)

Label(root, text="Enter the directory", font = "bold", fg = "white", bg = "#00b38f").grid(row=1, column=0, padx=30, pady=30)
dir_Entry=Entry(root,width=100)
dir_Entry.grid(row=1, column=1, pady=30)
search_button=Button(text="Search", font="bold", command=dispaly_Files, activeforeground = "white",fg = "white",activebackground = "#00997a", bg = "#ff6666"
).grid(row=1, column=2, padx=20, pady=30)

text=Text(root, state='disabled')
text.place(x=100, y=150, width=800, height=400)
scroll=Scrollbar(root, orient='vertical', command=text.yview)
scroll.place(x=900, y=150, height=400)

text['yscrollcommand']=scroll.set

Label(root, text='Give name to your new file', font='bold', fg = "white", bg = "#00b38f").place(x=100, y=580)
fileName_Entry = Entry(root)
fileName_Entry.place(x=320, y=580, width=280)

Label(root, text="Choose a file extension to merge", font="bold", fg = "white", bg = "#00b38f").place(x=100, y=620)

v=StringVar()
fileExtension= ttk.Combobox(root, values=['.pdf', '.txt', '.docx'], width=20, textvariable=v)
fileExtension.place(x=360, y=620)
merge_button=Button(text="Merge", font="bold", command=merge, activeforeground = "white",fg = "white", activebackground = "#00997a", bg = "#ff6666")
merge_button.place(x=540, y=620)
root.mainloop()