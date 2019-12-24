from tkinter import *
import tkinter as ttk

root = Tk()
root.title("Horoscope Matcher")

# # Add a grid
# mainframe = Frame(root)
# mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
# mainframe.columnconfigure(0, weight = 1)
# mainframe.rowconfigure(0, weight = 1)
# mainframe.pack(pady = 100, padx = 100)

# # Create a Tkinter variable
# tkvar = StringVar(root)

# # Dictionary with options
# choices = {'sevvai','sukran','budhan','chandran','suryan', 'sani','rahu','ketu','guru'}
# tkvar.set('empty') # set the default option

# popupMenu = OptionMenu(mainframe, tkvar, *choices)
# Label(mainframe, text="Mesham").grid(row = 1, column = 1)
# popupMenu.grid(row = 2, column =1)

# # on change dropdown value
# def change_dropdown(*args):
#     print( tkvar.get() )

# # link function to change dropdown
# tkvar.trace('w', change_dropdown)

# root.mainloop()

# create all of the main containers
center = Frame(root, bg='white', width=900, height=900, padx=3, pady=3)

# layout all of the main containers
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(9, weight=1)
center.grid(row=1, sticky="nsew")

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)
cells = {}
tkvar_list = []
iter = 0
for row in range(4):
    for column in range(4):
        if row in [1,2] and column in [1,2]:
            cell = Frame(center, bg='white', highlightbackground="white",
                        highlightcolor="white", highlightthickness=1,
                        width=200, height=200,  padx=3,  pady=3)
            cell.grid(row=row, column=column)
            cells[(row, column)] = cell
        else:
            # Create a Tkinter variable
            tkvar = StringVar(root)
            tkvar_list.append(tkvar)
            # Dictionary with options
            choices = ['sevvai','sukran','budhan','chandran','suryan', 'sani','rahu','ketu','guru']
            tkvar.set('empty') # set the default option
            cell = Frame(center, bg='white', highlightbackground="black",
                        highlightcolor="black", highlightthickness=1,
                        width=200, height=200,  padx=3,  pady=3)
            cell.grid(row=row, column=column)                  

            popupMenu = OptionMenu(center, tkvar_list[iter], *choices)
            popupMenu.grid(row = row, column =column)
            # # checkbutton widget 
            # c1 = Checkbutton(center, text = "Lagnam") 
            # c1.grid(row = row, column = column, sticky = W, columnspan = 2) 
            # on change dropdown value
            def change_dropdown(*args):
                print( tkvar.get() )

            # link function to change dropdown
            tkvar.trace('w', change_dropdown())

            cells[(row, column)] = cell
            iter = iter+1

root.mainloop()