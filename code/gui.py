"""
THIS IS CURRENTLY NOT BEING USED

"""
from tkinter import *
import tkinter as ttk

root = Tk()
root.title("Horoscope Matcher")
global choices 
meshalist = []
rishabalist = []
mithunalist = []
karkadagalist = []
simhalist = []
kanyalist = []
thulalist = []
vrichigalist = []
dhanusulist = []
makaralist = []
kumbhalist = []
meenalist = []
# Add a grid
mainframe = Frame(root, bg='white', width=50, height=50, padx=1, pady=1)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(9, weight = 1)
mainframe.rowconfigure(9, weight = 1)

cells = {}
for row in range(4):
    for column in range(4):
        if row in [1,2] and column in [1,2]:
            cell = Frame(mainframe, bg='white', highlightbackground="white",
                        highlightcolor="white", highlightthickness=1,
                        width=200, height=200,  padx=1,  pady=1)
            cell.grid(row=row, column=column)
            cells[(row, column)] = cell
        else:
            cell = Frame(mainframe, bg='white', highlightbackground="black",
                        highlightcolor="black", highlightthickness=1,
                        width=200, height=200,  padx=1,  pady=1)
            cell.grid(row=row, column=column)                  
            cells[(row, column)] = cell

# Create a Tkinter variable
mesha = StringVar(root)
rishaba = StringVar(root)
mithuna = StringVar(root)
karkadaga = StringVar(root)
simha = StringVar(root)
kanya = StringVar(root)
thula = StringVar(root)
vrichiga = StringVar(root)
dhanusu = StringVar(root)
makara = StringVar(root)
kumbha = StringVar(root)
meena = StringVar(root)

# Dictionary with options
choices = ['empty','sevvai','sukran','budhan','chandran','suryan', 'sani','rahu','ketu','guru']

meshaMenu = OptionMenu(mainframe, mesha, *choices)
rishabaMenu = OptionMenu(mainframe, rishaba, *choices)
mithunaMenu = OptionMenu(mainframe, mithuna, *choices)
karkadagaMenu = OptionMenu(mainframe, karkadaga, *choices)
simhaMenu = OptionMenu(mainframe, simha, *choices)
kanyaMenu = OptionMenu(mainframe, kanya, *choices)
thulaMenu = OptionMenu(mainframe, thula, *choices)
vrichigaMenu = OptionMenu(mainframe, vrichiga, *choices)
dhanusuMenu = OptionMenu(mainframe, dhanusu, *choices)
makaraMenu = OptionMenu(mainframe, makara, *choices)
kumbhaMenu = OptionMenu(mainframe, kumbha, *choices)
meenaMenu = OptionMenu(mainframe, meena, *choices)
meshaMenu.grid(row = 0, column = 1)
rishabaMenu.grid(row = 0, column = 2)
mithunaMenu.grid(row = 0, column = 3)
karkadagaMenu.grid(row = 1, column = 3)
simhaMenu.grid(row = 2, column = 3)
kanyaMenu.grid(row = 3, column = 3)
thulaMenu.grid(row = 3, column = 2)
vrichigaMenu.grid(row = 3, column = 1)
dhanusuMenu.grid(row = 3, column = 0)
makaraMenu.grid(row = 2, column = 0)
kumbhaMenu.grid(row = 1, column = 0)
meenaMenu.grid(row = 0, column = 0)

# on change dropdown value
def mesha_dropdown(*args):
    meshalist.append( mesha.get() )
# on change dropdown value
def rishaba_dropdown(*args):
    rishabalist.append( rishaba.get() )
# on change dropdown value
def mithuna_dropdown(*args):
    mithunalist.append( mithuna.get() )
# on change dropdown value
def karkadaga_dropdown(*args):
    karkadagalist.append( karkadaga.get() )
# on change dropdown value
def simha_dropdown(*args):
    simhalist.append( simha.get() )
# on change dropdown value
def kanya_dropdown(*args):
    kanyalist.append( kanya.get() )
# on change dropdown value
def thula_dropdown(*args):
    thulalist.append( thula.get() )
# on change dropdown value
def vrichiga_dropdown(*args):
    vrichigalist.append( vrichiga.get() )
# on change dropdown value
def dhanusu_dropdown(*args):
    dhanusulist.append( dhanusu.get() )
# on change dropdown value
def makara_dropdown(*args):
    makaralist.append( makara.get() )
# on change dropdown value
def kumbha_dropdown(*args):
    kumbhalist.append( kumbha.get() )
# on change dropdown value
def meena_dropdown(*args):
    meenalist.append( meena.get() )
    

# link function to change dropdown
mesha.trace('w', mesha_dropdown)
rishaba.trace('w', rishaba_dropdown)
mithuna.trace('w', mithuna_dropdown)
karkadaga.trace('w', karkadaga_dropdown)
simha.trace('w', simha_dropdown)
kanya.trace('w', kanya_dropdown)
thula.trace('w', thula_dropdown)
vrichiga.trace('w', vrichiga_dropdown)
dhanusu.trace('w', dhanusu_dropdown)
makara.trace('w', makara_dropdown)
kumbha.trace('w', kumbha_dropdown)
meena.trace('w', meena_dropdown)

button = Button(mainframe, text="\n  SUBMIT  \n", command=root.destroy)
button.grid(row = 2, column = 2)

root.mainloop()
