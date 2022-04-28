from queue import Empty
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import random

window = tk.Tk()
window.title("Grabbelton!")
window.geometry("500x500")
window.configure(bg="black")

# benodigdheden van de opdracht
grabbelton = ["Huis","Fles","Tesla Model X","Tesla Model S","Kaas","DaVinci schoolgebouw","5 Frikandellen","Cadeaukaart T.W.V €10","Magnetron","Appel"," 1 liter bakvet","Citroen","Danootje","Envelop","Frans toets","Gitaar","Hotelovernachting","Indirecte vrij trap","Jojo","Kanon","Lepel","Mint"] # dit is de lijst met de spullen die je kunt grabbelen
gegrabbeldespullen = [] # hier worden de gegrabbelde spullen in een lijst opgeslagen
#
opties = {'fill': 'both', 'padx': 100, 'pady': 100, 'ipadx': 15} # hiermee kun je de button verplaatsen

def TotaleItems():
    global WatErIsGePakt
    box1 = tk.Label(
        window,
        text= "Er zitten in totaal 22 items in de grabbelton!",
        bg = "green",
        fg = "blue"
        )

    box1.pack(
        ipadx=20,
        ipady=20
    )

def Gegrabbled():
    global WatErIsGePakt# hier wordt gegrabbeld
    if len (grabbelton) <1: # hier wordt gecheckt of de lijst leeg is als die leeg is dan krijg je een error te zien! (is wel net zo fijn :)
        print("Lijst is leeg!")
        showerror(
        title="Error",
        message="De grabbelton is leeg!\nStart het programma opnieuw op om weer te kunnen grabbelen!"
        )
    WatErIsGePakt = random.randrange(0, len(grabbelton)) # hier wordt iets gegrabbeld
    showinfo(
        title="Grabbelton",
        message=f"Gefeliciteerd, U heeft een {grabbelton[WatErIsGePakt]} gegrabbeld!"
    )
    grabbelton.pop(WatErIsGePakt)
    print(grabbelton)

tk.Button( # dit is de button voor de knop om te kunnen grabbelen
    window,
    text="Klik om te grabbelen!",
    command=Gegrabbled).pack(opties)



TotaleItems()


window.mainloop() # hier wordt het hele bestand uitgevoerd











