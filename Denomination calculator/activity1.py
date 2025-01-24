from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("app_img.jpg")

upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text='Hey User!, Welcome to Denomination Counter Application')

label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination counter?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Let's get started!", command=msg, bg='brown', fg='white')
button1.place(x=260, y=360)

def topwin():
    top = TopLevel()
    top.title("Denomination Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination",bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')