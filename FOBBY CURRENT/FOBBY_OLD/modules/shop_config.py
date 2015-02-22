import Tkinter, re, sys, yaml, tkMessageBox, os, unicodedata
sys.path.append(os.getcwd()[:-7])
import FOBBY
 
def make_shop(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,path,save_data):
    global stuff_loaded
    global update_selector
    update_selector = False
    stuff_loaded = False
    global searchable
    searchable = []
    ymls = []

    shops = []
    
    items_1 = []
    items_2 = []
    items_3 = []
    items_4 = []
    items_5 = []
    items_6 = []
    items_7 = []
    
    
    final_format = []
    selector_index = []
    loaded = tuple()
    
    item_1 = Tkinter.StringVar()
    item_2 = Tkinter.StringVar()
    item_3 = Tkinter.StringVar()
    item_4 = Tkinter.StringVar()
    item_5 = Tkinter.StringVar()
    item_6 = Tkinter.StringVar()
    item_7 = Tkinter.StringVar()

    item_1_n = Tkinter.StringVar()
    item_2_n = Tkinter.StringVar()
    item_3_n = Tkinter.StringVar()
    item_4_n = Tkinter.StringVar()
    item_5_n = Tkinter.StringVar()
    item_6_n = Tkinter.StringVar()
    item_7_n = Tkinter.StringVar()
    
    x_path = path[:-13]
    store_w = Tkinter.Toplevel()
    store_w.geometry('600x580+550+300')
    
    windows.append(store_w)
    w_2.append((store_w,"shops"))
    current = Tkinter.StringVar()
    
    global search_for_type
    search_for_type = Tkinter.StringVar()
    search_for_type.set("index")
    
    search_for_what = Tkinter.StringVar()
    
    global selected_type

    selected_type = Tkinter.StringVar()

    global add, dele, to_add
    add = False
    dele = False
    to_add = 0
    
    if os.path.exists(save_data+ "/store_table.yml"):
        stram = open(save_data + "/store_table.yml", "r")
    else:
        r_path = x_path + "store_table.yml"
        stram = open(r_path, "r")

    yml = yaml.load(stram)
    str_yml = str(yml)
    le = (re.findall(r'[0-9]+: {',str_yml))
    for l in range(len(le)):
        z = re.findall(r'[0-9]+',le[l])
        shops.append(int(le[l][0:(len(str(z[0])))]))
        items_1.append(yml[int(z[0])]['Item 1'])
        items_2.append(yml[int(z[0])]['Item 2'])
        items_3.append(yml[int(z[0])]['Item 3'])
        items_4.append(yml[int(z[0])]['Item 4'])
        items_5.append(yml[int(z[0])]['Item 5'])
        items_6.append(yml[int(z[0])]['Item 6'])
        items_7.append(yml[int(z[0])]['Item 7'])
        
    i = -1
    while i < (len(items_1)) -1:
        i += 1
        ymls.append((shops[i],items_1[i],items_1[i],items_2[i],items_3[i],items_4[i],items_5[i],items_6[i],items_7[i]))
    file.close(stram)
    searchable = [y for y in ymls]

    selection = Tkinter.Listbox(store_w)
    listboxes.append(selection)
    for l in range(len(ymls)):
        selection.insert(l, ymls[l][0])
    selection.place(x=16, y=64)

    selections_scroller = Tkinter.Scale(store_w, from_=0, to=len(ymls))
    selections_scroller.config(command=selection.yview)
    scalers.append(selections_scroller)
    selections_scroller.place(x=128 , y=80 )

    searcher = Tkinter.Entry(store_w, textvariable = search_for_what)
    entries.append(searcher)
    searcher.place(x=16, y=270)

    def selector():
        global stuff_loaded
        global loaded
        global pos
        global update_selector,add,dele,to_add
        global searchable

        searching_for = search_for_what.get()
        search_type = selected_type.get()
        selections_scroller.config(to=len(ymls))
        
        if stuff_loaded == True:
            replacer()
        try:
            pos = int(selection.curselection()[0])
        except IndexError:
            pos = -1

        if update_selector:
            try:
                temp_store_select = selection.curselection()[0]
                searchable_mod()
                print temp_store_select
                if search_type == "index":
                    if int(temp_store_select) > 0:
                        if add:
                            pos = int(searchable[int(temp_store_select) +1][0])
                            add = False
                        elif dele:
                            pos = int(searchable[int(temp_store_select) -1][0])
                            dele = False
                elif int(temp_store_select) == 0:
                    pos = -1
                else:
                    if add:
                        pos = to_add
                        add = False
                    elif dele:
                        pos = int(searchable[int(temp_store_select) -1][0])
                        dele = False
                selection.delete(0, "end")
                i = -1
                for no in ymls:
                    i += 1
                    selection.insert(i, no[0])
                
                loaded = ymls[[y[0] for y in ymls].index([s[0] for s in searchable][pos])]
                
                update_selector = False
            
            except IndexError or AttributeError:
                pos = 0
                print "Fail 1"

        loaded = ymls[[y[0] for y in ymls].index([s[0] for s in searchable][pos])]
        print loaded
        
        item_1.set(loaded[1])
        item_2.set(loaded[2])
        item_3.set(loaded[3])
        item_4.set(loaded[4])
        item_5.set(loaded[5])
        item_6.set(loaded[6])
        item_7.set(loaded[7])

        if os.path.exists(save_data+ "/item_configuration_table.yml"):
            strem = open(save_data+ "/item_configuration_table.yml", "r")
        else:
            r_path = x_path + "item_configuration_table.yml"
            strem = open(r_path, "r")

        items = yaml.load(strem)
        item_names = {item:items[item]["Name"] for item in items}
        print items
        print item_names
        strem.close()
        
        current.set("You are currently editing: " + str(loaded[0]))

        try:
            item_1_n.set(item_names[int(item_1.get())])
        except:
            item_1_n.set("Error: Unknown")

        try:
            item_2_n.set(item_names[int(item_2.get())])
        except:
            item_2_n.set("Error: Unknown")

        try:
            item_3_n.set(item_names[int(item_3.get())])
        except:
            item_3_n.set("Error: Unknown")

        try:
            item_4_n.set(item_names[int(item_4.get())])
        except:
            item_4_n.set("Error: Unknown")

        try:
            item_5_n.set(item_names[int(item_5.get())])
        except:
            item_5_n.set("Error: Unknown")

        try:
            item_6_n.set(item_names[int(item_6.get())])
        except:
            item_6_n.set("Error: Unknown")

        try:
            item_7_n.set(item_names[int(item_7.get())])
        except:
            item_7_n.set("Error: Unknown")
        stuff_loaded = True
        
    def find_pos(event):
        selector()
    selection.bind("<<ListboxSelect>>", find_pos)

    def searchable_mod():
        global searchable
        global update_selector
        searching_for = search_for_what.get()
        search_type = search_for_type.get()
        searchable = []
        if searching_for != "":
            selection.delete(0,'end')
            if search_type == "index":
                searchable = [y for y in ymls if str(y[0]).find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, s[0])
                    selection.insert(i, str(s[0]) + ' (' + str(s[6]) + ')')
        else:
            selection.delete(0,'end')
            searchable = [y for y in ymls]
            i = -1
            for s in searchable:
                i += 1
                selection.insert(i, str(s[0]))

    def searchable_modify(event):
        searchable_mod()

    searcher.bind("<KeyRelease>", searchable_modify)

    
    searchable_as= [("By Index Number", "index")]
    
    #Items
    item_ent_1 = Tkinter.Entry(store_w, textvariable = item_1)
    entries.append(item_ent_1)
    item_ent_1.place(x = 130+120, y = 50)
    item_lab_1 = Tkinter.Label(store_w, text = 'Item 1:')
    labels.append(item_lab_1)
    item_lab_1.place(x=50+120, y=50)
    item_lab_1_n = Tkinter.Label(store_w, textvariable = item_1_n)
    labels.append(item_lab_1_n)
    item_lab_1_n.place(x=130+120+160, y=50)

    item_ent_2 = Tkinter.Entry(store_w, textvariable = item_2)
    entries.append(item_ent_2)
    item_ent_2.place(x = 130+120, y = 82)
    item_lab_2 = Tkinter.Label(store_w, text = 'Item 2:')
    labels.append(item_lab_2)
    item_lab_2.place(x=50+120, y=82)
    item_lab_2_n = Tkinter.Label(store_w, textvariable = item_2_n)
    labels.append(item_lab_2_n)
    item_lab_2_n.place(x=130+120+160, y=82)

    item_ent_3 = Tkinter.Entry(store_w, textvariable = item_3)
    entries.append(item_ent_3)
    item_ent_3.place(x = 130+120, y = 114)
    item_lab_3 = Tkinter.Label(store_w, text = 'Item 3:')
    labels.append(item_lab_3)
    item_lab_3.place(x=50+120, y=114)
    item_lab_3_n = Tkinter.Label(store_w, textvariable = item_3_n)
    labels.append(item_lab_3_n)
    item_lab_3_n.place(x=130+120+160, y=114)

    item_ent_4 = Tkinter.Entry(store_w, textvariable = item_4)
    entries.append(item_ent_4)
    item_ent_4.place(x = 130+120, y = 146)
    item_lab_4 = Tkinter.Label(store_w, text = 'Item 4:')
    labels.append(item_lab_4)
    item_lab_4.place(x=50+120, y=146)
    item_lab_4_n = Tkinter.Label(store_w, textvariable = item_4_n)
    labels.append(item_lab_4_n)
    item_lab_4_n.place(x=130+120+160, y=146)

    item_ent_5 = Tkinter.Entry(store_w, textvariable = item_5)
    entries.append(item_ent_5)
    item_ent_5.place(x = 130+120, y = 146+32)
    item_lab_5 = Tkinter.Label(store_w, text = 'Item 5:')
    labels.append(item_lab_5)
    item_lab_5.place(x=50+120, y=146+32)
    item_lab_5_n = Tkinter.Label(store_w, textvariable = item_5_n)
    labels.append(item_lab_5_n)
    item_lab_5_n.place(x=130+120+160, y=146+32)

    item_ent_6 = Tkinter.Entry(store_w, textvariable = item_6)
    entries.append(item_ent_6)
    item_ent_6.place(x = 130+120, y = 146+64)
    item_lab_6 = Tkinter.Label(store_w, text = 'Item 6:')
    labels.append(item_lab_6)
    item_lab_6.place(x=50+120, y=146+64)
    item_lab_6_n = Tkinter.Label(store_w, textvariable = item_6_n)
    labels.append(item_lab_6_n)
    item_lab_6_n.place(x=130+120+160, y=146+64)

    item_ent_7 = Tkinter.Entry(store_w, textvariable = item_7)
    entries.append(item_ent_7)
    item_ent_7.place(x = 130+120, y = 146+92)
    item_lab_7 = Tkinter.Label(store_w, text = 'Item 7:')
    labels.append(item_lab_7)
    item_lab_7.place(x=50+120, y=146+92)
    item_lab_7_n = Tkinter.Label(store_w, textvariable = item_7_n)
    labels.append(item_lab_7_n)
    item_lab_7_n.place(x=130+120+160, y=146+92)

    def run_select(event):
        selector()

    item_ent_1.bind("<KeyRelease>", run_select)
    item_ent_2.bind("<KeyRelease>", run_select)
    item_ent_3.bind("<KeyRelease>", run_select)
    item_ent_4.bind("<KeyRelease>", run_select)
    item_ent_5.bind("<KeyRelease>", run_select)
    item_ent_6.bind("<KeyRelease>", run_select)
    item_ent_7.bind("<KeyRelease>", run_select)

    def delete_entry():
        global update_selector,dele
        global loaded
        if loaded != [] and loaded != -1 and loaded != tuple():
            result = tkMessageBox.askquestion("Delete", "Are You Sure?", icon='warning', parent = b_action)
            if result == 'yes':
                ymls.remove(ymls[[s[0] for s in searchable].index([s[0] for s in searchable][pos])])
                update_selector = True
                dele = True
                selector()

    def add_entry():
        if searchable == ymls: 
            global update_selector,add,to_add
            stop = 0
            for i in range(len(ymls)):
                if int(ymls[i][0]) != i:
                    ymls.insert(i,(i,0,0,0,0,0,0,0))
                    update_selector = True
                    add = True
                    to_add = i
                    selector()  
                    return
            if stop == 0:
                ymls.append((i+1,0,0,0,0,0,0,0))
                update_selector = True
                to_add = i + 1
                add = True
                selector()     
    delete_button = Tkinter.Button(store_w, command = delete_entry, text= "Delete Entry")
    buttons.append(delete_button)
    delete_button.place(x= 16, y = 32)
    add_button = Tkinter.Button(store_w, command = add_entry, text = "Add Entry")
    buttons.append(add_button)
    add_button.place(x= 90, y = 32)

    #Tracker
    current_pos = Tkinter.Label(store_w, textvariable = current)
    labels.append(current_pos)
    current_pos.place(x = 420, y = 400)

    def replacer():
        global stuff_loaded
        global selected_type
        global loaded
        a = loaded[0]
        b = loaded[1]
        c = loaded[2]
        d = loaded[3]
        e = loaded[4]
        f = loaded[5]
        g = loaded[6]
        h = loaded[7]

        item_1_t = item_1.get()
        if item_1_t != b:
            b = int(item_1_t)
            print b

        item_2_t = item_2.get()
        if item_2_t != c:
            c = int(item_2_t)

        item_3_t = item_3.get()
        if item_3_t != d:
            d = int(item_3_t)

        item_4_t = item_4.get()
        if item_4_t != e:
            e = int(item_4_t)

        item_5_t = item_5.get()
        if item_5_t != f:
            f = int(item_5_t)

        item_6_t = item_6.get()
        if item_6_t != g:
            g = int(item_6_t)

        item_7_t = item_7.get()
        if item_7_t != h:
            h = int(item_7_t)
            
        replaced = tuple((a,b,c,d,e,f,g,h))
        if replaced != loaded:
            ymls[[s[0] for s in searchable][pos]] = replaced
        return    

    def saver():
        global stuff_loaded
        global loaded
        if stuff_loaded:
            replacer()
            location = os.getcwd()
            to_dump = open(save_data + "/store_table.yml",'w')
            changed_ymls = {}
            for y in ymls:
                changed_ymls[y[0]] = {"Item 1" : int(y[1]),
                                         "Item 2" : int(y[2]),
                                         "Item 3" : int(y[3]),
                                         "Item 4" : int(y[4]),
                                         "Item 5" : int(y[5]),
                                         "Item 6" : int(y[6]),
                                         "Item 7" : int(y[7])}
            yaml.dump(changed_ymls, to_dump, default_flow_style=False)
        store_w.destroy()

        w_2.remove(w_2[[w[1] for w in w_2].index("shops")])
        stram.close()

    store_w.protocol("WM_DELETE_WINDOW", saver)

def call_store(w_2):
    
    (w_2[[w[1] for w in w_2].index("shops")])[0].lift()


