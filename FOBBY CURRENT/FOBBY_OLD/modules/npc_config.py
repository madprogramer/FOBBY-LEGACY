import Tkinter, re, sys, yaml, tkMessageBox, os, unicodedata, base64
sys.path.append(os.getcwd()[:-7])
from PIL import Image, ImageTk
import FOBBY

def digit_conversion(integer):
    string = str(integer)
    if len(string) == 1:
        string = "00" + str(integer)
    elif len(string) == 2:
        string = "0" + str(integer)
    return string
 
def npcs_c(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,path,save_data):
    global stuff_loaded
    global pk_text
    global update_selector
    update_selector = False
    stuff_loaded = False
    
    global searchable
    searchable = []
    ymls = []

    npcs = []

    
    
    directions = []
    flags = []
    sprites = []
    text_pointers_1 = []
    text_pointers_2 = []
    types = []
    show_sprites = []
    movements = []
    
    final_format = []
    
    selector_index = []
    loaded = tuple()
    
    direction = Tkinter.StringVar()
    flag = Tkinter.StringVar()
    hex_flag = Tkinter.StringVar()
    sprite = Tkinter.StringVar()
    text_pointer_1 = Tkinter.StringVar()
    text_pointer_2 = Tkinter.StringVar()
    npc_type = Tkinter.StringVar()
    show_npc = Tkinter.StringVar()
    movement = Tkinter.StringVar()
    
    x_path = path[:-13]
    npc_w = Tkinter.Toplevel()
    npc_w.geometry('1080x1080')
    
    windows.append(npc_w)
    w_2.append((npc_w,"npc config"))
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

    spr_loadable = {}
    
    if os.path.exists(save_data+ "/npc_config_table.yml"):
        stram = open(save_data + "/npc_config_table.yml", "r")
    else:
        r_path = x_path + "npc_config_table.yml"
        stram = open(r_path, "r")

    yml = yaml.load(stram)
    str_yml = str(yml)
    print str_yml

    if os.path.exists(save_data+ "/sprite_groups.yml"):
        strem = open(save_data + "/sprite_groups.yml", "r")
    else:
        r_path = x_path + "sprite_groups.yml"
        strem = open(r_path, "r")
        yml_2 = yaml.load(strem)

    le = (re.findall(r'[0-9]+: {',str_yml))
    for l in range(len(le)):
        z = re.findall(r'[0-9]+',le[l])
        npcs.append(int(le[l][0:(len(str(z[0])))]))
        directions.append(yml[int(z[0])]['Direction'])
        flags.append(yml[int(z[0])]['Event Flag'])
        movements.append(yml[int(z[0])]['Movement'])
        show_sprites.append(yml[int(z[0])]['Show Sprite'])
        sprites.append(yml[int(z[0])]['Sprite'])
        text_pointers_1.append(yml[int(z[0])]['Text Pointer 1'])
        text_pointers_2.append(yml[int(z[0])]['Text Pointer 2'])
        types.append(yml[int(z[0])]['Type'])
        
    i = -1
    while i < (len(directions)) -1:
        i += 1
        ymls.append((npcs[i],directions[i],flags[i],movements[i],show_sprites[i],sprites[i],
                     text_pointers_1[i],text_pointers_2[i],types[i]))
    file.close(stram)
    searchable = [y for y in ymls]

    selection = Tkinter.Listbox(npc_w)
    listboxes.append(selection)
    for l in range(len(ymls)):
        selection.insert(l, ymls[l][0])
    selection.place(x=16, y=64)

    selections_scroller = Tkinter.Scale(npc_w, from_=0, to=len(ymls))
    selections_scroller.config(command=selection.yview)
    scalers.append(selections_scroller)
    selections_scroller.place(x=128 , y=80 )

    searcher = Tkinter.Entry(npc_w, textvariable = search_for_what)
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
        
        direction.set(loaded[1])
        flag.set(loaded[2])
        movement.set(loaded[3])

        show_npc.set(loaded[4])
        sprite.set(loaded[5])

        if loaded[6].find(".") == -1:
            text_pointer_1.set(loaded[6][1:])
        else:
            text_pointer_1.set(loaded[6])

        if loaded[7].find(".") == -1:
            text_pointer_2.set(loaded[7][1:])
        else:
            text_pointer_2.set(loaded[7])

        npc_type.set(loaded[8])

        hex_flag.set(hex(int(flag.get())))

        stuff_loaded = True



        if os.path.exists(save_data + "/SpriteGroups/" + digit_conversion(loaded[5]) +".png"):
            global sprite_final,group_sprite,sprite_path,real_sprite

            real_sprite = True
            
            sprite_path = save_data + "/SpriteGroups/" + digit_conversion(loaded[5]) +".png"



            group_sprite = Image.open(sprite_path)



            sprite_final = ImageTk.PhotoImage(group_sprite)
                
            spr_lab.config(image = sprite_final,text = "")

            print sprite_final,group_sprite,sprite_path,real_sprite


        elif os.path.exists(x_path + "SpriteGroups/" + digit_conversion(loaded[5]) +".png"):
            global sprite_final,group_sprite,sprite_path,real_sprite

            real_sprite = True
            sprite_path = x_path + "SpriteGroups/" + digit_conversion(loaded[5]) +".png"

            group_sprite = Image.open(sprite_path)

            sprite_final = ImageTk.PhotoImage(group_sprite)
                
            spr_lab.config(image = sprite_final,text = "")

            print sprite_final,group_sprite,sprite_path,real_sprite

        else:
            sprite_path = save_data + "/SpriteGroups/" + digit_conversion(loaded[5]) +".png"
            real_sprite = False
            spr_lab.config(image = "" ,text = "Sorry, this sprite is missing!")

        print(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"0"+".png")

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"0"+".png"):
            global spr_lab_0_p

            spr_lab_0_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"0"+".png")

            spr_lab_0_p = ImageTk.PhotoImage(spr_lab_0_i)
            
            spr_lab_0.config(image = spr_lab_0_p ,text = "")

            spr_loadable[0] = spr_lab_0_p
        else:
            spr_lab_0.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"1"+".png"):
            global spr_lab_1_p

            spr_lab_1_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"1"+".png")

            spr_lab_1_p = ImageTk.PhotoImage(spr_lab_1_i)
            
            spr_lab_1.config(image = spr_lab_1_p ,text = "")

            spr_loadable[1] = spr_lab_1_p
        else:
            spr_lab_1.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"2"+".png"):
            global spr_lab_2_p

            spr_lab_2_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"2"+".png")

            spr_lab_2_p = ImageTk.PhotoImage(spr_lab_2_i)
            
            spr_lab_2.config(image = spr_lab_2_p ,text = "")

            spr_loadable[2] = spr_lab_2_p
        else:
            spr_lab_2.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"3"+".png"):
            global spr_lab_3_p

            spr_lab_3_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"3"+".png")

            spr_lab_3_p = ImageTk.PhotoImage(spr_lab_3_i)
            
            spr_lab_3.config(image = spr_lab_3_p ,text = "")

            spr_loadable[3] = spr_lab_3_p
        else:
            spr_lab_3.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"4"+".png"):
            global spr_lab_4_p

            spr_lab_4_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"4"+".png")

            spr_lab_4_p = ImageTk.PhotoImage(spr_lab_4_i)
            
            spr_lab_4.config(image = spr_lab_4_p ,text = "")

            spr_loadable[4] = spr_lab_4_p
        else:
            spr_lab_4.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"5"+".png"):
            global spr_lab_5_p

            spr_lab_5_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"5"+".png")

            spr_lab_5_p = ImageTk.PhotoImage(spr_lab_5_i)
            
            spr_lab_5.config(image = spr_lab_5_p ,text = "")

            spr_loadable[5] = spr_lab_5_p
        else:
            spr_lab_5.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"6"+".png"):
            global spr_lab_6_p

            spr_lab_6_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"6"+".png")

            spr_lab_6_p = ImageTk.PhotoImage(spr_lab_6_i)
            
            spr_lab_6.config(image = spr_lab_6_p ,text = "")

            spr_loadable[6] = spr_lab_6_p
        else:
            spr_lab_6.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"7"+".png"):
            global spr_lab_7_p

            spr_lab_7_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"7"+".png")

            spr_lab_7_p = ImageTk.PhotoImage(spr_lab_7_i)
            
            spr_lab_7.config(image = spr_lab_7_p ,text = "")

            spr_loadable[7] = spr_lab_7_p
        else:
            spr_lab_7.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"8"+".png"):
            global spr_lab_8_p

            spr_lab_8_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"8"+".png")

            spr_lab_8_p = ImageTk.PhotoImage(spr_lab_8_i)
            
            spr_lab_8.config(image = spr_lab_8_p ,text = "")

            spr_loadable[8] = spr_lab_8_p
        else:
            spr_lab_8.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"9"+".png"):
            global spr_lab_9_p

            spr_lab_9_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"9"+".png")

            spr_lab_9_p = ImageTk.PhotoImage(spr_lab_9_i)
            
            spr_lab_9.config(image = spr_lab_9_p ,text = "")

            spr_loadable[9] = spr_lab_9_p
        else:
            spr_lab_9.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"10"+".png"):
            global spr_lab_10_p

            spr_lab_10_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"10"+".png")

            spr_lab_10_p = ImageTk.PhotoImage(spr_lab_10_i)
            
            spr_lab_10.config(image = spr_lab_10_p ,text = "")

            spr_loadable[10] = spr_lab_10_p
        else:
            spr_lab_10.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"11"+".png"):
            global spr_lab_11_p

            spr_lab_11_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"11"+".png")

            spr_lab_11_p = ImageTk.PhotoImage(spr_lab_11_i)
            
            spr_lab_11.config(image = spr_lab_11_p ,text = "")

            spr_loadable[11] = spr_lab_11_p
        else:
            spr_lab_11.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"12"+".png"):
            global spr_lab_12_p

            spr_lab_12_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"12"+".png")

            spr_lab_12_p = ImageTk.PhotoImage(spr_lab_12_i)
            
            spr_lab_12.config(image = spr_lab_12_p ,text = "")

            spr_loadable[12] = spr_lab_12_p
        else:
            spr_lab_12.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"13"+".png"):
            global spr_lab_13_p

            spr_lab_13_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"13"+".png")

            spr_lab_13_p = ImageTk.PhotoImage(spr_lab_13_i)
            
            spr_lab_13.config(image = spr_lab_13_p ,text = "")

            spr_loadable[13] = spr_lab_13_p
        else:
            spr_lab_13.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"14"+".png"):
            global spr_lab_14_p

            spr_lab_14_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"14"+".png")

            spr_lab_14_p = ImageTk.PhotoImage(spr_lab_14_i)
            
            spr_lab_14.config(image = spr_lab_14_p ,text = "")

            spr_loadable[14] = spr_lab_14_p
        else:
            spr_lab_14.config(image = "" )

        if os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"15"+".png"):
            global spr_lab_15_p

            spr_lab_15_i = Image.open(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+"15"+".png")

            spr_lab_15_p = ImageTk.PhotoImage(spr_lab_15_i)
            
            spr_lab_15.config(image = spr_lab_15_p ,text = "")

            spr_loadable[15] = spr_lab_15_p
        else:
            spr_lab_15.config(image = "" )

        spr_lab_l.config(image="")
            

            
            
        current.set("You are currently editing: " + str(loaded[5]))
        
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
            elif search_type == "sprite":
                searchable = [y for y in ymls if y[5].find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, str(s[0]) + ' (' + str(s[5]) + ')')

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
        ("By Sprite", "sprite")]    

    y = 290
    for text, typ in searchable_as:
        search_radio = Tkinter.Radiobutton(npc_w, text=text,
                     var=search_for_type, value=typ)
        search_radio.place(x=16,y=y)
        radiobuttons.append(search_radio)
        search_radio.bind('<Button-1>',searchable_modify)
        y += 32

    looks =[("Up","up"),("Right","right"),("Left","left"),("Down","down")]

    y = 50
    for text, typ in looks:
        look_radio = Tkinter.Radiobutton(npc_w, text=text,
                     variable=direction, value=typ)
        look_radio.place(x=200,y=y)
        radiobuttons.append(look_radio)
        y += 32

    flag_lab = Tkinter.Label(npc_w, text = 'Flag:')
    labels.append(flag_lab)
    flag_lab.place(x=200 , y=50+128)
    flag_ent = Tkinter.Entry(npc_w, textvariable = flag)
    entries.append(flag_ent)
    flag_ent.place(x = 280, y =50+128)
    flag_hex = Tkinter.Label(npc_w, textvariable = hex_flag)
    labels.append(flag_hex)
    flag_hex.place(x=200 , y=50+128+32)

    def update_hex(event):
        hex_flag.set(hex(int(flag.get())))

    flag_ent.bind("<KeyRelease>", update_hex)

    move_lab = Tkinter.Label(npc_w, text = 'Movements:')
    labels.append(move_lab)
    move_lab.place(x=200 , y=50+160+32)
    move_ent = Tkinter.Entry(npc_w, textvariable = movement)
    entries.append(move_ent)
    move_ent.place(x = 280, y =50+160+32)

    #Show Sprite Condition
    conditions = [
        ("Always", "always"),
        ("When Flag is ON", "when event flag set"),
        ("When Flag is OFF", "when event flag unset")]    

    y = 262+32
    for text, typ in conditions:
        cond_radio = Tkinter.Radiobutton(npc_w, text=text,
                     variable=show_npc, value=typ)
        cond_radio.place(x=200,y=y)
        radiobuttons.append(cond_radio)
        y += 32

    show_spr = Tkinter.Label(npc_w, text = 'Show Sprite Condition:')
    labels.append(show_spr)
    show_spr.place(x=200 , y=240+32 )

    sprite_lab = Tkinter.Label(npc_w, text = 'Sprite Group:')
    labels.append(sprite_lab)
    sprite_lab.place(x=410 , y=50)
    sprite_ent = Tkinter.Entry(npc_w, textvariable = sprite)
    entries.append(sprite_ent)
    sprite_ent.place(x = 500, y =50)
    sprite_ent.bind("<KeyRelease>",find_pos)

    pointer_1_lab = Tkinter.Label(npc_w, text = 'Text Pointer 1 (Check or Talk):')
    labels.append(pointer_1_lab)
    pointer_1_lab.place(x=410 , y=50+32)
    pointer_1_ent = Tkinter.Entry(npc_w, textvariable = text_pointer_1)
    entries.append(pointer_1_ent)
    pointer_1_ent.place(x = 410, y = 50+64)

    pointer_2_lab = Tkinter.Label(npc_w, text = 'Text Pointer 2 (Item used on NPC or Item to get from Chest):')
    labels.append(pointer_2_lab)
    pointer_2_lab.place(x=410 , y=50+96)
    pointer_2_ent = Tkinter.Entry(npc_w, textvariable = text_pointer_2)
    entries.append(pointer_2_ent)
    pointer_2_ent.place(x = 410, y =50+128)

    types = [
        ("Person (Talk)", "person"),
        ("Object (Check)", "object"),
        ("Item (Check, ex. Present)", "item")]    

    y = 50+128+32
    for text, typ in types:
        type_radio = Tkinter.Radiobutton(npc_w, text=text,
                     variable=npc_type, value=typ)
        type_radio.place(x=410,y=y)
        radiobuttons.append(type_radio)
        y += 32

    def col_check(event):
        global loaded
        print loaded
        #print str(yml_2[loaded[5]])
        spr_lab_col.config(text = str(yml_2[loaded[5]]["Collision Settings"]))

    spr_lab = Tkinter.Label(npc_w)
    labels.append(spr_lab)
    spr_lab.place(x=20 , y=412)

    spr_lab_0 = Tkinter.Label(npc_w)
    labels.append(spr_lab_0)
    spr_lab_0.place(x=370 , y=412)

    def click_0(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[0])
        return

    spr_lab_0.bind("<Button-1>",click_0)
    spr_lab_0.bind("<Button-1>",col_check)

    spr_lab_1 = Tkinter.Label(npc_w)
    labels.append(spr_lab_1)
    spr_lab_1.place(x=500 , y=412)

    def click_1(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[1])
        return

    spr_lab_1.bind("<Button-1>",click_1)
    spr_lab_1.bind("<Button-1>",col_check)

    spr_lab_2 = Tkinter.Label(npc_w)
    labels.append(spr_lab_2)
    spr_lab_2.place(x=630 , y=412)

    def click_2(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[2])
        return

    spr_lab_2.bind("<Button-1>",click_2)
    spr_lab_2.bind("<Button-1>",col_check)

    spr_lab_3 = Tkinter.Label(npc_w)
    labels.append(spr_lab_3)
    spr_lab_3.place(x=760 , y=412)

    def click_3(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[3])
        return

    spr_lab_3.bind("<Button-1>",click_3)
    spr_lab_3.bind("<Button-1>",col_check)

    spr_lab_4 = Tkinter.Label(npc_w)
    labels.append(spr_lab_4)
    spr_lab_4.place(x=370 , y=552)

    def click_4(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[4])
        return

    spr_lab_4.bind("<Button-1>",click_4)
    spr_lab_4.bind("<Button-1>",col_check)

    spr_lab_5 = Tkinter.Label(npc_w)
    labels.append(spr_lab_5)
    spr_lab_5.place(x=500 , y=552)

    def click_5(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[5])
        return

    spr_lab_5.bind("<Button-1>",click_5)
    spr_lab_5.bind("<Button-1>",col_check)

    spr_lab_6 = Tkinter.Label(npc_w)
    labels.append(spr_lab_6)
    spr_lab_6.place(x=630 , y=552)

    def click_6(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[6])
        return

    spr_lab_6.bind("<Button-1>",click_6)
    spr_lab_6.bind("<Button-1>",col_check)

    spr_lab_7 = Tkinter.Label(npc_w)
    labels.append(spr_lab_7)
    spr_lab_7.place(x=760 , y=552)

    def click_7(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[7])
        return

    spr_lab_7.bind("<Button-1>",click_7)
    spr_lab_7.bind("<Button-1>",col_check)

    spr_lab_8 = Tkinter.Label(npc_w)
    labels.append(spr_lab_8)
    spr_lab_8.place(x=370 , y=692)

    def click_8(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[8])
        return

    spr_lab_8.bind("<Button-1>",click_8)
    spr_lab_8.bind("<Button-1>",col_check)

    spr_lab_9 = Tkinter.Label(npc_w)
    labels.append(spr_lab_9)
    spr_lab_9.place(x=500 , y=692)

    def click_9(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[9])
        return

    spr_lab_9.bind("<Button-1>",click_9)
    spr_lab_9.bind("<Button-1>",col_check)


    spr_lab_10 = Tkinter.Label(npc_w)
    labels.append(spr_lab_10)
    spr_lab_10.place(x=630 , y=692)

    def click_10(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[10])
        return

    spr_lab_10.bind("<Button-1>",click_10)
    spr_lab_10.bind("<Button-1>",col_check)

    spr_lab_11 = Tkinter.Label(npc_w)
    labels.append(spr_lab_11)
    spr_lab_11.place(x=760 , y=692)

    def click_11(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[11])
        return

    spr_lab_11.bind("<Button-1>",click_11)
    spr_lab_11.bind("<Button-1>",col_check)

    spr_lab_12 = Tkinter.Label(npc_w)
    labels.append(spr_lab_12)
    spr_lab_12.place(x=370 , y=832)

    def click_12(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[12])
        return

    spr_lab_12.bind("<Button-1>",click_12)
    spr_lab_12.bind("<Button-1>",col_check)

    spr_lab_13 = Tkinter.Label(npc_w)
    labels.append(spr_lab_13)
    spr_lab_13.place(x=500 , y=832)

    def click_13(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[13])
        return

    spr_lab_13.bind("<Button-1>",click_13)
    spr_lab_13.bind("<Button-1>",col_check)

    spr_lab_14 = Tkinter.Label(npc_w)
    labels.append(spr_lab_14)
    spr_lab_14.place(x=630 , y=832)

    def click_14(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[14])
        return

    spr_lab_14.bind("<Button-1>",click_14)
    spr_lab_14.bind("<Button-1>",col_check)

    spr_lab_15 = Tkinter.Label(npc_w)
    labels.append(spr_lab_15)
    spr_lab_15.place(x=760 , y=832)

    def click_15(event):
        print(spr_loadable)
        spr_lab_l.config(image=spr_loadable[15])
        return

    spr_lab_15.bind("<Button-1>",click_15)
    spr_lab_15.bind("<Button-1>",col_check)

    spr_lab_l = Tkinter.Label(npc_w)
    labels.append(spr_lab_l)
    spr_lab_l.place(x=812 , y=20)

    spr_lab_col = Tkinter.Label(npc_w)
    labels.append(spr_lab_col)
    spr_lab_col.place(x=812 , y=20)




    def decompile_spr():
        global loaded, group_sprite,sprite_final,group_sprite,sprite_path,real_sprite
        if stuff_loaded == True:
            print (group_sprite.size)
            imagex,imagey = group_sprite.size
            parts = []
            count = -1
            for y in range(imagey/4,imagey+1,imagey/4):
                for x in range(imagex/4,imagex+1,imagex/4):
                    count +=1
                    print count
                    
                    print x-1,y-1
                    if not os.path.exists(save_data+"/"+"SpriteGroups"):
                        os.mkdir(save_data+"/"+"SpriteGroups")
                        
                    if not os.path.exists(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])):
                        os.mkdir(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5]))
                    crop_image = group_sprite.crop((x-imagex/4,y-imagey/4,x,y))
                    png_info = group_sprite.info

                    crop_image.save(save_data+"/"+"SpriteGroups"+"/"+str(loaded[5])+"/"+str(count)+".png",**png_info)
            selector()

    spr_decompile_but = Tkinter.Button(npc_w,text='Decompile Sprites',command=decompile_spr)
    buttons.append(spr_decompile_but)
    spr_decompile_but.place(x=20 ,y=380)

    def delete_entry():
        global update_selector,dele
        global loaded
        if loaded != [] and loaded != -1 and loaded != tuple():
            result = tkMessageBox.askquestion("Delete", "Are You Sure?", icon='warning', parent = npc_w)
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
                    ymls.insert(i,(i,"down",0x0,12,"always",1,"$0","$0","person"))
                    update_selector = True
                    add = True
                    to_add = i
                    selector()  
                    return
            if stop == 0:
                ymls.append((i+1,"down",0x0,12,"always",1,"$0","$0","person"))
                update_selector = True
                add = True
                to_add = i + 1
                selector()

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
        i = loaded[8]

        direction_t = direction.get()
        if direction_t != b:
            b = direction_t

        event_f = flag.get()
        if event_f != c:
            c = int(event_f)

        move_f = movement.get()
        if move_f != d:
            d = int(move_f)

        show_cond = show_npc.get()
        if show_cond != e:
            e = show_cond

        sprite_d = sprite.get()
        if sprite_d != f:
            f = int(sprite_d)

        code_adress_1 = text_pointer_1.get()
        if code_adress_1 != g:
            if code_adress_1.find(".") == -1:
                g = "$" + code_adress_1
            else:
                g = code_adress_1

        code_adress_2 = text_pointer_2.get()
        if code_adress_2 != h:
            if code_adress_2.find(".") == -1:
                h = "$" + code_adress_2
            else:
                h = code_adress_2

        type_g = npc_type.get()
        if type_g != i:
            i = type_g

        replaced = tuple((a,b,c,d,e,f,g,h,i))
        if replaced != loaded:
            ymls[[s[0] for s in searchable][pos]] = replaced
        return    

    def saver():
        global stuff_loaded
        global loaded
        if stuff_loaded:
            replacer()
            location = os.getcwd()
            to_dump = open(save_data + "/npc_config_table.yml",'w')
            changed_ymls = {}
            for y in ymls:
                try:
                    y_2 = hex(y[2])
                except:
                    y_2 = hex(str(y[2]))
                changed_ymls[y[0]] = {"Direction" : y[1],
                                         "Event Flag" : y[2],
                                         "Movement" : y[3],
                                         "Show Sprite" : y[4],
                                         "Sprite" : y[5],
                                         "Text Pointer 1" : y[6],
                                         "Text Pointer 2" : y[7],
                                         "Type" : y[8]}
            yaml.dump(changed_ymls, to_dump, default_flow_style=False)
        npc_w.destroy()

        w_2.remove(w_2[[w[1] for w in w_2].index("npc config")])
        stram.close()

    npc_w.protocol("WM_DELETE_WINDOW", saver)

def call_npc_config(w_2):
    
    (w_2[[w[1] for w in w_2].index("npc config")])[0].lift()


