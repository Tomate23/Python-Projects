from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

txt = Label(window, text="Eleccion")
txt.grid(row=1, column=0)
select = StringVar()

rad1 = Radiobutton(window,text='First', value=1, variable=select)
rad1.grid(column=0, row=0)

rad2 = Radiobutton(window,text='Second', value=2, variable=select)
rad2.grid(column=1, row=0)

rad3 = Radiobutton(window,text='Third', value=3, variable=select)
rad3.grid(column=2, row=0)

def chose():
    num = select.get()
    msg = "has elegido: " + num
    txt.configure(text=msg)

boton = Button(window, text="Submit!", command=chose)
boton.grid(row=2, column=0)

window.mainloop()


