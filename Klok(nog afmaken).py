from tkinter import *
from time import strftime
root = Tk()

root.geometry("500x500")
root.resizable(0,0)
root.title('Klok')

Label(root,text = 'Klok', font ='arial 30 bold').pack() # hier wordt de grootte van de tekst weergegeven

def time():
    tijd = strftime('%H:%M:%S %p')
    lettertype.config(text = tijd)
    lettertype.after(10, time)

lettertype = Label(root, 
            font = ('arial', 40, 'bold'),
            pady=150,
            foreground = 'green'
            )

lettertype.pack()

time()

mainloop()