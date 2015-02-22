import os
import pickle
import sys
sys.path.append("C:\Users\Ahmet\Desktop\Fobby")
from FOBBY import *
proj_load_order = False

def first_time_set(first_time):
    if first_time == True:
        first_time = False

def load_proj(first_time,proj_path,proj_load_order):
        if first_time or proj_load_order:
            Open = tkMessageBox.showinfo(title = "Load Project", message = "Please go into your CoilSnake project directory and select the 'Project.snake' file!")
            temp = askopenfilename()
            if temp[-13:] == 'Project.snake':
                proj_path = temp
            else:
                Invalid = tkMessageBox.showwarning(title = "Invalid", message = "Please make sure you selected 'Project.snake'.")
                
def load_proj_order():
        global proj_load_order
        proj_load_order = True
        load_proj()
        proj_load_order = False
        

def loader(needle, haystack):
        for element in haystack:
            if not isinstance(element, list):
                if element == needle:
                    return True
            else:
                found = loader(needle, element)
                if found:
                    return element[0]

def register_registerer(theme,proj_path,first_time):
        register = [[theme,'theme'],[proj_path,'proj_path'],[first_time,'first_time']]
        print register
        return register



