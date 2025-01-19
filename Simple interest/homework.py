from tkinter import *

def cal_si():
  si=(int(t1.get())*int(t2.get())*int(t3.get()))/100
  s.set(si)

def clearEntry():
  t1.delete(0,END)
  t2.delete(0,END)
  t3.delete(0,END)
  s.set(0)
  t1.focus_set()

def Me_Exit():
  main.destroy()
  
main=Tk()
main.title('Tkinter Simple interest calculator')

main.minsize(100,100)
main.geometry('540x180')
main.resizable(False,False)

ph=PhotoImage(file='tk.png')
main.iconphoto(False,ph)

main.configure(bg="#2299AA")


s=StringVar()


l1 = Label(main, bg="#99FF99",  text="Principal Amount:",font=('Arial',16)).grid(row=1)
l2 = Label(main, bg="#99ff99", text="Rate of Interest:",font=('Arial',16)).grid(row=2)
l3 = Label(main, bg="#99FF99", text="Duration (Years):",font=('Arial',16)).grid(row=3)

  
t1 = Entry(main,font=('Arial',16))
t1.grid(row=1, column=1)
t1.focus_set()
t2 = Entry(main,font=('Arial',16))
t2.grid(row=2, column=1)
t3 = Entry(main,font=('Arial',16))
t3.grid(row=3, column=1)

b1=Button(main,text="Compute SI", command=cal_si, font=('Arial',16)).grid(row=4,column=0)
b2=Button(main,text="Clear", command=clearEntry, font=('Arial',16)).grid(row=4,column=1)
b3=Button(main,text="Exit", command=Me_Exit, font=('Arial',16)).grid(row=4,column=2)

l4 = Label(main, text="Simple Interest:",font=('Arial',16)).grid(row=5)
t4 = Entry(main, state="disabled", textvariable=s, font=('Arial',16)).grid(row=5, column=1)