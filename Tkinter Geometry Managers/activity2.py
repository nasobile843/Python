from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='#d0efff')

lbl1 = Label(frame, text = "Full Name", bg="#3895D3", fg='white', width=12 )
lbl2 = Label(frame, text = "Email Id", bg="#3895D3", fg='white', width=12 )
lbl3 = Label(frame, text = "Enter Password", bg="#3895D3", fg='white', width=12 )

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    greet = "Hey"+name
    message = "\nCongradulations for your new accont!"
    

