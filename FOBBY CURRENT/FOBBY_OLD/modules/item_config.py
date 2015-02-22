import Tkinter, re, sys, yaml, tkMessageBox, os, unicodedata
sys.path.append(os.getcwd()[:-7])
import FOBBY
 
def item_config(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,path,save_data):
    global stuff_loaded
    global update_selector
    update_selector = False
    stuff_loaded = False
    global searchable
    searchable = []

    items = []

    ymls = []

    costs = []
    miscflags = []
    names = []
    help_pointers = []
    types = []
    arguments = []
    actions = []
    final_format = []
    loaded = tuple()

    global previous_l
    previous_l = -1
    global cand_l
    cand_l = -1

    global add, dele, to_add
    add = False
    dele = False
    to_add = 0
    
    global par
    par = Tkinter.StringVar()
    global fla
    fla = Tkinter.StringVar()
    global fre
    fre = Tkinter.StringVar()
    global fir
    fir = Tkinter.StringVar()

    global fix,a_move
    fix = Tkinter.StringVar()
    fix.set('fix this')
    a_move = Tkinter.StringVar()
    a_move.set("Show me ya' moves")
    
    lab = [("0", "0"),
           ("1", "1"),
           ("2", "2"),
           ("3", "3")]

    cost = Tkinter.StringVar()
    misc_flag = Tkinter.StringVar()
    u_1 = Tkinter.IntVar()
    u_2 = Tkinter.IntVar()
    u_3 = Tkinter.IntVar()
    u_4 = Tkinter.IntVar()
    u_5 = Tkinter.IntVar()
    name = Tkinter.StringVar()
    help_pointer = Tkinter.StringVar()
    selection_type = Tkinter.StringVar()
    argument = []
    global a_1
    a_1 = Tkinter.StringVar()
    global a_2
    a_2 = Tkinter.StringVar()
    global a_3
    a_3 = Tkinter.StringVar()
    global a_4
    a_4 = Tkinter.StringVar()
    a_1_d = Tkinter.StringVar()
    a_2_d = Tkinter.StringVar()
    a_3_d = Tkinter.StringVar()
    a_4_d = Tkinter.StringVar()     
    action = Tkinter.StringVar()
    

    x_path = path[:-13]
    global i_config
    i_config = Tkinter.Toplevel()
    i_config.geometry('800x864+450+150')
    windows.append(i_config)
    w_2.append((i_config,"item_config"))
    current = Tkinter.StringVar()

    global search_for_type
    search_for_type = Tkinter.StringVar()
    search_for_type.set("index")

    search_for_what = Tkinter.StringVar()
    
    global selected_type

    selected_type = Tkinter.StringVar()
    
    if os.path.exists(save_data+ "/item_configuration_table.yml"):
        stram = open(save_data+ "/item_configuration_table.yml", "r")
    else:
        r_path = x_path + "item_configuration_table.yml"
        stram = open(r_path, "r")

    yml = yaml.load(stram)
    str_yml = str(yml)
    print str_yml

    le = (re.findall(r'[0-9]+: {',str_yml))
    for l in range(len(le)):
        z = re.findall(r'[0-9]+',le[l])
        items.append(int(le[l][0:(len(str(z[0])))]))
        miscflags.append(yml[int(z[0])]['Misc Flags'])
        names.append(yml[int(z[0])]['Name'])
        actions.append(yml[int(z[0])]['Action'])
        help_pointers.append(yml[int(z[0])]['Help Text Pointer'])
        types.append(yml[int(z[0])]['Type'])
        arguments.append(yml[int(z[0])]['Argument'])
        costs.append(yml[int(z[0])]['Cost'])
        
    i = -1
    while i < (len(items)) -1:
        i += 1
        ymls.append((items[i],miscflags[i],names[i],actions[i],help_pointers[i],types[i],arguments[i],costs[i]))
    file.close(stram)
    print ymls

    selection = Tkinter.Listbox(i_config)
    listboxes.append(selection)
    i = -1
    for no in ymls:
        i += 1
        selection.insert(i, no[0])
    selection.place(x=16, y=64)

    selections_scroller = Tkinter.Scale(i_config, from_=0, to=len(ymls))
    selections_scroller.config(command=selection.yview)
    scalers.append(selections_scroller)
    selections_scroller.place(x=128 , y=80 )

    searcher = Tkinter.Entry(i_config, textvariable = search_for_what)
    entries.append(searcher)
    searcher.place(x=16, y=270)


    #Argument
    arg_1 = Tkinter.Entry(i_config, textvariable = a_1)
    entries.append(arg_1)
    arg_1.place(x = 500, y = 120)

    arg_1_t = Tkinter.Label(i_config, textvariable = a_1)
    entries.append(arg_1_t)

    arg_1_d = Tkinter.Label(i_config, textvariable = a_1_d)
    labels.append(arg_1_d)
    arg_1_d.place(x=640, y =120)
        
    arg_2 = Tkinter.Entry(i_config, textvariable = a_2)
    entries.append(arg_2)
    arg_2.place(x = 500, y = 152)

    arg_2_d = Tkinter.Label(i_config, textvariable = a_2_d)
    labels.append(arg_2_d)
    arg_2_d.place(x=640, y =152)
        
    arg_3 = Tkinter.Entry(i_config, textvariable = a_3)
    entries.append(arg_3)
    arg_3.place(x = 500, y = 184)

    arg_3_d = Tkinter.Label(i_config, textvariable = a_3_d)
    labels.append(arg_3_d)
    arg_3_d.place(x=640, y =184)
        
    arg_4 = Tkinter.Entry(i_config, textvariable = a_4)
    entries.append(arg_4)
    arg_4.place(x = 500, y = 216)

    arg_4_t = Tkinter.Label(i_config, textvariable = a_4)
    labels.append(arg_4_t)
    
    arg_4_d = Tkinter.Label(i_config, textvariable = a_4_d)
    labels.append(arg_4_d)
    arg_4_d.place(x=640, y =216)

    #Ressitance Radiobuttons

    r_r_0 = Tkinter.Radiobutton(i_config, text="0",
                                variable=par, value="0")
    radiobuttons.append(r_r_0)
    r_r_1 = Tkinter.Radiobutton(i_config, text="1",
                                variable=par, value="1")
    radiobuttons.append(r_r_1)
    r_r_2 = Tkinter.Radiobutton(i_config, text="2",
                                variable=par, value="2")
    radiobuttons.append(r_r_2)
    r_r_3 = Tkinter.Radiobutton(i_config, text="3",
                                variable=par, value="3")
    radiobuttons.append(r_r_3)
    r_r_4 = Tkinter.Radiobutton(i_config, text="0",
                                variable=fla, value="0")
    radiobuttons.append(r_r_4)
    r_r_5 = Tkinter.Radiobutton(i_config, text="1",
                                variable=fla, value="1")
    radiobuttons.append(r_r_5)
    r_r_6 = Tkinter.Radiobutton(i_config, text="2",
                                variable=fla, value="2")
    radiobuttons.append(r_r_6)
    r_r_7 = Tkinter.Radiobutton(i_config, text="3",
                                variable=fla, value="3")
    radiobuttons.append(r_r_7)
    r_r_8 = Tkinter.Radiobutton(i_config, text="0",
                                variable=fre, value="0")
    radiobuttons.append(r_r_8)
    r_r_9 = Tkinter.Radiobutton(i_config, text="1",
                                variable=fre, value="1")
    radiobuttons.append(r_r_9)
    r_r_10 = Tkinter.Radiobutton(i_config, text="2",
                                variable=fre, value="2")
    radiobuttons.append(r_r_10)
    r_r_11 = Tkinter.Radiobutton(i_config, text="3",
                                variable=fre, value="3")
    radiobuttons.append(r_r_11)
    r_r_12 = Tkinter.Radiobutton(i_config, text="0",
                                variable=fir, value="0")
    radiobuttons.append(r_r_12)
    r_r_13 = Tkinter.Radiobutton(i_config, text="1",
                                variable=fir, value="1")
    radiobuttons.append(r_r_13)
    r_r_14 = Tkinter.Radiobutton(i_config, text="2",
                                variable=fir, value="2")
    radiobuttons.append(r_r_14)
    r_r_15 = Tkinter.Radiobutton(i_config, text="3",
                                variable=fir, value="3")
    radiobuttons.append(r_r_15)

    #Recovery Types

    recovery_types = Tkinter.Listbox(i_config,height =12)
    listboxes.append(recovery_types)
    to_ins_rec = [(0,"HP"),(1,"PP"),(2,"HP & PP"),(3,"Random IQ or Luck"),(4,"IQ"),
                  (5,"Guts"),(6,"Speed"),(7,"Vitality"),(8,"Luck"),(9,"Cure Cold"),
                  (10,"Poison Cure"),(11,"Nothing")]
    for a,b in to_ins_rec:
        recovery_types.insert(a,b)

    #Bonus Stuff
    Desc_label = Tkinter.Label(i_config, text = """
Paralysis

Flash

Freeze

Fire

For sleep resistance:
Set fire to 1 or 2
And all the others to 0
""")
    labels.append(Desc_label)

    Fixed = Tkinter.Label(i_config, textvariable = fix)
    labels.append(Fixed)

    action_item_de = Tkinter.Label(i_config, textvariable = a_move)
    labels.append(action_item_de)
                  
    def selector():
        global stuff_loaded
        global loaded
        global pos
        global update_selector,add,dele,to_add
        global searchable
        global previous_l, cand_l

        searching_for = search_for_what.get()
        search_type = selected_type.get()
        selections_scroller.config(to=len(ymls))
        if stuff_loaded == True:
            replacer()
        try:
            pos = int(selection.curselection()[0])
        except IndexError:
            pos = -1

        if searching_for == "":
            searchable = [y for y in ymls]
            
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

        print[s[0] for s in searchable]
        loaded = ymls[[y[0] for y in ymls].index([s[0] for s in searchable][pos])]

        print "LOADED: " + str(loaded)
        
        if "ness can use" in loaded[1]:
            u_1.set(1)
        else:
            u_1.set(0)
        if "paula can use" in loaded[1]:
            u_2.set(1)
        else:
            u_2.set(0)
        if "jeff can use" in loaded[1]:
            u_3.set(1)
        else:
            u_3.set(0)
        if "poo can use" in loaded[1]:
            u_4.set(1)
        else:
            u_4.set(0)
        if "item disappears when used" in loaded[1]:
            u_5.set(1)
        else:
            u_5.set(0)

        name.set(loaded[2])
        
        action.set(loaded[3])

        try:
            if loaded[4].find(".") == -1:
                help_pointer.set(loaded[4][1:])
            else:
                help_pointer.set(loaded[4])

        except AttributeError:
            help_pointer.set(str(loaded[4]))

        selection_type.set((loaded[5]))
        argument = loaded[6]
        
        a_1.set(str(argument[0]))
        a_2.set(str(argument[1]))
        a_3.set(str(argument[2]))        
        a_4.set(str(argument[3]))

        cost.set(loaded[7])
        
        stuff_loaded = True
        print loaded

        current.set("You are currently editing: " + str(loaded[0]))

        try:
            c_t = int(selection_type.get())
        except ValueError:
            print ":C"
        else:
            if c_t == 0:
                a_1_d.set("Strength")
                a_2_d.set("Extra Power")
                a_3_d.set("Extra Power Increase")
                a_4_d.set("Special")
            elif c_t == 4:
                a_1_d.set("PST Entry +1")
                a_2_d.set("Extra Power")
                a_3_d.set("Extra Power Increase")
                a_4_d.set("Special")
            elif c_t == 8:
                a_1_d.set("Strength")
                a_2_d.set("Fixed Item")
                a_3_d.set("IQ Required")
                a_4_d.set("Special")
            elif c_t == 16:
                a_1_d.set("Offense")
                a_2_d.set("Guts")
                a_3_d.set("4th Character Offense")
                a_4_d.set("Miss Rate (x/16)")
            elif c_t == 17:
                a_1_d.set("Offense")
                a_2_d.set("Guts")
                a_3_d.set("4th Character Offense")
                a_4_d.set("Miss Rate (x/16)")
            elif c_t == 20:
                a_1_d.set("Defense")
                a_2_d.set("Speed")
                a_3_d.set("4th Character Defense")
                a_4_d.set("Protection Type")
            elif c_t == 24:
                a_1_d.set("Defense")
                a_2_d.set("Luck")
                a_3_d.set("4th Character Defense")
                a_4_d.set("Protection Type")
            elif c_t == 28:
                a_1_d.set("Defense")
                a_2_d.set("Luck")
                a_3_d.set("4th Character Defense")
                a_4_d.set("Protection Type")
            elif c_t == 32:
                a_1_d.set("Recovery Type")
                a_2_d.set("4th Character Amount")
                a_3_d.set("Amount")
                a_4_d.set("Skip Sandwich Effect Time")
            elif c_t == 36:
                a_1_d.set("Recovery Type")
                a_2_d.set("4th Character Amount")
                a_3_d.set("Amount")
                a_4_d.set("Skip Sandwich Effect Time")
            elif c_t == 40:
                a_1_d.set("Recovery Type")
                a_2_d.set("4th Character Amount")
                a_3_d.set("Amount")
                a_4_d.set("Skip Sandwich Effect Time")
            elif c_t == 44:
                a_1_d.set("Recovery Type")
                a_2_d.set("4th Character Amount")
                a_3_d.set("Amount")
                a_4_d.set("Skip Sandwich Effect Time")
            elif c_t == 48:
                a_1_d.set("Strength")
                a_2_d.set("Extra Power")
                a_3_d.set("Extra Power Increase")
                a_4_d.set("Special")
            elif c_t == 52:
                a_1_d.set("Strength")
                a_2_d.set("Extra Power")
                a_3_d.set("Extra Power Increase")
                a_4_d.set("Special")
            elif c_t == 53:
                a_1_d.set("Strength")
                a_2_d.set("Extra Power")
                a_3_d.set("Extra Power Increase")
                a_4_d.set("Special")
            elif c_t == 56:
                a_1_d.set("Strength")
                a_2_d.set("Extra Power")
                a_3_d.set("Extra Power Increase")
                a_4_d.set("Special")
            elif c_t == 58:
                a_1_d.set("Strength")
                a_2_d.set("Extra Power")
                a_3_d.set("Extra Power Increase")
                a_4_d.set("Special")
            elif c_t == 59:
                a_1_d.set("Strength")
                a_2_d.set("Extra Power")
                a_3_d.set("Extra Power Increase")
                a_4_d.set("Special")

            if c_t == 8:
                if Fixed.winfo_exists:
                    Fixed.place(x = 400, y = 300)
                    try:
                        fix.set(ymls[int(a_2.get())][2])
                    except IndexError:
                        fix.set("Unknown")
                    except IndexError:
                        fix.set("Unknown")
                    
                if Desc_label.winfo_exists:
                    Desc_label.place_forget()
                if r_r_0.winfo_exists:
                    r_r_0.place_forget()
                if r_r_1.winfo_exists:
                    r_r_1.place_forget()
                if r_r_2.winfo_exists:
                    r_r_2.place_forget()
                if r_r_3.winfo_exists:
                    r_r_3.place_forget()
                if r_r_4.winfo_exists:
                    r_r_4.place_forget()
                if r_r_5.winfo_exists:
                    r_r_5.place_forget()
                if r_r_6.winfo_exists:
                    r_r_6.place_forget()
                if r_r_7.winfo_exists:
                    r_r_7.place_forget()
                if r_r_8.winfo_exists:
                    r_r_8.place_forget()
                if r_r_9.winfo_exists:
                    r_r_9.place_forget()
                if r_r_10.winfo_exists:
                    r_r_10.place_forget()
                if r_r_11.winfo_exists:
                    r_r_11.place_forget()
                if r_r_12.winfo_exists:
                    r_r_12.place_forget()
                if r_r_13.winfo_exists:
                    r_r_13.place_forget()
                if r_r_14.winfo_exists:
                    r_r_14.place_forget()
                if r_r_15.winfo_exists:
                    r_r_15.place_forget()
                if arg_4_t.winfo_exists:
                    arg_4_t.place_forget()
                if arg_4.winfo_exists == False:
                    arg_4.place(x = 500, y = 216)
                if action_item_de.winfo_exists:
                    action_item_de.place_forget()
                if arg_1_t.winfo_exists:
                    arg_1_t.place_forget()
                    arg_1.place(x=500,y=120)
                    recovery_types.place_forget()
        
            elif c_t == 20 or c_t == 24 or c_t == 28:
                global par, fla, fir, fre
                print par.get(), fla.get(), fre.get(), fir.get()

                r_r_0.place(x=400,y=250)
                r_r_1.place(x=432,y=250)
                r_r_2.place(x=464,y=250)
                r_r_3.place(x=496,y=250)
                r_r_4.place(x=400,y=282)
                r_r_5.place(x=432,y=282)
                r_r_6.place(x=464,y=282)
                r_r_7.place(x=496,y=282)
                r_r_8.place(x=400,y=314)
                r_r_9.place(x=432,y=314)
                r_r_10.place(x=464,y=314)
                r_r_11.place(x=496,y=314)
                r_r_12.place(x=400,y=346)
                r_r_13.place(x=432,y=346)
                r_r_14.place(x=464,y=346)
                r_r_15.place(x=496,y=346)

                r_r_0.config(command = selector)
                r_r_1.config(command = selector)
                r_r_2.config(command = selector)
                r_r_3.config(command = selector)
                r_r_4.config(command = selector)
                r_r_5.config(command = selector)
                r_r_6.config(command = selector)
                r_r_7.config(command = selector)
                r_r_8.config(command = selector)
                r_r_9.config(command = selector)
                r_r_10.config(command = selector)
                r_r_11.config(command = selector)
                r_r_12.config(command = selector)
                r_r_13.config(command = selector)
                r_r_14.config(command = selector)
                r_r_15.config(command = selector)

                Desc_label.place(x=532, y=250)

                print a_4.get()

                print par.get(), fla.get(), fre.get(), fir.get()
                
                try:
                    if cand_l != previous_l and cand_l != loaded[0]:
                        previous_l = cand_l
                    if loaded[0] == cand_l and cand_l != previous_l:
                        a_4.set(str((int(fir.get())) + 4*int(fre.get()) + 16*int(fla.get()) + 64*int(par.get())))

                    print a_4.get()                        
                except ValueError:
                    "Hey"
                    tem = a_4.get()
                    print tem

                    par.set("0")
                    while 64*(int(par.get())-1) <= int(tem) and par.get() != "3" and int(tem) > 0 and  int(tem) - 64 >= 0:
                        par.set(str(int(par.get())+1))
                        tem =  str(int(tem)-64)
                        print tem
                        print "Par: " + par.get()


                    fla.set("0")
                    while 16*(int(fla.get())-1) <= (int(tem)) and fla.get() != "3" and int(tem)  > 0 and int(tem) - 16 >= 0:
                        fla.set(str(int(fla.get())+1))
                        tem =  str(int(tem)-16)
                        print tem
                        print "Fla: " + fla.get()

                    fre.set("0")
                    while 4*(int(fre.get())-1) <= int(tem) and fre.get() != "3" and int(tem) > 0 and int(tem) - 4 >= 0:
                        fre.set(str(int(fre.get())+1))
                        tem =  str(int(tem)-4)
                        print tem
                        print "Fre: " + fre.get()

                    fir.set("0")
                    while (int(fir.get())-1) <= int(tem) and fir.get() != "3" and int(tem)  > 0 and int(tem) - 1 >= 0:
                        fir.set(str(int(fir.get())+1))
                        tem =  str(int(tem)-1)
                        print tem
                        print "Fir: " + fir.get()
                    

                except UnboundLocalError:
                    print "Listen"
                    if loaded[0] != previous_l:
                        tem = a_4.get()
                        par.set("0")
                        while 64*(int(par.get())-1) <= int(tem) and par.get() != "3" and int(tem) > 0 and int(tem) - 64 >= 0:
                            par.set(str(int(par.get())+1))
                            tem =  str(int(tem)-64)
                            print tem
                            print "Par: " + par.get()

                        fla.set("0")
                        while 16*(int(fla.get())-1) <= (int(tem)) and fla.get() != "3" and int(tem)  > 0 and int(tem) - 16 >= 0:
                            fla.set(str(int(fla.get())+1))
                            tem =  str(int(tem)-16)
                            print tem
                            print "Fla: " + fla.get()

                        fre.set("0")
                        while 4*(int(fre.get())-1) <= int(tem) and fre.get() != "3" and int(tem) > 0 and int(tem) - 4 >= 0:
                            fre.set(str(int(fre.get())+1))
                            tem =  str(int(tem)-4)
                            print tem
                            print "Fre: " + fre.get()

                        fir.set("0")
                        while (int(fir.get())-1) <= int(tem) and fir.get() != "3" and int(tem)  > 0 and int(tem) - 1 >= 0:
                            fir.set(str(int(fir.get())+1))
                            tem =  str(int(tem)-1)
                            print tem
                            print "Fir: " + fir.get()
                        
                else:
                    print a_4.get()
                    if loaded[0] != previous_l:
                        print "Wash Out!" 
                        tem = a_4.get()
                        par.set("0")
                        while 64*(int(par.get())-1) <= int(tem) and par.get() != "3" and int(tem) > 0 and int(tem) - 64 >= 0:
                            par.set(str(int(par.get())+1))
                            tem =  str(int(tem)-64)
                            print tem
                            print "Par: " + par.get()

                        fla.set("0")
                        while 16*(int(fla.get())-1) <= (int(tem)) and fla.get() != "3" and int(tem)  > 0 and int(tem) - 16>= 0:
                            fla.set(str(int(fla.get())+1))
                            tem =  str(int(tem)-16)
                            print tem
                            print "Fla: " + fla.get()

                        fre.set("0")
                        while 4*(int(fre.get())-1) <= int(tem) and fre.get() != "3" and int(tem) > 0 and int(tem) - 4 >= 0:
                            fre.set(str(int(fre.get())+1))
                            tem =  str(int(tem)-4)
                            print tem
                            print "Fre: " + fre.get()

                        fir.set("0")
                        while (int(fir.get())-1) <= int(tem) and fir.get() != "3" and int(tem)  > 0 and int(tem) - 1 >= 0:
                            fir.set(str(int(fir.get())+1))
                            tem =  str(int(tem)-1)
                            print tem
                            print "Fir: " + fir.get()             

                print par.get(), fla.get(), fre.get(), fir.get()
                
                if arg_4_t.winfo_exists:
                    arg_4_t.place(x = 500, y = 216)
                if arg_4.winfo_exists:
                    arg_4.place_forget()
                if arg_1_t.winfo_exists:
                    arg_1_t.place_forget()
                    arg_1.place(x=500,y=120)
                    recovery_types.place_forget()
                if Fixed.winfo_exists:
                    Fixed.place_forget()
                if action_item_de.winfo_exists:
                    action_item_de.place_forget()
                print a_4.get()

            elif c_t == 32 or c_t == 36 or c_t == 40 or c_t == 44:
                h_type = a_1.get()
                recovery_types.place(x=500,y= 500)

                print recovery_types.curselection()

                try:
                    print recovery_types.curselection()
                    print loaded
                    heal_type = recovery_types.curselection()[0]
                    print heal_type
                    a_1.set(heal_type)
                    print (str(argument[0]))
                except IndexError:
                    print "FAIL"

                def rec_click(event):
                    try:
                        print recovery_types.curselection()
                        print loaded
                        heal_type = recovery_types.curselection()[0]
                        print heal_type
                        a_1.set(heal_type)
                        print (str(argument[0]))
                    except IndexError:
                        print "FAIL"
                recovery_types.bind("<<ListboxSelect>>", rec_click)


                                
                if arg_1.winfo_exists():
                    arg_1_t.place(x=500, y =120)
                    arg_1.place_forget()

                try:
                    if r_r_0.winfo_exists:
                        r_r_0.place_forget()
                    if r_r_1.winfo_exists:
                        r_r_1.place_forget()
                    if r_r_2.winfo_exists:
                        r_r_2.place_forget()
                    if r_r_3.winfo_exists:
                        r_r_3.place_forget()
                    if r_r_4.winfo_exists:
                        r_r_4.place_forget()
                    if r_r_5.winfo_exists:
                        r_r_5.place_forget()
                    if r_r_6.winfo_exists:
                        r_r_6.place_forget()
                    if r_r_7.winfo_exists:
                        r_r_7.place_forget()
                    if r_r_8.winfo_exists:
                        r_r_8.place_forget()
                    if r_r_9.winfo_exists:
                        r_r_9.place_forget()
                    if r_r_10.winfo_exists:
                        r_r_10.place_forget()
                    if r_r_11.winfo_exists:
                        r_r_11.place_forget()
                    if r_r_12.winfo_exists:
                        r_r_12.place_forget()
                    if r_r_13.winfo_exists:
                        r_r_13.place_forget()
                    if r_r_14.winfo_exists:
                        r_r_14.place_forget()
                    if r_r_15.winfo_exists:
                        r_r_15.place_forget()
                    if arg_4_t.winfo_exists:
                        arg_4_t.place_forget()
                    if arg_4.winfo_exists:
                        arg_4.place(x = 500, y = 216)
                    if Desc_label.winfo_exists:
                        Desc_label.place_forget()
                    if Fixed.winfo_exists:
                        Fixed.place_forget()
                        
                except NameError:
                    print "No problem here"

                if action_item_de.winfo_exists:
                    action_item_de.place_forget()

            elif c_t == 52 or c_t == 53:
                if action_item_de.winfo_exists:
                    action_item_de.place(x=400, y =250)

                    if os.path.exists(os.getcwd()+ "/tempsave/battle_action_table.yml"):
                        strem = open(os.getcwd() + "/tempsave/battle_action_table.yml", "r")
                    else:
                        r_path = x_path + "battle_action_table.yml"
                        strem = open(r_path, "r")
                    yml_2 = yaml.load(strem)
                    found = False
                    for y in yml_2:
                        if y == loaded[4]:
                            addr = yml_2[y]['Code Address']
                            found = True
                    if not found:
                        addr = "Unknown"
                    print addr
                    strem.close()
                    
                    a_move.set("Adress: " + addr)

                    
                if r_r_0.winfo_exists:
                    r_r_0.place_forget()
                if r_r_1.winfo_exists:
                    r_r_1.place_forget()
                if r_r_2.winfo_exists:
                    r_r_2.place_forget()
                if r_r_3.winfo_exists:
                    r_r_3.place_forget()
                if r_r_4.winfo_exists:
                    r_r_4.place_forget()
                if r_r_5.winfo_exists:
                    r_r_5.place_forget()
                if r_r_6.winfo_exists:
                    r_r_6.place_forget()
                if r_r_7.winfo_exists:
                    r_r_7.place_forget()
                if r_r_8.winfo_exists:
                    r_r_8.place_forget()
                if r_r_9.winfo_exists:
                    r_r_9.place_forget()
                if r_r_10.winfo_exists:
                    r_r_10.place_forget()
                if r_r_11.winfo_exists:
                    r_r_11.place_forget()
                if r_r_12.winfo_exists:
                    r_r_12.place_forget()
                if r_r_13.winfo_exists:
                    r_r_13.place_forget()
                if r_r_14.winfo_exists:
                    r_r_14.place_forget()
                if r_r_15.winfo_exists:
                    r_r_15.place_forget()
                if arg_4_t.winfo_exists:
                    arg_4_t.place_forget()
                if arg_4.winfo_exists == False:
                    arg_4.place(x = 500, y = 216)
                if Desc_label.winfo_exists:
                    Desc_label.place_forget()
                if Fixed.winfo_exists:
                    Fixed.place_forget()
            else:
                try:
                    if action_item_de.winfo_exists:
                        action_item_de.place_forget()
                        
                    if r_r_0.winfo_exists:
                        r_r_0.place_forget()
                    if r_r_1.winfo_exists:
                        r_r_1.place_forget()
                    if r_r_2.winfo_exists:
                        r_r_2.place_forget()
                    if r_r_3.winfo_exists:
                        r_r_3.place_forget()
                    if r_r_4.winfo_exists:
                        r_r_4.place_forget()
                    if r_r_5.winfo_exists:
                        r_r_5.place_forget()
                    if r_r_6.winfo_exists:
                        r_r_6.place_forget()
                    if r_r_7.winfo_exists:
                        r_r_7.place_forget()
                    if r_r_8.winfo_exists:
                        r_r_8.place_forget()
                    if r_r_9.winfo_exists:
                        r_r_9.place_forget()
                    if r_r_10.winfo_exists:
                        r_r_10.place_forget()
                    if r_r_11.winfo_exists:
                        r_r_11.place_forget()
                    if r_r_12.winfo_exists:
                        r_r_12.place_forget()
                    if r_r_13.winfo_exists:
                        r_r_13.place_forget()
                    if r_r_14.winfo_exists:
                        r_r_14.place_forget()
                    if r_r_15.winfo_exists:
                        r_r_15.place_forget()
                    if Desc_label.winfo_exists:
                        Desc_label.place_forget()
                        
                    if arg_4_t.winfo_exists:
                        arg_4_t.place_forget()
                    if arg_4.winfo_exists:
                        arg_4.place(x = 500, y = 216)
                    if arg_1_t.winfo_exists:
                        arg_1_t.place_forget()
                        arg_1.place(x=500,y=120)
                        recovery_types.place_forget()
                    if Fixed.winfo_exists:
                        Fixed.place_forget()

                except NameError:
                    print "No problem here"

            
            cand_l = loaded[0]
            print previous_l, loaded[0], cand_l

    def find_pos(event):
        selector()
    selection.bind("<<ListboxSelect>>", find_pos)

    #Important 1
    arg_2.bind("<KeyRelease>", find_pos)

    def searchable_mod():
        global searchable
        global update_selector
        searching_for = search_for_what.get()
        search_type = search_for_type.get()
        if searching_for != "":
            selection.delete(0,'end')
            if search_type == "index":
                searchable = [y for y in ymls if str(y[0]).find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, s[0])
            elif search_type == "name":
                searchable = [y for y in ymls if y[2].find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, str(s[0]) + ' (' + str(s[2]) + ')')

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
        ("By Name", "name")]    

    z = 290
    for text, typ in searchable_as:
        search_radio = Tkinter.Radiobutton(i_config, text=text,
                     var=search_for_type, value=typ)
        search_radio.place(x=16,y=z)
        radiobuttons.append(search_radio)
        search_radio.bind("<ButtonPress-1>", searchable_modify)
        z += 32

    #Cost
    price = Tkinter.Entry(i_config, textvariable = cost)
    entries.append(price)
    price.place(x = 280, y = 112)
    cost_label = Tkinter.Label(i_config, text = 'Cost:')
    labels.append(cost_label)
    cost_label.place(x=200 , y=112 )

    #Miscflag
    flag_label = Tkinter.Label(i_config, text = 'Misc_flags:')
    labels.append(flag_label)
    flag_label.place(x=400+50 , y=80+128+64 )

    checbox_1 = Tkinter.Checkbutton(i_config, variable = u_1, text = "Ness can use")
    checbox_1.place(x=450, y = 112+128+64)
    checkbuttons.append(checbox_1)
    checbox_2 = Tkinter.Checkbutton(i_config, variable = u_2, text = "Paula can use")
    checbox_2.place(x=450, y = 144+128+64)
    checkbuttons.append(checbox_2)
    checbox_3 = Tkinter.Checkbutton(i_config, variable = u_3, text = "Jeff can use")
    checbox_3.place(x=450, y = 176+128+64)
    checkbuttons.append(checbox_3)
    checbox_4 = Tkinter.Checkbutton(i_config, variable = u_4, text = "Poo can use")
    checbox_4.place(x=450, y = 208+128+64)
    checkbuttons.append(checbox_4)
    checbox_5 = Tkinter.Checkbutton(i_config, variable = u_5, text = "One Use")
    checbox_5.place(x=450, y = 208+128+64+32)
    checkbuttons.append(checbox_5)

    #Name
    nameget = Tkinter.Entry(i_config, textvariable = name)
    entries.append(nameget)
    nameget.place(x = 280, y = 144)
    name_label = Tkinter.Label(i_config, text = 'Name:')
    labels.append(name_label)
    name_label.place(x=200 , y=144 )

    #HELP TEXT(meow)
    help_t = Tkinter.Entry(i_config, textvariable = help_pointer)
    entries.append(help_t)
    help_t.place(x = 300, y = 176)
    h_label = Tkinter.Label(i_config, text = 'Help Text Pointer:')
    labels.append(h_label)
    h_label.place(x=200 , y=176 )

    # TYPE
    types = [
        ("Franklin Badge", "0"),
        ("Teddy Bears", "4"),
        ("Broken Items", "8"),
        ("Melee Weapons", "16"),
        ("Ranged Weapons(yo-yo and slingshots)", "17"),
        ("Items Equipped On The Body", "20"),
        ("Items Equipped On The Arms", "24"),
        ("Items Equipped in The 'Other' Section", "28"),
        ("Foods", "32"),
        ("Beverage and Capsules", "36"),
        ("Condiments", "40"),
        ("Edible Food For All Characters(Such as Large Pizza)", "44"),
        ("Items With Special Properties", "48"),
        ("Battle items", "52"),
        ("Random Items in Battle(Fly Honey, Defense Shower, Sudden Guts Pill)", "53"),
        ("Items used outside of battle(Pencil Eraser)", "56"),
        ("Random Items out of Battle(Hawk Eye, Bicycle, Zombie Paper)", "58"),
        ("Key Items(can't be dropped)", "59")]

    y = 250
    for text, typ in types:
        type_radio = Tkinter.Radiobutton(i_config, text=text,
                     variable=selection_type, value=typ, command = selector)
        type_radio.place(x=200,y=y)
        radiobuttons.append(type_radio)
        y += 32


    types = Tkinter.Label(i_config, text = 'Type:')
    labels.append(types)
    types.place(x=200 , y=224)
        
    #Effect
    ac = Tkinter.Entry(i_config, textvariable = action)
    entries.append(ac)
    ac.place(x = 280, y = 208)
    ac_label = Tkinter.Label(i_config, text = 'Action:')
    labels.append(ac_label)
    ac_label.place(x=200 , y=208 )



    def delete_entry():
        global update_selector,dele
        global loaded
        if loaded != [] and loaded != -1 and loaded != tuple():
            result = tkMessageBox.askquestion("Delete", "Are You Sure?", icon='warning', parent = i_config)
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
                    ymls.insert(i,(i,['ness can use', 'paula can use', 'jeff can use', 'poo can use'],"NO NAME","0","none.none","0",[0,0,0,0],"0"))
                    update_selector = True
                    add = True
                    to_add = i
                    selector()
                    return
            if stop == 0:
                ymls.append((i+1,['ness can use', 'paula can use', 'jeff can use', 'poo can use'],"NO NAME","0","none.none","0",[0,0,0,0],"0"))
                update_selector = True
                add = True
                to_add = i + 1
                selector()
            
            

    delete_button = Tkinter.Button(i_config, command = delete_entry, text= "Delete Entry")
    buttons.append(delete_button)
    delete_button.place(x= 16, y = 32)
    add_button = Tkinter.Button(i_config, command = add_entry, text = "Add Entry")
    buttons.append(add_button)
    add_button.place(x= 90, y = 32)
    
    #Tracker
    current_pos = Tkinter.Label(i_config, textvariable = current)
    labels.append(current_pos)
    current_pos.place(x = 420, y = 100)

    def replacer():
        global stuff_loaded
        global selected_type
        global pk_text
        global loaded
        print loaded
        a = loaded[0]
        b = loaded[1]
        c = loaded[2]
        d = loaded[3]
        e = loaded[4]
        f = loaded[5]
        g = loaded[6]
        h = loaded[7]


        misc_flags_for = []
        if u_1.get() == 1:
            misc_flags_for.append('ness can use')
        if u_2.get() == 1:
            misc_flags_for.append('paula can use')
        if u_3.get() == 1:
            misc_flags_for.append('jeff can use')
        if u_4.get() == 1:
            misc_flags_for.append('poo can use')
        if u_5.get() ==5:
            misc_flags_for.append('item disappears when used')
            
        if misc_flags_for != b:
            b = misc_flags_for

        n = name.get()
        if n != c:
            c = n

        act = action.get()
        if act != d:
            d = act
        
        h_pointer = help_pointer.get()
        if h_pointer != e:
            if h_pointer.find(".") == -1: 
                e =  "$" + str(h_pointer)
            else:
                e = str(h_pointer)

        s_type = selection_type.get()
        if int(s_type) != f:
            f = int(s_type)

        try:    
            argument_a = int(a_1.get())
        except ValueError:
            argument_a = 0
        try:
            argument_b = int(a_2.get())
        except ValueError:
            argument_b = 0
        try:   
            argument_c = int(a_3.get())
        except ValueError:
            argument_c = 0
        try:   
            argument_d = int(a_4.get())
        except ValueError:
            argument_d = 0

        argument_list = [argument_a,argument_b,argument_c,argument_d]

        if argument_list != g:
            g = argument_list

        cost_for = cost.get()
        if int(cost_for) != h:
            h = int(cost_for)

        replaced = tuple((a,b,c,d,e,f,g,h))
        if replaced != loaded:
            ymls[pos] = replaced
        return

    def saver():
        global stuff_loaded
        global pk_text
        global loaded
        if stuff_loaded:
            replacer()
            location = os.getcwd()
            to_dump = open(save_data + "/item_configuration_table.yml",'w')
            changed_ymls = {}
            for y in ymls:
                changed_ymls[int(y[0])] = {"Misc Flags" : y[1],
                                         "Name" : y[2],
                                         "Action" : y[3],
                                         "Help Text Pointer" : y[4],
                                         "Type" : y[5],
                                         "Argument" : y[6],
                                         "Cost" : y[7]}
            yaml.dump(changed_ymls, to_dump, default_flow_style=False)
        i_config.destroy()
        
        w_2.remove(w_2[[w[1] for w in w_2].index("item_config")])
        stram.close()

    i_config.protocol("WM_DELETE_WINDOW", saver)

def call_item_config(w_2):
    (w_2[[w[1] for w in w_2].index("item_config")])[0].lift()




