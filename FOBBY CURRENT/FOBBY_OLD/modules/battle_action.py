import Tkinter, re, sys, yaml, tkMessageBox, os, unicodedata
sys.path.append(os.getcwd()[:-7])
import FOBBY
 
def b_action(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,path,save_data):
    global stuff_loaded
    global pk_text
    global update_selector
    update_selector = False
    stuff_loaded = False
    global searchable
    searchable = []
    ymls = []
    moves = []
    actions = []
    code_adresses = []
    directions = []
    costs = []
    targets = []
    text_adresses = []
    final_format = []
    selector_index = []
    loaded = tuple()
    p_cost = Tkinter.StringVar()
    text_adress_a = Tkinter.StringVar()
    code_adress_a = Tkinter.StringVar()
    selected_direction = Tkinter.StringVar()
    selected_target = Tkinter.StringVar()
    x_path = path[:-13]
    b_action = Tkinter.Toplevel()
    b_action.geometry('600x580+550+300')
    
    windows.append(b_action)
    w_2.append((b_action,"battle_action"))
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
    
    if os.path.exists(save_data+ "/battle_action_table.yml"):
        stram = open(save_data + "/battle_action_table.yml", "r")
    else:
        r_path = x_path + "battle_action_table.yml"
        stram = open(r_path, "r")

    yml = yaml.load(stram)
    str_yml = str(yml)
    le = (re.findall(r'[0-9]+: {',str_yml))
    for l in range(len(le)):
        z = re.findall(r'[0-9]+',le[l])
        moves.append(int(le[l][0:(len(str(z[0])))]))
        actions.append(yml[int(z[0])]['Action type'])
        code_adresses.append(yml[int(z[0])]['Code Address'])
        directions.append(yml[int(z[0])]['Direction'])
        costs.append(yml[int(z[0])]['PP Cost'])
        targets.append(yml[int(z[0])]['Target'])
        text_adresses.append(yml[int(z[0])]['Text Address'])
    
        
    i = -1
    while i < (len(actions)) -1:
        i += 1
        ymls.append((moves[i],actions[i],code_adresses[i],directions[i],costs[i],targets[i],text_adresses[i]))
    file.close(stram)
    searchable = [y for y in ymls]

    selection = Tkinter.Listbox(b_action)
    listboxes.append(selection)
    for l in range(len(ymls)):
        selection.insert(l, ymls[l][0])
    selection.place(x=16, y=64)

    selections_scroller = Tkinter.Scale(b_action, from_=0, to=len(ymls))
    selections_scroller.config(command=selection.yview)
    scalers.append(selections_scroller)
    selections_scroller.place(x=128 , y=80 )

    searcher = Tkinter.Entry(b_action, textvariable = search_for_what)
    entries.append(searcher)
    searcher.place(x=16, y=270)


    def selector():
        global stuff_loaded
        global pk_text
        global loaded
        global pos
        global update_selector,add,dele,to_add
        global searchable

        pk_text = p_cost.get()
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
        
        selected_type.set(loaded[1])
        if loaded[1] == "physical (affected by shields and defending)":
            selected_type.set("physical")
        if loaded[2].find(".") == -1:
            code_adress_a.set(loaded[2][1:])
        else:
            code_adress_a.set(loaded[2])
        selected_direction.set(loaded[3])
        p_cost.set(loaded[4])
        selected_target.set(loaded[5])
        if loaded[6].find(".") == -1:
            text_adress_a.set(loaded[6][1:])
        else:
            text_adress_a.set(loaded[6])
        stuff_loaded = True

        current.set("You are currently editing: " + str(loaded[0]))

        
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
            elif search_type == "type":
                searchable = [y for y in ymls if y[1].find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, str(s[0]) + ' (' + str(s[1]) + ')')
            elif search_type == "code_adress_code":
                searchable = [y for y in ymls if y[2].find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, str(s[0]) + ' (' + str(s[2]) + ')')
            elif search_type == "direction":
                searchable = [y for y in ymls if y[3].find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, str(s[0]) + ' (' + str(s[3]) + ')')
            elif search_type == "cost":
                searchable = [y for y in ymls if str(y[4]).find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, str(s[0]) + ' (' + str(s[4]) + ')')
            elif search_type == "target":
                searchable = [y for y in ymls if y[5].find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, str(s[0]) + ' (' + str(s[5]) + ')')
            elif search_type == "text_adress":
                searchable = [y for y in ymls if y[6].find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
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

    
    searchable_as= [
        ("By Index Number", "index"),
        ("By Type", "type"),
        ("By Code Adress (Code)", "code_adress_code"),
        ("By Direction", "direction"),
        ("By PP Cost", "cost"),
        ("By Target", "target"),
        ("By Text Adress", "text_adress")]    

    y = 290
    for text, typ in searchable_as:
        search_radio = Tkinter.Radiobutton(b_action, text=text,
                     var=search_for_type, value=typ)
        search_radio.place(x=16,y=y)
        radiobuttons.append(search_radio)
        search_radio.bind('<Button-1>',searchable_modify)
        y += 32



    types =[("Physical", "physical"),
    ("Physical (ignore shields and guard)", "physical (unaffected by shields and defending)"),
    ("PSI", "psi"),
    ("Other", "other"),
    ("Item", "item"),
    ("None or Unknown", "nothing")]

    y = 250
    for text, typ in types:
        type_radio = Tkinter.Radiobutton(b_action, text=text,
                     variable=selected_type, value=typ)
        type_radio.place(x=200,y=y)
        radiobuttons.append(type_radio)
        y += 32

    types = Tkinter.Label(b_action, text = 'Type:')
    labels.append(types)
    types.place(x=200 , y=218 )

    #Direction
    directions = [
        ("Self", "self"),
        ("Party", "party"),
        ("Enemy", "enemy")]    

    y = 250
    for text, typ in directions:
        direct_radio = Tkinter.Radiobutton(b_action, text=text,
                     variable=selected_direction, value=typ)
        direct_radio.place(x=410,y=y)
        radiobuttons.append(direct_radio)
        y += 32

    direct = Tkinter.Label(b_action, text = 'Direction:')
    labels.append(direct)
    direct.place(x=410 , y=218 )

    #Code Adreess
    code_a = Tkinter.Entry(b_action, textvariable = code_adress_a)
    entries.append(code_a)
    code_a.place(x = 280, y = 160)
    pk_cost = Tkinter.Label(b_action, text = 'Code Adress:')
    labels.append(pk_cost)
    pk_cost.place(x=200 , y=160 )
     
    #PP Cost
    cost = Tkinter.Entry(b_action, textvariable = p_cost)
    entries.append(cost)
    cost.place(x = 280, y = 80)
    pk_cost = Tkinter.Label(b_action, text = 'PP Cost:')
    labels.append(pk_cost)
    pk_cost.place(x=200 , y=80 )

    #Target
    targets = [
        ("Single", "one"),
        ("Row", "row"),
        ("All", "all"),
        ("None", "none")]    

    y = 250
    for text, typ in targets:
        target_radio = Tkinter.Radiobutton(b_action, text=text,
                     variable=selected_target, value=typ)
        target_radio.place(x=490,y=y)
        radiobuttons.append(target_radio)
        y += 32

    target = Tkinter.Label(b_action, text = 'Target:')
    labels.append(target)
    target.place(x=490 , y=218 )

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
                    ymls.insert(i,(i,"physical","$0","self","0","one","$0"))
                    update_selector = True
                    add = True
                    to_add = i
                    selector()  
                    return
            if stop == 0:
                ymls.append((i+1,"physical","$0","self","0","one","$0"))
                update_selector = True
                to_add = i + 1
                add = True
                selector()
            
            

    delete_button = Tkinter.Button(b_action, command = delete_entry, text= "Delete Entry")
    buttons.append(delete_button)
    delete_button.place(x= 16, y = 32)
    add_button = Tkinter.Button(b_action, command = add_entry, text = "Add Entry")
    buttons.append(add_button)
    add_button.place(x= 90, y = 32)
    

    #Text Adresser
    code_t = Tkinter.Entry(b_action, textvariable = text_adress_a)
    entries.append(code_t)
    code_t.place(x = 280, y = 120)
    pk_cost = Tkinter.Label(b_action, text = 'Text Adress:')
    labels.append(pk_cost)
    pk_cost.place(x=200 , y=120 )

    #Tracker
    current_pos = Tkinter.Label(b_action, textvariable = current)
    labels.append(current_pos)
    current_pos.place(x = 420, y = 100)

    def replacer():
        global stuff_loaded
        global selected_type
        global pk_text
        global loaded
        a = loaded[0]
        b = loaded[1]
        c = loaded[2]
        d = loaded[3]
        e = loaded[4]
        f = loaded[5]
        g = loaded[6]

        selected_t = selected_type.get()
        if selected_t != b:
            b = selected_t

        code_adressed = code_adress_a.get()
        if code_adressed != c:
            if code_adressed.find(".") == -1:
                c = "$" + code_adressed
            else:
                c = code_adressed

        directed = selected_direction.get()
        if directed != d:
            d = directed
        
        pk_text = p_cost.get()
        if pk_text != e:
            e = int(pk_text)

        targeted = selected_target.get()
        if targeted != f:
            f = targeted

        text_adressed = text_adress_a.get()
        if text_adressed != g:
            if text_adressed.find(".") == -1:
                g = "$" + text_adressed
            else:
                g = text_adressed

        replaced = tuple((a,b,c,d,e,f,g))
        if replaced != loaded:
            ymls[[s[0] for s in searchable][pos]] = replaced
        return    

    def saver():
        global stuff_loaded
        global pk_text
        global loaded
        if stuff_loaded:
            replacer()
            location = os.getcwd()
            to_dump = open(save_data + "/battle_action_table.yml",'w')
            changed_ymls = {}
            for y in ymls:
                changed_ymls[y[0]] = {"Action type" : y[1],
                                         "Code Address" : y[2],
                                         "Direction" : y[3],
                                         "PP Cost" : y[4],
                                         "Target" : y[5],
                                         "Text Address" : y[6]}
            yaml.dump(changed_ymls, to_dump, default_flow_style=False)
        b_action.destroy()

        w_2.remove(w_2[[w[1] for w in w_2].index("battle_action")])
        stram.close()

    b_action.protocol("WM_DELETE_WINDOW", saver)

def call_battle_action(w_2):
    
    (w_2[[w[1] for w in w_2].index("battle_action")])[0].lift()


