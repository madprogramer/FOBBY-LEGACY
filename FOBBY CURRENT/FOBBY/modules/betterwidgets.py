import Tkinter

def cascade(alist):
    for section in alist:
        menubar.add_cascade(label=section[0], menu =section[1])

def buttonify(widgets,window,tab,_id,coord_1,coord_2,com):
    b = Tkinter.Button(window, text=str(_id), command = com)
    b.place(x = coord_1, y = coord_2)
    widgets[_id][tab] = b

def menu_attach(men,alist):
    for section in alist:
        men.add_command(label=section[0], command=section[1])

def empty():
    pass

#def make_window():
