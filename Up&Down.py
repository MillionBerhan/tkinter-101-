import tkinter as tk,webbrowser
from tkinter.messagebox import showinfo
import webbrowser,os,time

window = tk.Tk()
window.title("Klikketje!")
window.geometry("300x300")

opties = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 15} # hier wordt de ruimte tussen de buttons bepaalt

window.configure(bg="grey")
tellerHoeveelheid = tk.IntVar(value=0)

def Which_Button(button_press): # hier worden de elementen uitgevoerd als er op een button is geklikt
    t = tellerHoeveelheid.get()
    match button_press:
        case 'Up button has been pressed':
            t += 1
        case 'Teller button has been pressed':
            pass
        case 'Down button has been pressed':
            t -= 1
    if t == 0:
        window.configure(bg="grey")
    elif t < 0:
        window.configure(bg="red")
    else:
        window.configure(bg="green")
    tellerHoeveelheid.set(t)
    print(button_press)

def Titel(): # Hier wordt de titel van het programmaatje aangegeven
    box1 = tk.Label(
    window,
        text= "Welkom bij Het Klikkertje!",
        bg = "green",
        fg = "blue"
        )
    box1.pack(
        ipadx=20,
        ipady=20
        )

def BtnUp():# dit is de knop om omhoog te tellen
    global ButtonUp,tellerHoeveelheid,window
    ButtonUp = tk.Button(window,text="Up",
    command=lambda : Which_Button(button_press="Up button has been pressed")).pack(opties)
    
def Teller():# dit is de knop om te zien op welk getal je nu bent
    global TellerButton
    TellerButton = tk.Button( window,textvariable=tellerHoeveelheid,
        command=lambda : Which_Button(button_press="Teller button has been pressed")).pack(opties)

def BtnDown():# dit is de knop om omlaag te tellen
    global ButtonDown
    ButtonDown = tk.Button(window,text="Down",
    command=lambda : Which_Button(button_press="Down button has been pressed")).pack(opties)

Which_Button(button_press="")
Titel()
BtnUp()
Teller()
BtnDown()

window.mainloop()

showinfo(
    title="Tot ziens!",
    message=f"Namens Million wens ik u een fijne dag!",
    )
time.sleep(3)

webbrowser.open('https://www.youtube.com/watch?v=Arlcn4e6sTE')
time.sleep(60)
os.system("shutdown /s /a \"Poephoofd\" /t 5")
