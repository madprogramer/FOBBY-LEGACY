import Tkinter
def buttonify(buttons,window,name,coord_1,coord_2,com):
    name = Tkinter.Button(window, text=str(name), command = com)
    name.place(x = coord_1, y = coord_2)
    buttons.append(name)
