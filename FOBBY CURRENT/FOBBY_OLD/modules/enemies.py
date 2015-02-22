import Tkinter, re, sys, yaml, tkMessageBox, os, unicodedata, os.path
from PIL import Image, ImageTk
from tkFileDialog import *
sys.path.append(os.getcwd()[:-7])
import FOBBY

def digit_conversion(integer):
    string = str(integer)
    if len(string) == 1:
        string = "00" + str(integer)
    elif len(string) == 2:
        string = "0" + str(integer)
    return string
 
def enemies_c(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,path,save_data):
    global stuff_loaded
    global pk_text
    global update_selector
    update_selector = False
    stuff_loaded = False
    global searchable
    searchable = []
    ymls = []
    global enemy_sprite_final,enemy_sprite,sprite_path,real_sprite

    enemys = []
    the_flags = []
    
    action_1s = []
    action_1_args = []
    action_2s = []
    action_2_args = []
    action_3s = []
    action_3_args = []
    action_4s = []
    action_4_args = []
    action_orders = []
    
    boss_flags = []
    death_sounds = []
    death_texts = []
    defenses = []
    encounter_texts = []
    xps = []

    final_actions = []
    final_action_args = []
    fire_vuls = []
    flash_vuls = []
    freeze_vuls = []

    genders = []
    gutses = []
    hps = []
    hyp_vuls = []
    init_stats = []
    drops = []
    drop_rates = []

    levels = []
    lucks = []
    max_calls = []
    mirror_rates = []
    miss_rates = []

    moneys = []
    move_pats = []
    musics = []
    names = []
    offenses = []
    overworld_sprites = []
    pps = []
    par_vuls = []
    rows = []
    run_flags = []
    speeds = []
    e_types = []
    unknowns = []

    global sprites
    sprites = {}

    loaded = tuple()
    

    the_flag = Tkinter.IntVar()
    
    action_1 = Tkinter.StringVar()
    action_1_arg = Tkinter.StringVar()
    action_2 = Tkinter.StringVar()
    action_2_arg = Tkinter.StringVar()
    action_3 = Tkinter.StringVar()
    action_3_arg = Tkinter.StringVar()
    action_4 = Tkinter.StringVar()
    action_4_arg = Tkinter.StringVar()
    action_order = Tkinter.StringVar()
    
    boss_flag = Tkinter.IntVar()
    death_sound = Tkinter.StringVar()
    death_text = Tkinter.StringVar()
    defense = Tkinter.StringVar()
    encounter_text = Tkinter.StringVar()
    xp = Tkinter.StringVar()

    final_action = Tkinter.StringVar()
    final_action_arg = Tkinter.StringVar()
    fire_vul = Tkinter.StringVar()
    flash_vul = Tkinter.StringVar()
    freeze_vul = Tkinter.StringVar()

    gender = Tkinter.StringVar()
    guts = Tkinter.StringVar()
    hp = Tkinter.StringVar()
    hyp_vul = Tkinter.StringVar()
    init_stat = Tkinter.StringVar()
    drop = Tkinter.StringVar()
    drop_rate = Tkinter.StringVar()

    level = Tkinter.StringVar()
    luck = Tkinter.StringVar()
    max_call = Tkinter.StringVar()
    mirror_rate = Tkinter.StringVar()
    miss_rate = Tkinter.StringVar()

    money = Tkinter.StringVar()
    move_pat = Tkinter.StringVar()
    music = Tkinter.StringVar()
    name = Tkinter.StringVar()
    offense = Tkinter.StringVar()
    overworld_sprite = Tkinter.StringVar()
    pp = Tkinter.StringVar()
    par_vul = Tkinter.StringVar()
    row = Tkinter.StringVar()
    run_flag = Tkinter.IntVar()
    speed = Tkinter.StringVar()
    e_type = Tkinter.StringVar()
    unknown = Tkinter.StringVar()

    drop_item_name = Tkinter.StringVar()

    sprite_path = ""
    
    x_path = path[:-13]
    enemy_c = Tkinter.Toplevel()
    enemy_c.geometry('1450x800+50+0')
    
    windows.append(enemy_c)
    w_2.append((enemy_c,"Enemy Config"))
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

    print save_data
    if os.path.exists(save_data+ "/enemy_configuration_table.yml"):
        stram = open(save_data+ "/enemy_configuration_table.yml", "r")
    else:
        r_path = x_path + "enemy_configuration_table.yml"
        stram = open(r_path, "r")

    yml = yaml.load(stram)
    str_yml = str(yml)
    le = (re.findall(r'[0-9]+: {',str_yml))
    for l in range(len(le)):
        z = re.findall(r'[0-9]+',le[l])
        enemys.append(int(le[l][0:(len(str(z[0])))]))
        
        the_flags.append(yml[int(z[0])]['"The" Flag'])
        action_1s.append(yml[int(z[0])]["Action 1"])
        action_1_args.append(yml[int(z[0])]["Action 1 Argument"])
        action_2s.append(yml[int(z[0])]["Action 2"])
        action_2_args.append(yml[int(z[0])]["Action 2 Argument"])
        action_3s.append(yml[int(z[0])]["Action 3"])
        action_3_args.append(yml[int(z[0])]["Action 3 Argument"])
        action_4s.append(yml[int(z[0])]["Action 4"])
        action_4_args.append(yml[int(z[0])]["Action 4 Argument"])
        action_orders.append(yml[int(z[0])]["Action Order"])
        boss_flags.append(yml[int(z[0])]["Boss Flag"])
        death_sounds.append(yml[int(z[0])]["Death Sound"])
        death_texts.append(yml[int(z[0])]["Death Text Pointer"])
        defenses.append(yml[int(z[0])]["Defense"])
        encounter_texts.append(yml[int(z[0])]["Encounter Text Pointer"])
        xps.append(yml[int(z[0])]["Experience points"])
        final_actions.append(yml[int(z[0])]["Final Action"])
        final_action_args.append(yml[int(z[0])]["Final Action Argument"])
        fire_vuls.append(yml[int(z[0])]["Fire vulnerability"])
        flash_vuls.append(yml[int(z[0])]["Flash vulnerability"])
        freeze_vuls.append(yml[int(z[0])]["Freeze vulnerability"])
        genders.append(yml[int(z[0])]["Gender"])
        gutses.append(yml[int(z[0])]["Guts"])
        hps.append(yml[int(z[0])]["HP"])
        hyp_vuls.append(yml[int(z[0])]["Hypnosis/Brainshock vulnerability"])
        init_stats.append(yml[int(z[0])]["Initial Status"])
        drops.append(yml[int(z[0])]["Item Dropped"])
        drop_rates.append(yml[int(z[0])]["Item Rarity"])
        levels.append(yml[int(z[0])]["Level"])
        lucks.append(yml[int(z[0])]["Luck"])
        max_calls.append(yml[int(z[0])]["Max Call"])
        mirror_rates.append(yml[int(z[0])]["Mirror Success Rate"])
        miss_rates.append(yml[int(z[0])]["Miss Rate"])
        moneys.append(yml[int(z[0])]["Money"])
        move_pats.append(yml[int(z[0])]["Movement pattern"])
        musics.append(yml[int(z[0])]["Music"])
        names.append(yml[int(z[0])]["Name"])
        offenses.append(yml[int(z[0])]["Offense"])
        overworld_sprites.append(yml[int(z[0])]["Overworld Sprite"])
        pps.append(yml[int(z[0])]["PP"])
        par_vuls.append(yml[int(z[0])]["Paralysis vulnerability"])
        rows.append(yml[int(z[0])]["Row"])
        run_flags.append(yml[int(z[0])]["Run Flag"])
        speeds.append(yml[int(z[0])]["Speed"])
        e_types.append(yml[int(z[0])]["Type"])
        unknowns.append(yml[int(z[0])]["Unknown"])
        
    i = -1
    while i < (len(the_flags)) -1:
        i += 1
        ymls.append((enemys[i],the_flags[i],action_1s[i],action_1_args[i],action_2s[i],action_2_args[i],action_3s[i],
                     action_3_args[i],action_4s[i],action_4_args[i],action_orders[i],boss_flags[i],death_sounds[i],
                     death_texts[i],defenses[i],encounter_texts[i],xps[i],final_actions[i],final_action_args[i],
                     fire_vuls[i],flash_vuls[i],freeze_vuls[i],genders[i],gutses[i],hps[i],hyp_vuls[i],init_stats[i],
                     drops[i],drop_rates[i],levels[i],lucks[i],max_calls[i],mirror_rates[i],miss_rates[i],moneys[i],
                     move_pats[i],musics[i],names[i],offenses[i],overworld_sprites[i],pps[i],par_vuls[i],rows[i],run_flags[i],
                     speeds[i],e_types[i],unknowns[i]))
    file.close(stram)
    searchable = [y for y in ymls]

    selection = Tkinter.Listbox(enemy_c)
    listboxes.append(selection)
    for l in range(len(ymls)):
        selection.insert(l, ymls[l][0])
    selection.place(x=16, y=64)

    selections_scroller = Tkinter.Scale(enemy_c, from_=0, to=len(ymls))
    selections_scroller.config(command=selection.yview)
    scalers.append(selections_scroller)
    selections_scroller.place(x=128 , y=80 )

    searcher = Tkinter.Entry(enemy_c, textvariable = search_for_what)
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

        the_flag.set(loaded[1])
        action_1.set(loaded[2])
        action_1_arg.set(loaded[3])
        action_2.set(loaded[4])
        action_2_arg.set(loaded[5])
        action_3.set(loaded[6])
        action_3_arg.set(loaded[7])
        action_4.set(loaded[8])
        action_4_arg.set(loaded[9])
        action_order.set(loaded[10])       
        boss_flag.set(loaded[11])
        death_sound.set(loaded[12])

        if loaded[13].find(".") == -1:
            death_text.set(loaded[13][1:])
        else:
            death_text.set(loaded[13])
            
        defense.set(loaded[14])

        print loaded[15]
        if str(loaded[15]).find(".") == -1:
            encounter_text.set(loaded[15][1:])
        else:
            encounter_text.set(loaded[15])
            
        xp.set(loaded[16])
        final_action.set(loaded[17])
        final_action_arg.set(loaded[18])
        fire_vul.set(str(loaded[19])[:-1])
        flash_vul.set(str(loaded[20])[:-1])
        freeze_vul.set(str(loaded[21])[:-1])
        gender.set(loaded[22])
        guts.set(loaded[23])
        hp.set(loaded[24])
        hyp_vul.set(str(loaded[25])[:-1])
        init_stat.set(loaded[26])
        drop.set(loaded[27])
        drop_rate.set(loaded[28])
        level.set(loaded[29])
        luck.set(loaded[30])
        max_call.set(loaded[31])
        mirror_rate.set(loaded[32])
        miss_rate.set(loaded[33])
        money.set(loaded[34])
        move_pat.set(loaded[35])
        music.set(loaded[36])
        name.set(loaded[37])
        offense.set(loaded[38])
        overworld_sprite.set(loaded[39])
        pp.set(loaded[40])
        par_vul.set(str(loaded[41])[:-1])
        row.set(loaded[42])
        run_flag.set(loaded[43]-6)
        speed.set(loaded[44])
        e_type.set(loaded[45])
        unknown.set(loaded[46])

        print loaded

        stuff_loaded = True

        current.set("You are currently editing: " + str(loaded[0]))
                
        print digit_conversion(loaded[0])
        if os.path.exists(save_data + "/BattleSprites/" + digit_conversion(loaded[0]) +".png"):
            global enemy_sprite_final,enemy_sprite,sprite_path,real_sprite

            real_sprite = True
            
            sprite_path = save_data + "/BattleSprites/" + digit_conversion(loaded[0]) +".png"



            enemy_sprite = Image.open(sprite_path)



            enemy_sprite_final = ImageTk.PhotoImage(enemy_sprite)
                
            spr_lab.config(image = enemy_sprite_final,text = "")

            print sprite_path, enemy_sprite, enemy_sprite_final

            spr_but_del.place(x = 1325, y = 20)


        elif os.path.exists(x_path + "BattleSprites/" + digit_conversion(loaded[0]) +".png"):
            global enemy_sprite_final,enemy_sprite,sprite_path,real_sprite

            real_sprite = True
            sprite_path = x_path + "BattleSprites/" + digit_conversion(loaded[0]) +".png"

            enemy_sprite = Image.open(sprite_path)

            enemy_sprite_final = ImageTk.PhotoImage(enemy_sprite)
                
            spr_lab.config(image = enemy_sprite_final,text = "")

            print sprite_path, enemy_sprite, enemy_sprite_final

            spr_but_del.place(x = 1325, y = 20)

        else:
            sprite_path = save_data + "/BattleSprites/" + digit_conversion(loaded[0]) +".png"
            real_sprite = False
            spr_lab.config(image = "" ,text = "Sorry, this enemy has no sprite")

            if spr_but_del.winfo_exists():
                spr_but_del.place_forget()

        spr_but_rep.place(x = 1275, y = 20)

        print(sprite_path)

        if os.path.exists(save_data+ "/item_configuration_table.yml"):
            strem = open(save_data+ "/item_configuration_table.yml", "r")
            item_yml = yaml.load(strem)
        else:
            r_path = x_path + "item_configuration_table.yml"
            strem = open(r_path, "r")
            item_yml = yaml.load(strem)

        print strem

        item_names = {item:item_yml[item]['Name'] for item in item_yml}

        try:
            drop_item_name.set(str(item_names[int(drop.get())]))
        except IndexError:
            drop_item_name.set("Error: Unknown")
            
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
            elif search_type == "name":
                searchable = [y for y in ymls if y[37].find(searching_for) > -1]
                i = -1
                for s in searchable:
                    i += 1
                    selection.insert(i, str(s[0]) + ' (' + str(s[37]) + ')')
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

    y = 290
    for text, typ in searchable_as:
        search_radio = Tkinter.Radiobutton(enemy_c, text=text,
                     var=search_for_type, value=typ)
        search_radio.place(x=16,y=y)
        radiobuttons.append(search_radio)
        search_radio.bind('<Button-1>',searchable_modify)
        y += 32
        
    #The Flags:

    flag_check = Tkinter.Checkbutton(enemy_c, variable = the_flag, text = "The Flag")
    checkbuttons.append(flag_check)

    flag_check.place(x = 200, y = 32)

    boss_check = Tkinter.Checkbutton(enemy_c, variable = boss_flag, text = "Boss Flag")
    checkbuttons.append(boss_check)

    boss_check.place(x = 200, y = 64)

    #Actions
        
    act_1 = Tkinter.Entry(enemy_c, textvariable = action_1)
    entries.append(act_1)
    act_1.place(x = 240, y = 160)
    act_1_t = Tkinter.Label(enemy_c, text = 'Action 1:')
    labels.append(act_1_t)
    act_1_t.place(x=160 , y=160)
    act_1_arg = Tkinter.Entry(enemy_c, textvariable = action_1_arg)
    entries.append(act_1_arg)
    act_1_arg.place(x = 450, y = 160)
    act_1_arg_t = Tkinter.Label(enemy_c, text = 'Argument:')
    labels.append(act_1_arg_t)
    act_1_arg_t.place(x=370 , y=160)

    act_2 = Tkinter.Entry(enemy_c, textvariable = action_2)
    entries.append(act_2)
    act_2.place(x = 240, y = 192)
    act_2_t = Tkinter.Label(enemy_c, text = 'Action 2:')
    labels.append(act_2_t)
    act_2_t.place(x=160 , y=192)
    act_2_arg = Tkinter.Entry(enemy_c, textvariable = action_2_arg)
    entries.append(act_2_arg)
    act_2_arg.place(x = 450, y = 192)
    act_2_arg_t = Tkinter.Label(enemy_c, text = 'Argument:')
    labels.append(act_2_arg_t)
    act_2_arg_t.place(x=370 , y=192)

    act_3 = Tkinter.Entry(enemy_c, textvariable = action_3)
    entries.append(act_3)
    act_3.place(x = 240, y = 224)
    act_3_t = Tkinter.Label(enemy_c, text = 'Action 3:')
    labels.append(act_3_t)
    act_3_t.place(x=160 , y=224)
    act_3_arg = Tkinter.Entry(enemy_c, textvariable = action_3_arg)
    entries.append(act_3_arg)
    act_3_arg.place(x = 450, y = 224)
    act_3_arg_t = Tkinter.Label(enemy_c, text = 'Argument:')
    labels.append(act_3_arg_t)
    act_3_arg_t.place(x=370 , y=224)

    act_4 = Tkinter.Entry(enemy_c, textvariable = action_4)
    entries.append(act_4)
    act_4.place(x = 240, y = 256)
    act_4_t = Tkinter.Label(enemy_c, text = 'Action 4:')
    labels.append(act_4_t)
    act_4_t.place(x=160 , y=256)
    act_4_arg = Tkinter.Entry(enemy_c, textvariable = action_4_arg)
    entries.append(act_4_arg)
    act_4_arg.place(x = 450, y = 256)
    act_4_arg_t = Tkinter.Label(enemy_c, text = 'Argument:')
    labels.append(act_4_arg_t)
    act_4_arg_t.place(x=370 , y=256)

    act_f = Tkinter.Entry(enemy_c, textvariable = final_action)
    entries.append(act_f)
    act_f.place(x = 240, y = 288)
    act_f_t = Tkinter.Label(enemy_c, text = 'Final Action:')
    labels.append(act_f_t)
    act_f_t.place(x=160 , y=288)
    act_f_arg = Tkinter.Entry(enemy_c, textvariable = final_action_arg)
    entries.append(act_f_arg)
    act_f_arg.place(x = 450, y = 288)
    act_f_arg_t = Tkinter.Label(enemy_c, text = 'Argument:')
    labels.append(act_f_arg_t)
    act_f_arg_t.place(x=370 , y=288)

    orders =[("Random", "0"),("1, %50; 2, %25; 3 and 4, %12.5", "1"),
             ("In order", "2"),("1 or 2 on odd turn; 3 or 4 on even turn", "3")]

    y = 288 + 96 - 32
    for text, typ in orders:
        order_radio = Tkinter.Radiobutton(enemy_c, text=text,
                     variable=action_order, value=typ)
        order_radio.place(x=160,y=y)
        radiobuttons.append(order_radio)
        y += 32

    order_lab = Tkinter.Label(enemy_c, text = 'Action Order:')
    labels.append(order_lab)
    order_lab.place(x=160 ,y=288+64 - 32)

    #ENCOUNTER TEXT

    enc_text_ent = Tkinter.Entry(enemy_c, textvariable = encounter_text)
    entries.append(enc_text_ent)
    enc_text_ent.place(x = 290, y = 288+64+64+64)
    enc_text_lab = Tkinter.Label(enemy_c, text = 'Encounter Text Adress:')
    labels.append(enc_text_lab)
    enc_text_lab.place(x=160 , y=288+64+64+64)
    

    ###DEATH

    death_text_ent = Tkinter.Entry(enemy_c, textvariable = death_text)
    entries.append(death_text_ent)
    death_text_ent.place(x = 290, y = 288+64+64+64+64-32)
    death_text_lab = Tkinter.Label(enemy_c, text = 'Death Text Adress:')
    labels.append(death_text_lab)
    death_text_lab.place(x=160 , y=288+64+64+64+32)

    death_sound_lab = Tkinter.Label(enemy_c, text = "Boss Death Sound(Kills all enemies on defeat)")
    labels.append(death_sound_lab)
    death_sound_lab.place(x = 160, y = 288+256)
    
    d_sounds =[("Normal", "normal"),("Boss", "boss")]

    y=288+256+32
    for text, typ in d_sounds:
        death_radio = Tkinter.Radiobutton(enemy_c, text=text,
                     variable=death_sound, value=typ)
        death_radio.place(x=160,y=y)
        radiobuttons.append(death_radio)
        y += 32


    #STATS
    name_ent = Tkinter.Entry(enemy_c, textvariable = name)
    entries.append(name_ent)
    name_ent.place(x = 640, y = 32)
    name_lab = Tkinter.Label(enemy_c, text = 'Name:')
    labels.append(name_lab)
    name_lab.place(x=580, y=32)
    
    level_ent = Tkinter.Entry(enemy_c, textvariable = level)
    entries.append(level_ent)
    level_ent.place(x = 640, y = 64)
    level_lab = Tkinter.Label(enemy_c, text = 'Level:')
    labels.append(level_lab)
    level_lab.place(x=580 , y=64)

    hp_ent = Tkinter.Entry(enemy_c, textvariable = hp)
    entries.append(hp_ent)
    hp_ent.place(x = 640, y = 96)
    hp_lab = Tkinter.Label(enemy_c, text = 'HP:')
    labels.append(hp_lab)
    hp_lab.place(x=580 , y=96)

    pp_ent = Tkinter.Entry(enemy_c, textvariable = pp)
    entries.append(pp_ent)
    pp_ent.place(x = 640, y = 128)
    pp_lab = Tkinter.Label(enemy_c, text = 'PP:')
    labels.append(pp_lab)
    pp_lab.place(x=580 , y=128)

    offense_ent = Tkinter.Entry(enemy_c, textvariable = offense)
    entries.append(offense_ent)
    offense_ent.place(x = 640, y = 160)
    offense_lab = Tkinter.Label(enemy_c, text = 'Offense:')
    labels.append(offense_lab)
    offense_lab.place(x=580, y=160)

    defense_ent = Tkinter.Entry(enemy_c, textvariable = defense)
    entries.append(defense_ent)
    defense_ent.place(x = 640, y = 192)
    defense_lab = Tkinter.Label(enemy_c, text = 'Defense:')
    labels.append(defense_lab)
    defense_lab.place(x=580 , y=192)

    speed_ent = Tkinter.Entry(enemy_c, textvariable = speed)
    entries.append(speed_ent)
    speed_ent.place(x = 640, y = 224)
    speed_lab = Tkinter.Label(enemy_c, text = 'Speed:')
    labels.append(speed_lab)
    speed_lab.place(x=580 , y=224)

    guts_ent = Tkinter.Entry(enemy_c, textvariable = guts)
    entries.append(guts_ent)
    guts_ent.place(x =640, y = 256)
    guts_lab = Tkinter.Label(enemy_c, text = 'Guts:')
    labels.append(guts_lab)
    guts_lab.place(x=580 , y=256)

    luck_ent = Tkinter.Entry(enemy_c, textvariable = luck)
    entries.append(luck_ent)
    luck_ent.place(x = 640, y = 288)
    luck_lab = Tkinter.Label(enemy_c, text = 'Luck:')
    labels.append(luck_lab)
    luck_lab.place(x=580 , y=288)

    xp_ent = Tkinter.Entry(enemy_c, textvariable = xp)
    entries.append(xp_ent)
    xp_ent.place(x = 640, y = 320)
    xp_lab = Tkinter.Label(enemy_c, text = 'XP:')
    labels.append(xp_lab)
    xp_lab.place(x=580 , y=320)

    money_ent = Tkinter.Entry(enemy_c, textvariable = money)
    entries.append(money_ent)
    money_ent.place(x = 640, y = 352)
    money_lab = Tkinter.Label(enemy_c, text = 'Money:')
    labels.append(money_lab)
    money_lab.place(x=580 , y=352)

    ###DROP HANDLING

    drop_ent = Tkinter.Entry(enemy_c, textvariable = drop)
    entries.append(drop_ent)
    drop_ent.place(x = 640, y = 384)
    drop_lab = Tkinter.Label(enemy_c, text = 'Drop:')
    labels.append(drop_lab)
    drop_lab.place(x=580 , y=384)

    drop_item_name_lab = Tkinter.Label(enemy_c, textvariable = drop_item_name)
    labels.append(drop_item_name_lab)
    drop_item_name_lab.place(x=580, y = 384+(32*9))

    d_rate =[("1/128", "0"),("1/64", "1"),("1/32", "2"),("1/16", "3"),
               ("1/8", "4"),("1/4", "5"),("1/2", "6"),("Always", "7")]

    y=384+32
    for text, typ in d_rate:
        rate_radio = Tkinter.Radiobutton(enemy_c, text=text,
                     variable=drop_rate, value=typ)
        rate_radio.place(x=580,y=y)
        radiobuttons.append(rate_radio)
        y += 32

    ###Initial Status:
    stat_lab = Tkinter.Label(enemy_c, text = 'Initial Status:')
    labels.append(stat_lab)
    stat_lab.place(x=770 , y=32)
    
    possible_status = [("Normal","normal"),("Asleep", "asleep"),
                       ("Unable to concentrate", "cannot concentrate"),
                       ("feeling strange","feeling strange"),("PSI shield alpha","psi shield alpha"),
                       ("PSI shield alpha","psi shield alpha"),("Physical shield alpha","shield alpha"),
                       ("Physical shield alpha","shield beta")]
    y=64
    for text, typ in possible_status:
        status_radio = Tkinter.Radiobutton(enemy_c, text=text,
                     variable=init_stat, value=typ)
        status_radio.place(x=770,y=y)
        radiobuttons.append(status_radio)
        y += 32

    ###Ressistances: 
    fire_vul_ent = Tkinter.Entry(enemy_c, textvariable = fire_vul)
    entries.append(fire_vul_ent)
    fire_vul_ent.place(x = 900, y = 256+64)
    fire_vul_lab = Tkinter.Label(enemy_c, text = 'PK Fire Vulnerability:')
    labels.append(fire_vul_lab)
    fire_vul_lab.place(x=770 , y=256+64)

    flash_vul_ent = Tkinter.Entry(enemy_c, textvariable = flash_vul)
    entries.append(flash_vul_ent)
    flash_vul_ent.place(x = 900, y = 288+64)
    flash_vul_lab = Tkinter.Label(enemy_c, text = 'PK Flash Vulnerability:')
    labels.append(flash_vul_lab)
    flash_vul_lab.place(x=770 , y=288+64)

    freeze_vul_ent = Tkinter.Entry(enemy_c, textvariable = freeze_vul)
    entries.append(freeze_vul_ent)
    freeze_vul_ent.place(x = 900, y = 384)
    freeze_vul_lab = Tkinter.Label(enemy_c, text = 'PK Freeze Vulnerability:')
    labels.append(freeze_vul_lab)
    freeze_vul_lab.place(x=770 , y=384)

    hyp_vul_ent = Tkinter.Entry(enemy_c, textvariable = hyp_vul)
    entries.append(hyp_vul_ent)
    hyp_vul_ent.place(x = 770, y = 416+32)
    hyp_vul_lab = Tkinter.Label(enemy_c, text = 'Hypnosis/Brainshock Vulnerability:')
    labels.append(hyp_vul_lab)
    hyp_vul_lab.place(x=770 , y=416)

    par_vul_ent = Tkinter.Entry(enemy_c, textvariable = par_vul)
    entries.append(par_vul_ent)
    par_vul_ent.place(x = 900, y = 416+64)
    par_vul_lab = Tkinter.Label(enemy_c, text = 'Paralysis Vulnerability:')
    labels.append(par_vul_lab)
    par_vul_lab.place(x=770 , y=416+64)

    ###Type-gender-miss rate-unknown

    valid_types =[("Normal", "normal"),("Metal", "metal"),("Insect", "insect")]

    y=416+96
    for text, typ in valid_types:
        type_radio = Tkinter.Radiobutton(enemy_c, text=text,
                     variable=e_type, value=typ)
        type_radio.place(x=770,y=y)
        radiobuttons.append(type_radio)
        y += 32


    valid_genders =[("He", "male"),("She", "female"),("It", "neutral")]
    y = 512+96
    for text, typ in valid_genders:
        gender_radio = Tkinter.Radiobutton(enemy_c, text=text,
                     variable=gender, value=typ)
        gender_radio.place(x=770,y=y)
        radiobuttons.append(gender_radio)
        y += 32

    miss_ent = Tkinter.Entry(enemy_c, textvariable = miss_rate)
    entries.append(miss_ent)
    miss_ent.place(x = 900, y = 608+96)
    miss_lab = Tkinter.Label(enemy_c, text = 'Miss Rate (x/16):')
    labels.append(miss_lab)
    miss_lab.place(x=770 , y=608+96)

    unknown_ent = Tkinter.Entry(enemy_c, textvariable = unknown)
    entries.append(unknown_ent)
    unknown_ent.place(x = 770, y = 640+128)
    unknown_lab = Tkinter.Label(enemy_c, text = "Unknown(It's a secret to everyone):")
    labels.append(unknown_lab)
    unknown_lab.place(x=770, y=640+96)


    #Left-offs:
        
    call_ent = Tkinter.Entry(enemy_c, textvariable = max_call)
    entries.append(call_ent)
    call_ent.place(x = 1050, y = 32)
    call_lab = Tkinter.Label(enemy_c, text = 'Max Call:')
    labels.append(call_lab)
    call_lab.place(x=920 , y=32)

    mirror_ent = Tkinter.Entry(enemy_c, textvariable = mirror_rate)
    entries.append(mirror_ent)
    mirror_ent.place(x = 1050, y = 64)
    mirror_lab = Tkinter.Label(enemy_c, text = 'Successful Mirror %:')
    labels.append(mirror_lab)
    mirror_lab.place(x=920 , y=64)

    move_ent = Tkinter.Entry(enemy_c, textvariable = move_pat)
    entries.append(move_ent)
    move_ent.place(x = 1050, y = 96)
    move_lab = Tkinter.Label(enemy_c, text = 'Movement Pattern:')
    labels.append(move_lab)
    move_lab.place(x=920 , y=96)

    music_ent = Tkinter.Entry(enemy_c, textvariable = music)
    entries.append(music_ent)
    music_ent.place(x = 1050, y = 128)
    music_lab = Tkinter.Label(enemy_c, text = 'Music:')
    labels.append(music_lab)
    music_lab.place(x=920 , y=128)

    rows =[("Front Row", "1"),("Back Row", "0")]
    y = 160
    for text, typ in rows:
        row_radio = Tkinter.Radiobutton(enemy_c, text=text,
                     variable=row, value=typ)
        row_radio.place(x=920,y=y)
        radiobuttons.append(row_radio)
        y += 32

    flee_check = Tkinter.Checkbutton(enemy_c, variable = run_flag, text = "Flee-able")
    checkbuttons.append(flee_check)
    flee_check.place(x = 920, y = 192+32)

    over_spr_ent = Tkinter.Entry(enemy_c, textvariable = overworld_sprite)
    entries.append(over_spr_ent)
    over_spr_ent.place(x = 1050, y = 214+32)
    over_spr_lab = Tkinter.Label(enemy_c, text = 'Overworld Sprite:')
    labels.append(over_spr_lab)
    over_spr_lab.place(x=920 , y=214+32)

    spr_lab = Tkinter.Label(enemy_c)
    labels.append(spr_lab)
    spr_lab.place(x=1250 , y=64)

    def rep_seq():
        global enemy_sprite_final,enemy_sprite,sprite_path,real_sprite,sprites,loaded
        ask_for_new_image = tkMessageBox.showinfo(title = "New File", message = "Please choose the new Image. Make sure it's a png file and that it's an indexed one with the appropriate palette!")
        new_image_path = askopenfilename()
        if new_image_path[-4:] == ".png":
            okay_png = tkMessageBox.showinfo(title = "Okay", message = "This is in PNG format. But we can't check the size, palette or even if ti's indexed at all just yet. You've been warned!")
            real_sprite = True
            enemy_sprite = Image.open(new_image_path)
            replacer()
            selector()

        else:
            bad_png = tkMessageBox.showwarning(title = "Invalid file type", message = "Title says all, operation aborted")

    def del_seq():
        print(sprite_path)
        global enemy_sprite_final,enemy_sprite,sprite_path,real_sprite,sprites,loaded
        option_0 = tkMessageBox.askyesno(title = "Are you sure?", message = "Are you sure yuo want to delete this is Image from the projects folder, the original shall not be touched.")
        if option_0:
            print(sprite_path)
            os.remove(sprite_path)
            real_sprite = False
            enemy_sprite = ""
            replacer()
            selector()
        
    spr_but_rep = Tkinter.Button(enemy_c, text = 'Replace', command = rep_seq)
    buttons.append(spr_but_rep)

    spr_but_del = Tkinter.Button(enemy_c, text = 'Delete Image', command = del_seq)
    buttons.append(spr_but_del)
    
    def delete_entry():
        global update_selector,dele
        global loaded
        if loaded != [] and loaded != -1 and loaded != tuple():
            result = tkMessageBox.askquestion("Delete", "Are You Sure?", icon='warning', parent = enemy_c)
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
                    ymls.insert(i,(i,0,0,0,0,0,0,0,0,0,0,0,"normal" , "none.none",0,"none.none",
                                   0,0,0,"100%" , "100%" , "100%" , "neutral",0,0,"100%" , "normal",0,0,
                                   1,0,0,100,0,0,0,98,"New Enemy",0,0,0,"100%",0,7,0,"normal",0))
                    update_selector = True
                    add = True
                    to_add = i
                    selector()  
                    return
            if stop == 0:
                ymls.append((i+1,0,0,0,0,0,0,0,0,0,0,0,"normal" , "none.none",0,"none.none",
                            0,0,0,"100%" , "100%","100%","neutral",0,0,"100%","normal",0,0,
                            1,0,0,100,0,0,0,98,"New Enemy",0,0,0,"100%",0,7,0,"normal",0))
                update_selector = True
                add = True
                to_add = i + 1
                selector()
                
    delete_button = Tkinter.Button(enemy_c, command = delete_entry, text= "Delete Entry")
    buttons.append(delete_button)
    delete_button.place(x= 16, y = 32)
    add_button = Tkinter.Button(enemy_c, command = add_entry, text = "Add Entry")
    buttons.append(add_button)
    add_button.place(x= 90, y = 32)

    def replacer():
        global stuff_loaded
        global loaded
        l0 = loaded[0]
        l1 = loaded[1]
        l2 = loaded[2]
        l3 = loaded[3]
        l4 = loaded[4]
        l5 = loaded[5]
        l6 = loaded[6]
        l7 = loaded[7]
        l8 = loaded[8]
        l9 = loaded[9]
        l10 = loaded[10]
        l11 = loaded[11]
        l12 = loaded[12]
        l13 = loaded[13]
        l14 = loaded[14]
        l15 = loaded[15]
        l16 = loaded[16]
        l17 = loaded[17]
        l18 = loaded[18]
        l19 = loaded[19]
        l20 = loaded[20]
        l21 = loaded[21]
        l22 = loaded[22]
        l23 = loaded[23]
        l24 = loaded[24]
        l25 = loaded[25]
        l26 = loaded[26]
        l27 = loaded[27]
        l28 = loaded[28]
        l29 = loaded[29]
        l30 = loaded[30]
        l31 = loaded[31]
        l32 = loaded[32]
        l33 = loaded[33]
        l34 = loaded[34]
        l35 = loaded[35]
        l36 = loaded[36]
        l37 = loaded[37]
        l38 = loaded[38]
        l39 = loaded[39]
        l40 = loaded[40]
        l41 = loaded[41]
        l42 = loaded[42]
        l43 = loaded[43]
        l44 = loaded[44]
        l45 = loaded[45]
        l46 = loaded[46]
        print len(loaded)


        the_flag_int = the_flag.get()
        if the_flag_int != l1:
            l1 = int(the_flag_int)

        action_1_t = action_1.get()
        if int(action_1_t) != l2:
            l2 = int(action_1_t)

        action_1_arg_t = action_1_arg.get()
        if int(action_1_arg_t) != l3:
            l3 = int(action_1_arg_t)

        action_2_t = action_2.get()
        if int(action_2_t) != l4:
            l4 = int(action_2_t)

        action_2_arg_t = action_2_arg.get()
        if int(action_2_arg_t) != l5:
            l5 = int(action_2_arg_t)

        action_3_t = action_3.get()
        if int(action_3_t) != l6:
            l6 = int(action_3_t)

        action_3_arg_t = action_3_arg.get()
        if int(action_3_arg_t) != l7:
            l7 = int(action_3_arg_t)

        action_4_t = action_4.get()
        if int(action_4_t) != l8:
            l8 = int(action_4_t)

        action_4_arg_t = action_4_arg.get()
        if int(action_4_arg_t) != l9:
            l9 = int(action_4_arg_t)

        action_order_t = action_order.get()
        if int(action_order_t) != l10:
            l10 = int(action_order_t)

        boss_flag_int = boss_flag.get()
        if boss_flag_int != l11:
            l11 = boss_flag_int

        death_sound_t = death_sound.get()
        if death_sound_t != l12:
            l12 = death_sound_t

        death_text_t = death_text.get()
        if death_text_t != l13:
            if death_text_t.find(".") == -1:
                l13 = "$" + death_text_t
            else:
                l13 = death_text_t

        defence_t = defense.get()
        if int(defence_t) != l14:
            l14 = int(defence_t)

        encounter_t = encounter_text.get()
        if encounter_t != l15:
            if encounter_t.find(".") == -1:
                l15 = "$" + encounter_t
            else:
                l15 = encounter_t

        xp_t = xp.get()
        if int(xp_t) != l16:
            l16 = int(xp_t)

        final_action_t = final_action.get()
        if int(final_action_t) != l17:
            l17 = int(final_action_t)

        final_action_arg_t = final_action_arg.get()
        if int(final_action_arg_t) != l18:
            l18 = int(final_action_arg_t)

        fire_vul_t = fire_vul.get()
        if fire_vul_t != l19:
            l19 = fire_vul_t + "%"

        flash_vul_t = flash_vul.get()
        if flash_vul_t != l20:
            l20 = flash_vul_t + "%"

        freeze_vul_t = freeze_vul.get()
        if freeze_vul_t != l21:
            l21 = freeze_vul_t + "%"

        gender_t = gender.get()
        if gender_t != l22:
            l22 = gender_t

        guts_t = guts.get()
        if int(guts_t) != l23:
            l23 = int(guts_t)

        hp_t = hp.get()
        if int(hp_t) != l24:
            l24 = int(hp_t)

        hyp_vul_t = hyp_vul.get()
        if hyp_vul_t != l25:
            l25 = hyp_vul_t + "%"

        init_stat_t = init_stat.get()
        if init_stat_t != l26:
            l26 = init_stat_t

        drop_t = drop.get()
        l27 = int(drop_t)

        drop_r = drop_rate.get()
        if int(drop_r) != l28:
            l28 = int(drop_r)

        level_t = level.get()
        if int(level_t) != l29:
            l29 = int(level_t)
            
        luck_t = luck.get()
        if int(luck_t) != l30:
            l30 = int(luck_t)

        max_t = max_call.get()
        if int(max_t) != l31:
            l31 = int(max_t)

        mirror_r = mirror_rate.get()
        if int(mirror_r) != l32:
            l32 = int(mirror_r)

        miss_r = miss_rate.get()
        if int(miss_r) != l33:
            l33 = int(miss_r)
            
        money_t = money.get()
        if int(money_t) != l34:
            l34 = int(money_t)

        move_p = move_pat.get()
        if int(move_p) != l35:
            l35 = int(move_p)    

        music_t = music.get()
        if int(music_t) != l36:
            l36 = int(music_t)   

        name_t = name.get()
        if name_t != l37:
            l37 = name_t

        offense_t = offense.get()
        if int(offense_t) != l38:
            l38 = int(offense_t)

        o_s = overworld_sprite.get()
        if int(o_s) != l39:
            l39 = int(o_s)

        pp_t = pp.get()
        if int(pp_t) != l40:
            l40 = int(pp_t)

        par_vul_t = par_vul.get()
        if (par_vul_t) != l41:
            l41 = (par_vul_t)+ "%"

        row_t = row.get()
        if int(row_t) != l42:
            l42 = int(row_t)

        run_f = run_flag.get()
        if int(run_f) != l43:
            l43 = int(run_f) + 6

        speed_t = speed.get()
        l44 = int(speed_t)

        e_type_t = e_type.get()
        if e_type_t != l45:
            l45 = e_type_t

        unknown_t = unknown.get()
        if int(unknown_t) != l46:
            l46 = int(unknown_t)

        replaced = tuple((l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,
                          l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40,
                          l41,l42,l43,l44,l45,l46))
        
        if replaced != loaded:
            ymls[[s[0] for s in searchable][pos]] = replaced


        if real_sprite == True:
            global enemy_sprite

            sprites[(save_data + "/BattleSprites/" + digit_conversion(loaded[0]) +".png")] = enemy_sprite

        else:

            sprites[sprite_path] = "None-existent"

        if os.path.exists(save_data + "/BattleSprites") == False:
            os.makedirs(save_data + "/BattleSprites")
        if os.path.exists(save_data + "/BattleSprites/" + "empty") == False:
            to_ignore = open(save_data + "/BattleSprites/" + "empty", "wb")
            to_ignore.close()
        to_ignore = open(save_data + "/BattleSprites/" + "empty", "rb")
        old_lines = [line for line in to_ignore if (line != "" or line != "\n")]
        print old_lines
        to_ignore.close()

        to_ignore = open(save_data + "/BattleSprites/" + "empty", "wb")
        
        print sprites
        lines = []
        for s in sprites:
            print type(type(sprites[s]))
            if type(sprites[s]) != str:
                png_info = sprites[s].info
                sprites[s].save(s,**png_info)
            else:
                lines.append(s)

        for l in lines:
            if l == "" or l == "\n":
                lines.remove(l)
            elif l not in old_lines:
                to_ignore.write(l + "\n")
            print l
        to_ignore.close()
            
        return    

    def saver():
        global stuff_loaded
        global loaded
        if stuff_loaded:
            replacer()
            location = os.getcwd()
            to_dump = open(save_data + "/enemy_configuration_table.yml",'w')
            changed_ymls = {}
            for y in ymls:
                changed_ymls[y[0]] = {'"The" Flag': y[1],
                                      "Action 1" : y[2],
                                      "Action 1 Argument" : y[3],
                                      "Action 2" : y[4],
                                      "Action 2 Argument" : y[5],
                                      "Action 3" : y[6],
                                      "Action 3 Argument" : y[7],
                                      "Action 4" : y[8],
                                      "Action 4 Argument" : y[9],
                                      "Action Order" : y[10],
                                      "Boss Flag" : y[11],
                                      "Death Sound" : y[12],
                                      "Death Text Pointer" : y[13],
                                      "Defense" : y[14],
                                      "Encounter Text Pointer" : y[15],
                                      "Experience points" : y[16],
                                      "Final Action" : y[17],
                                      "Final Action Argument" : y[18],
                                      "Fire vulnerability" : y[19],
                                      "Flash vulnerability" : y[20],
                                      "Freeze vulnerability" : y[21],
                                      "Gender" : y[22],
                                      "Guts" : y[23],
                                      "HP" : y[24],
                                      "Hypnosis/Brainshock vulnerability" : y[25],
                                      "Initial Status" : y[26],
                                      "Item Dropped" : y[27],
                                      "Item Rarity" : y[28],
                                      "Level" : y[29],
                                      "Luck" : y[30],
                                      "Max Call" : y[31],
                                      "Mirror Success Rate" : y[32],
                                      "Miss Rate" : y[33],
                                      "Money" : y[34],
                                      "Movement pattern" : y[35],
                                      "Music" : y[36],
                                      "Name" : y[37],
                                      "Offense" : y[38],
                                      "Overworld Sprite" : y[39],
                                      "PP" : y[40],
                                      "Paralysis vulnerability" : y[41],
                                      "Row" : y[42],
                                      "Run Flag" : y[43],
                                      "Speed": y[44],
                                      "Type" : y[45],
                                      "Unknown" : y[46]}
            yaml.dump(changed_ymls, to_dump, default_flow_style=False)
            
        if os.path.exists(save_data + "/BattleSprites") == False:
            os.makedirs(save_data + "/BattleSprites")
        if os.path.exists(save_data + "/BattleSprites/" + "empty") == False:
            to_ignore = open(save_data + "/BattleSprites/" + "empty", "wb")
            to_ignore.close()
        to_ignore = open(save_data + "/BattleSprites/" + "empty", "rb")
        old_lines = [line for line in to_ignore if (line != "" or line != "\n")]
        print old_lines
        to_ignore.close()

        to_ignore = open(save_data + "/BattleSprites/" + "empty", "wb")
        
        print sprites
        lines = []
        for s in sprites:
            print type(type(sprites[s]))
            if type(sprites[s]) != str:
                png_info = sprites[s].info
                sprites[s].save(s,**png_info)
            else:
                lines.append(s)

        for l in lines:
            if l == "" or l == "\n":
                lines.remove(l)
            elif l not in old_lines:
                to_ignore.write(l + "\n")
            print l
        to_ignore.close()
        
        enemy_c.destroy()

        w_2.remove(w_2[[w[1] for w in w_2].index("Enemy Config")])
        stram.close()

    enemy_c.protocol("WM_DELETE_WINDOW", saver)

#####THE ULTIMATE
def call_enemy_config(w_2):
    
    (w_2[[w[1] for w in w_2].index("Enemy Config")])[0].lift()


