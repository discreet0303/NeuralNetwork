# from src.gui import UiLayout

# if __name__ == "__main__":
#     UiLayout.UiLayout()

from tkinter import *

import tkinter

top = Tk()

mb =  Menubutton ( top, text = "condiments", relief = RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label = "mayo",
                          variable = mayoVar )
mb.menu.add_checkbutton ( label = "ketchup",
                          variable = ketchVar )

mb.pack()
top.mainloop()