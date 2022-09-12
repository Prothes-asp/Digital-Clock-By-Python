from tkinter import*
from tkinter.ttk import*
from time import strftime


Root = Tk()
Root.title('Python Digital Clock')

def time():
    String = strftime('%H:%M:%S %p')
    label.config(text=String)
    label.after(1000,time)

label = Label(Root,font=('ds-digital',80),background='black', foreground='cyan')
label.pack(anchor='center')


time()
mainloop()

