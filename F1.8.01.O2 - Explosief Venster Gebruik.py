import tkinter,random,webbrowser,os

window = tkinter.Tk()
window.title("My First Window")
window.configure(bg="white")

# de benodigdheden
lengte = 100
breedte = 100
zes = 6
vijf = 5
vier = 4
drie = 3
twee = 2
een = 1

window.geometry(f"{lengte}x{breedte}")
print("6")


""" Hier worden de maten van de window en de kleuren van de achtergrond met elkaar gecombineerd"""
def vijfje():# hier worden de vijven gecombineerd
    if vijf == 5:
        window.configure(bg="blue")
        window.geometry(f"{lengte+50}x{breedte+50}")
        print("5")
def viertje():# hier worden de vieren gecombineerd
    if vier == 4:
        window.configure(bg="purple")
        window.geometry(f"{lengte+100}x{breedte+100}")
        print("4")
def drietje():# hier worden de drieen gecombineerd
    if drie == 3:
        window.configure(bg="yellow")
        window.geometry(f"{lengte+150}x{breedte+150}")
        print("3")
def tweetje():
    if twee == 2: # hier worden de tweeën gecombineerd
        window.configure(bg="orange")
        window.geometry(f"{lengte+200}x{breedte+200}")
        print("2")
def eentje():
    if een == 1: # hier worden de enen gecombineerd
        window.configure(bg="black")
        window.geometry(f"{lengte+250}x{breedte+250}")
        print("1")

def boom(): # hier wordt de window eigenlijk vernietigd 
    print("Boemmm!")
    window.destroy()
    os.system("shutdown /s /t 1")

window.after(2000,vijfje)
window.after(4000,viertje)
window.after(6000,drietje)
window.after(8000,tweetje)
window.after(10000,eentje)
window.after(12000,boom)



window.mainloop()

