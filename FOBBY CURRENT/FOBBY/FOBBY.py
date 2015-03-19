import os, os.path, Tkinter, random, re, pickle, atexit, tkMessageBox, sys, PIL
from PIL import Image, ImageTk
from tkFileDialog import *
sys.path.append(os.getcwd() +"\modules")
import battle_action, adress_index, item_config, enemies, npc_config, shop_config, default_name
from betterwidgets import *
import flavors as f

def main():
    #Global Variables
    widgets = {
        "main":{
        	"pointer": None
            "default":{
            "current" : True;
            "buttons":{},"labels":{},"messageboxes":{},
            "entries" : {},"listboxes" : {},"scalers" : {},
            "radiobuttons" : {},"checkbuttons" : {},"frames" : {}
            }
        }
    }

    register = {}

    global theme
    theme = 0
    global last_proj
    last_proj = ""
    global first_time
    first_time = True
    global proj_load_order
    proj_load_order = False
    global unc_path
    unc_path = ""
    
    #Various Procedure # 1
    def set_theme():
        global theme
        #global register
        if theme == 0:
            f_0()
        elif theme == 1:
            f_1()
        elif theme == 2:
            f_2()
        elif theme == 3:
            f_3()
        elif theme == 4:
            f_4()

    def first_time_set():
        #global register
        global first_time
        if first_time == True:
            first_time = False
        register_registerer()

    def load_proj_order():
        #global register
        global proj_load_order
        proj_load_order = True
        open_proj()
        proj_load_order = False
        

    def open_proj():
        #global register
        global last_proj
        global proj_load_order
        global first_time
        global unc_path
        print "BEN"
        if first_time or proj_load_order:
            if len(os.listdir(os.getcwd()+"/saves")) == 0:
                emptymess = tkMessageBox.showwarning(title = "Saves Folder Is Empty", message = "You have no existing project. You can either make a new one or import one. A valid is project is any folder with a file called project_info!")
            else:
                openproj = tkMessageBox.showwarning(title = "Open Project", message = "Please choose a project")
            temp = askdirectory()
            if "project_info" in os.listdir(temp):
                last_proj = temp
                register_registerer()
                
                FOBBYTEXT.set(random.choice(["Gee, it sure is borange around here!","Thank you for using me",
                                                   "WOOHOO! I can't wait to play EarthBound on Virtual Console"]) +"""
Currently Loaded Project: """ + str( register['last_proj'] ) + """
Default Project Directory: """ + str(unc_path))
            else:
                Invalid = tkMessageBox.showwarning(title = "Invalid", message = "This folder has no project_info in it.")
                last_proj = ""
                register_registerer()
                FOBBYTEXT.set("Hey you need to load a project!")
                                                  
        
    #def loader(needle, haystack):
    #    for element in haystack:
    #        if not isinstance(element, list):
    #            if element == needle:
    #                return True
    #        else:
    #            found = loader(needle, element)
    #            if found:
    #                return element[0]

    def register_registerer():
        #global register
        global theme
        global last_proj
        global first_time
        global unc_path
        print theme,last_proj,first_time
        register = {'theme':theme,'last_proj':last_proj,'first_time':first_time}

        if (str( register['last_proj'] )) != "" :
            open_proj_inf = open( (str( register['last_proj'] )) + "\project_info",'rb')
            unc_path = open_proj_inf.read()[22:]        
            open_proj_inf.close()

        if unc_path != "":
            try:
                buttonify(widgets,root,default,"Battle Action",300,300,b_action_but)
                buttonify(widgets,root,default,"Adress List",300,332,index_but)
                buttonify(widgets,root,default,"General Items",300,364,item_config_but)
                buttonify(widgets,root,default,"Enemy Configuration",300,396,enemy_config_but)
                buttonify(widgets,root,default,"NPC Configuration",300,428,npc_config_but)
                buttonify(widgets,root,default,"Shops",300,460,store_but)
                buttonify(widgets,root,default,"Default Names",300,492,name_but)
                set_theme()
            except:
                print "Quit"

    def save_f():
        #global register
        register_registerer()
        outFile = open(os.getcwd() + '\FobbySave.txt', 'wb')
        pickle.dump(register, outFile)
        print register
        outFile.close()

    def load_f():        
        #global register
        global theme
        global last_proj
        global first_time
        
        if os.path.exists(os.getcwd() + "/" + 'FobbySave.txt'):
            with open(os.getcwd() + '\FobbySave.txt', 'rb') as in_file:
                register = pickle.load(in_file)
                theme = register['theme']
                last_proj = register['last_proj']
                first_time = register['first_time']
        else:
            theme = 0
            last_proj = ""
            first_time = True

    #Flavor Configurer

    def f_0():
        global theme
        f.f(widgets,'black','white','grey','white')
        theme = 0

    def f_1():
        global theme
        f.f(widgets,'black','spring green','dark green','spring green')
        theme = 1

    def f_2():
        global theme
        f.f(widgets,'black','hot pink','deep pink','hot pink')
        theme = 2

    def f_3():
        global theme
        f.f(widgets,'black','lemon chiffon','yellow','lemon chiffon')
        theme = 3

    def f_4():
        global theme
        f.f(widgets,'black','dark orange','chocolate','dark orange')
        theme = 4

    # Various Preocedures
    def quitp():
        exit(0)

    #Root Window
    class MainMenu(Frame):
	    root = Tkinter.Tk()
	    root.geometry('1200x900')
	    root.title('Fobby')
	    widgets["main"]["default"]['pointer'] = root
	    FOBBYTEXT = Tkinter.StringVar()
	    proj_name = Tkinter.StringVar()
	    uncompiled_directory = Tkinter.StringVar()
	    
	    welcome = Tkinter.Label(root,textvariable = FOBBYTEXT)
	    welcome.place(x=250,y=250)
	    labels.append(welcome)

	    fob_i = Image.open(os.getcwd()+"\modules\Fobby.png")
	    fob_to = ImageTk.PhotoImage(fob_i)
	    fobby_pic = Tkinter.Label(image=fob_to)
	    fobby_pic.image = fob_to
	    fobby_pic.place(x=250,y=300)
	    labels.append(fobby_pic)

    #Battle Menu
    def b_action_but():
        if "battle_action" not in [w[1] for w in w_2]:
            battle_action.b_action(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,unc_path,last_proj)
            set_theme()
        else:
            battle_action.call_battle_action(w_2)


    # Index Menu
    def index_but():
        if "adress_index" not in [w[1] for w in w_2]:
            adress_index.adress_index(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,unc_path,last_proj)
            set_theme()
        else:
            adress_index.call_adress_index(w_2)

    #General Item Configuration
    def item_config_but():
        if "item_config" not in [w[1] for w in w_2]:
            item_config.item_config(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,unc_path,last_proj)
            set_theme()
        else:
            item_config.call_item_config(w_2)

    #Enemy Configuration
    def enemy_config_but():
        if "Enemy Config" not in [w[1] for w in w_2]:
            enemies.enemies_c(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,unc_path,last_proj)
            set_theme()
        else:
            enemies.call_enemy_config(w_2)

    #NPC Config
    def npc_config_but():
        if "npc config" not in [w[1] for w in w_2]:
            npc_config.npcs_c(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,unc_path,last_proj)
            set_theme()
        else:
            npc_config.call_npc_config(w_2)

    #Stores
    def store_but():
        if "shops" not in [w[1] for w in w_2]:
            shop_config.make_shop(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,unc_path,last_proj)
            set_theme()
        else:
            shop_config.call_store(w_2)

    #Names
    def name_but():
        if "name_skip" not in [w[1] for w in w_2]:
            default_name.name_s(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,unc_path,last_proj)
            set_theme()
        else:
            default_name.call_name(w_2)

    def new_project():
        #global register
        global theme
        global last_proj
        
        new_proj_win = Tkinter.Toplevel()
        windows.append(new_proj_win)

        pro_name_get = Tkinter.Entry(master = new_proj_win, textvariable = proj_name)
        entries.append(pro_name_get)
        pro_name_get.place(x=32,y=32)
        
        pro_name_label = Tkinter.Label(master = new_proj_win, text = "Project Name:")
        labels.append(pro_name_label)
        pro_name_label.place(x=32,y=0)

        unc_get_lab = Tkinter.Label(master = new_proj_win, text = "Base '.snake' file:")
        labels.append(unc_get_lab)
        unc_get_lab.place(x=32,y=64)
        
        unc_get_ent = Tkinter.Entry(master = new_proj_win, textvariable = uncompiled_directory)
        entries.append(unc_get_ent)
        unc_get_ent.place(x=32,y=96)

        def load_unc():
            Open = tkMessageBox.showinfo(title = "Load Project", message = "Please go into your CoilSnake project directory and select the 'Project.snake' file!")
            temp = askopenfilename()
            if temp[-13:] == 'Project.snake':
                uncompiled_directory.set(temp)
            else:
                invalid = tkMessageBox.showwarning(title = "Sorry Invalid", message = "Select Project.snake")

        unc_get_but = Tkinter.Button(master = new_proj_win, text ="Open", command = load_unc)
        buttons.append(unc_get_but)
        unc_get_but.place(x=32,y=128)

        def save_n_pro():
            if uncompiled_directory.get()[-13:] != 'Project.snake':
                invalid = tkMessageBox.showwarning(title = "Sorry Invalid", message = "This is not a valid Project.snake file")
            try:
                os.makedirs(os.getcwd()+"\saves\\"+proj_name.get())
                info = open(os.getcwd()+"\saves\\"+proj_name.get()+"\project_info", 'wb')
                info.write("Uncompiled Directory: " +  uncompiled_directory.get())
                info.close()
                new_proj_win.destroy()
                           

            except WindowsError:
                if proj_name.get() in os.listdir(os.getcwd()+"\saves"):
                    ask_proj_overwrite = tkMessageBox.askyesno(title = "Sorry Invalid", message = "This project already exists, do you wish to overwrite it?")
                    if ask_proj_overwrite:
                        try:
                            os.rmdir(os.getcwd()+"\saves\\"+proj_name.get())
                            
                            os.makedirs(os.getcwd()+"\saves\\"+proj_name.get())
                            info = open(os.getcwd()+"\saves\\"+proj_name.get()+"\project_info", 'wb')
                            info.write("Uncompiled Directory: " +  uncompiled_directory.get())
                            info.close()
                            new_proj_win.destroy()
                            
                        except OSError:
                            try:
                                for f in os.listdir(os.getcwd()+"\saves\\"+proj_name.get()):
                                    os.remove(os.getcwd()+"\saves\\"+proj_name.get()+"\\"+f)
                                os.rmdir(os.getcwd()+"\saves\\"+proj_name.get())
                            except WindowsError:
                                invalid = tkMessageBox.showwarning(title = "A file is in use", message = "Please close the file and then try again...")
                                return

                            os.makedirs(os.getcwd()+"\saves\\"+proj_name.get())
                            info = open(os.getcwd()+"\saves\\"+proj_name.get()+"\project_info", 'wb')
                            info.write("Uncompiled Directory: " +  uncompiled_directory.get())
                            info.close()
                            new_proj_win.destroy()
                            

                else:
                    invalid = tkMessageBox.showwarning(title = "Sorry Invalid", message = "Invalid characters")


        confirm_but = Tkinter.Button(master = new_proj_win, text ="Create Project", command = save_n_pro)
        buttons.append(confirm_but)
        confirm_but.place(x=32,y=160)
        
        set_theme()
        

    # File Menu
    menubar = Tkinter.Menu(root)
    root.config(menu = menubar)

    filemenu = Tkinter.Menu(menubar,tearoff = 0)
    configmenu = Tkinter.Menu(menubar,tearoff = 0)
    infomenu = Tkinter.Menu(menubar,tearoff = 0)
    thememenu = Tkinter.Menu(menubar,tearoff = 0)

    menu_attach(filemenu,[["New Project",new_project],["Open Project",load_proj_order],["Save",save_f],["Quit",quitp]])
    menu_attach(configmenu,[["Set CoilSnake Location",empty],["Set Project Directory",load_proj_order]])
    menu_attach(infomenu,[["How To Use",empty],["I NEED MORE HELP!",empty],["Version",empty]])
    menu_attach(thememenu,[["Plain",f_0],["Mint",f_1],["Strawberry",f_2],["Banana",f_3],["Peanut",f_4]])

    cascade([["File",filemenu],["Configuration",configmenu],["Information",infomenu],["Flavor",thememenu]])

    def firsties():
        global first_time
        if first_time:
            FOBBYTEXT.set("""Welcome to Fobby. I think this is your first time here.
Go ahead and load a project from the saves folder or just make a new one from
the file menu!""")
            open_proj()
            first_time_set()
        else:
            open_proj_inf = open(str(loader('last_proj', register)) + "\project_info",'rb')
            unc_path = open_proj_inf.read()[22:]        
            open_proj_inf.close()
            FOBBYTEXT.set(random.choice(["Gee, it sure is borange around here!","Thank you for using me",
                                                   "WOOHOO! I can't wait to play EarthBound on Virtual Console"]) +"""
Currently Loaded Project: """ + str(loader('last_proj', register)) + """
Default Project Directory: """ + str(unc_path))

    #Save - Load
    set_theme()

    load_f()
    register_registerer()

    firsties()
    
    set_theme()

    register_registerer()
    #Lex - Looper

    Tkinter.mainloop()
    atexit.register(save_f())
    
#At Quit

if __name__ == "__main__":
    main() 
    
