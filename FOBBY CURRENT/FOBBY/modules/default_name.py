import Tkinter, re, sys, yaml, tkMessageBox, os, unicodedata
sys.path.append(os.getcwd()[:-7])
import FOBBY
 
def name_s(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,path,save_data):
    global stuff_loaded
    global update_selector
    update_selector = False
    stuff_loaded = False
    global searchable
    searchable = []
    ymls = []
    
    selector_index = []
    loaded = tuple()
    
    ness_1 = Tkinter.StringVar()
    ness_2 = Tkinter.StringVar()
    ness_3 = Tkinter.StringVar()
    ness_4 = Tkinter.StringVar()
    ness_5 = Tkinter.StringVar()
    ness_6 = Tkinter.StringVar()
    ness_7 = Tkinter.StringVar()
    ness_skip = Tkinter.StringVar()

    paula_1 = Tkinter.StringVar()
    paula_2 = Tkinter.StringVar()
    paula_3 = Tkinter.StringVar()
    paula_4 = Tkinter.StringVar()
    paula_5 = Tkinter.StringVar()
    paula_6 = Tkinter.StringVar()
    paula_7 = Tkinter.StringVar()
    paula_skip = Tkinter.StringVar()

    jeff_1 = Tkinter.StringVar()
    jeff_2 = Tkinter.StringVar()
    jeff_3 = Tkinter.StringVar()
    jeff_4 = Tkinter.StringVar()
    jeff_5 = Tkinter.StringVar()
    jeff_6 = Tkinter.StringVar()
    jeff_7 = Tkinter.StringVar()
    jeff_skip = Tkinter.StringVar()

    poo_1 = Tkinter.StringVar()
    poo_2 = Tkinter.StringVar()
    poo_3 = Tkinter.StringVar()
    poo_4 = Tkinter.StringVar()
    poo_5 = Tkinter.StringVar()
    poo_6 = Tkinter.StringVar()
    poo_7 = Tkinter.StringVar()
    poo_skip = Tkinter.StringVar()

    king_1 = Tkinter.StringVar()
    king_2 = Tkinter.StringVar()
    king_3 = Tkinter.StringVar()
    king_4 = Tkinter.StringVar()
    king_5 = Tkinter.StringVar()
    king_6 = Tkinter.StringVar()
    king_7 = Tkinter.StringVar()
    king_skip = Tkinter.StringVar()

    steak_1 = Tkinter.StringVar()
    steak_2 = Tkinter.StringVar()
    steak_3 = Tkinter.StringVar()
    steak_4 = Tkinter.StringVar()
    steak_5 = Tkinter.StringVar()
    steak_6 = Tkinter.StringVar()
    steak_7 = Tkinter.StringVar()
    steak_skip = Tkinter.StringVar()

    rockin_1 = Tkinter.StringVar()
    rockin_2 = Tkinter.StringVar()
    rockin_3 = Tkinter.StringVar()
    rockin_4 = Tkinter.StringVar()
    rockin_5 = Tkinter.StringVar()
    rockin_6 = Tkinter.StringVar()
    rockin_7 = Tkinter.StringVar()
    rockin_skip = Tkinter.StringVar()

    enable_skip = Tkinter.BooleanVar()
    enable_summary = Tkinter.BooleanVar()
    
    x_path = path[:-13]
    name_w = Tkinter.Toplevel()
    name_w.geometry('1200x400+300+300')
    
    windows.append(name_w)
    w_2.append((name_w,"name_skip"))
    
    if os.path.exists(save_data+ "/dont_care_names.yml"):
        stram = open(save_data + "/dont_care_names.yml", "r")
    else:
        r_path = x_path + "dont_care_names.yml"
        stram = open(r_path, "r")

    if os.path.exists(save_data+ "/naming_skip.yml"):
        strem = open(save_data + "/naming_skip.yml", "r")
    else:
        r_path = x_path + "naming_skip.yml"
        strem = open(r_path, "r")

    yml_1 = yaml.load(stram)
    str_yml_1 = str(yml_1)
    yml_2 = yaml.load(strem)
    str_yml_2 = str(yml_2)

    table_name_1 = Tkinter.Label(name_w, text = 'Ness:')
    labels.append(table_name_1)
    table_name_1.place(x=96,y=32)

    table_name_2 = Tkinter.Label(name_w, text = 'Paula:')
    labels.append(table_name_2)
    table_name_2.place(x=256,y=32)

    table_name_3 = Tkinter.Label(name_w, text = 'Jeff:')
    labels.append(table_name_3)
    table_name_3.place(x=416,y=32)

    table_name_4 = Tkinter.Label(name_w, text = 'Poo:')
    labels.append(table_name_4)
    table_name_4.place(x=576,y=32)

    table_name_5 = Tkinter.Label(name_w, text = 'Pet:')
    labels.append(table_name_5)
    table_name_5.place(x=736,y=32)

    table_name_3 = Tkinter.Label(name_w, text = 'Food:')
    labels.append(table_name_3)
    table_name_3.place(x=896,y=32)

    table_name_3 = Tkinter.Label(name_w, text = 'Thing:')
    labels.append(table_name_3)
    table_name_3.place(x=1056,y=32)

    table_number_1 = Tkinter.Label(name_w, text = 'Option #1:')
    labels.append(table_number_1)
    table_number_1.place(x=32,y=64)

    table_number_2 = Tkinter.Label(name_w, text = 'Option #2:')
    labels.append(table_number_2)
    table_number_2.place(x=32,y=96)

    table_number_3 = Tkinter.Label(name_w, text = 'Option #3:')
    labels.append(table_number_3)
    table_number_3.place(x=32,y=128)

    table_number_4 = Tkinter.Label(name_w, text = 'Option #4:')
    labels.append(table_number_4)
    table_number_4.place(x=32,y=160)

    table_number_5 = Tkinter.Label(name_w, text = 'Option #5:')
    labels.append(table_number_5)
    table_number_5.place(x=32,y=192)

    table_number_6 = Tkinter.Label(name_w, text = 'Option #6:')
    labels.append(table_number_6)
    table_number_6.place(x=32,y=224)

    table_number_7 = Tkinter.Label(name_w, text = 'Option #7:')
    labels.append(table_number_7)
    table_number_7.place(x=32,y=256)

    table_skip = Tkinter.Label(name_w, text = 'Skip:')
    labels.append(table_skip)
    table_skip.place(x=32,y=288)

    table_ness_1 = Tkinter.Entry(name_w)
    table_ness_2 = Tkinter.Entry(name_w)
    table_ness_3 = Tkinter.Entry(name_w)
    table_ness_4 = Tkinter.Entry(name_w)
    table_ness_5 = Tkinter.Entry(name_w)
    table_ness_6 = Tkinter.Entry(name_w)
    table_ness_7 = Tkinter.Entry(name_w)
    table_ness_skip = Tkinter.Entry(name_w)

    table_paula_1 = Tkinter.Entry(name_w)
    table_paula_2 = Tkinter.Entry(name_w)
    table_paula_3 = Tkinter.Entry(name_w)
    table_paula_4 = Tkinter.Entry(name_w)
    table_paula_5 = Tkinter.Entry(name_w)
    table_paula_6 = Tkinter.Entry(name_w)
    table_paula_7 = Tkinter.Entry(name_w)
    table_paula_skip = Tkinter.Entry(name_w)

    table_jeff_1 = Tkinter.Entry(name_w)
    table_jeff_2 = Tkinter.Entry(name_w)
    table_jeff_3 = Tkinter.Entry(name_w)
    table_jeff_4 = Tkinter.Entry(name_w)
    table_jeff_5 = Tkinter.Entry(name_w)
    table_jeff_6 = Tkinter.Entry(name_w)
    table_jeff_7 = Tkinter.Entry(name_w)
    table_jeff_skip = Tkinter.Entry(name_w)

    table_poo_1 = Tkinter.Entry(name_w)
    table_poo_2 = Tkinter.Entry(name_w)
    table_poo_3 = Tkinter.Entry(name_w)
    table_poo_4 = Tkinter.Entry(name_w)
    table_poo_5 = Tkinter.Entry(name_w)
    table_poo_6 = Tkinter.Entry(name_w)
    table_poo_7 = Tkinter.Entry(name_w)
    table_poo_skip = Tkinter.Entry(name_w)

    table_king_1 = Tkinter.Entry(name_w)
    table_king_2 = Tkinter.Entry(name_w)
    table_king_3 = Tkinter.Entry(name_w)
    table_king_4 = Tkinter.Entry(name_w)
    table_king_5 = Tkinter.Entry(name_w)
    table_king_6 = Tkinter.Entry(name_w)
    table_king_7 = Tkinter.Entry(name_w)
    table_king_skip = Tkinter.Entry(name_w)

    table_steak_1 = Tkinter.Entry(name_w)
    table_steak_2 = Tkinter.Entry(name_w)
    table_steak_3 = Tkinter.Entry(name_w)
    table_steak_4 = Tkinter.Entry(name_w)
    table_steak_5 = Tkinter.Entry(name_w)
    table_steak_6 = Tkinter.Entry(name_w)
    table_steak_7 = Tkinter.Entry(name_w)
    table_steak_skip = Tkinter.Entry(name_w)

    table_rockin_1 = Tkinter.Entry(name_w)
    table_rockin_2 = Tkinter.Entry(name_w)
    table_rockin_3 = Tkinter.Entry(name_w)
    table_rockin_4 = Tkinter.Entry(name_w)
    table_rockin_5 = Tkinter.Entry(name_w)
    table_rockin_6 = Tkinter.Entry(name_w)
    table_rockin_7 = Tkinter.Entry(name_w)
    table_rockin_skip = Tkinter.Entry(name_w)

    table_of_names = {(1,1):(table_ness_1,ness_1,96,64),(1,2):(table_ness_2,ness_2,96,96),(1,3):(table_ness_3,ness_3,96,128),
                      (1,4):(table_ness_4,ness_4,96,160),(1,5):(table_ness_5,ness_5,96,192),(1,6):(table_ness_6,ness_6,96,224),
                      (1,7):(table_ness_7,ness_7,96,256), (1,8):(table_ness_skip,ness_skip,96,288),(2,1):(table_paula_1,paula_1,256,64),
                      (2,2):(table_paula_2,paula_2,256,96),(2,3):(table_paula_3,paula_3,256,128),(2,4):(table_paula_4,paula_4,256,160),
                      (2,4):(table_paula_4,paula_4,256,160),(2,5):(table_paula_5,paula_5,256,192),(2,6):(table_paula_6,paula_6,256,224),
                      (2,7):(table_paula_7,paula_7,256,256),(2,8):(table_paula_skip,paula_skip,256,288),(3,1):(table_jeff_1,jeff_1,416,64),
                      (3,2):(table_jeff_2,jeff_2,416,96),(3,3):(table_jeff_3,jeff_3,416,128),(3,4):(table_jeff_4,jeff_4,416,160),
                      (3,5):(table_jeff_5,jeff_5,416,192),(3,6):(table_jeff_6,jeff_6,416,224),(3,7):(table_jeff_7,jeff_7,416,256),
                      (3,8):(table_jeff_skip,jeff_skip,416,288),(4,1):(table_poo_1,poo_1,576,64),(4,2):(table_poo_2,poo_2,576,96),
                      (4,3):(table_poo_3,poo_3,576,128),(4,4):(table_poo_4,poo_4,576,160),(4,5):(table_poo_5,poo_5,576,192),
                      (4,6):(table_poo_6,poo_6,576,224),(4,7):(table_poo_7,poo_7,576,256),(4,8):(table_poo_skip,poo_skip,576,288),
                      (5,1):(table_king_1,king_1,736,64),(5,2):(table_king_2,king_2,736,96),(5,3):(table_king_3,king_3,736,128),
                      (5,4):(table_king_4,king_4,736,160),(5,5):(table_king_5,king_5,736,192),(5,6):(table_king_6,king_6,736,224),
                      (5,7):(table_king_7,king_7,736,256),(5,8):(table_king_skip,king_skip,736,288),(6,1):(table_steak_1,steak_1,896,64),
                      (6,2):(table_steak_2,steak_2,896,96),(6,3):(table_steak_3,steak_3,896,128),(6,4):(table_steak_4,steak_4,896,160),
                      (6,5):(table_steak_5,steak_5,896,192),(6,6):(table_steak_6,steak_6,896,224),(6,7):(table_steak_7,steak_7,896,256),
                      (6,8):(table_steak_skip,steak_skip,896,288),(7,1):(table_rockin_1,rockin_1,1056,64),(7,2):(table_rockin_2,rockin_2,1056,96),
                      (7,3):(table_rockin_3,rockin_3,1056,128),(7,4):(table_rockin_4,rockin_4,1056,160),(7,5):(table_rockin_5,rockin_5,1056,192),
                      (7,6):(table_rockin_6,rockin_6,1056,224),(7,7):(table_rockin_7,rockin_7,1056,256),(7,8):(table_rockin_skip,rockin_skip,1056,288)}
    for x_cord in range(1,8):
        for y_cord in range(1,9):
            current_table = table_of_names[(x_cord,y_cord)]
            current_table[0].config(textvariable = current_table[1])
            entries.append(current_table[0])
            current_table[0].place(x= current_table[2], y = current_table[3])

    ness_1.set(yml_1[0]['Name 1'])
    ness_2.set(yml_1[0]['Name 2'])
    ness_3.set(yml_1[0]['Name 3'])
    ness_4.set(yml_1[0]['Name 4'])
    ness_5.set(yml_1[0]['Name 5'])
    ness_6.set(yml_1[0]['Name 6'])
    ness_7.set(yml_1[0]['Name 7'])
    ness_skip.set(yml_2['Name1'])

    paula_1.set(yml_1[1]['Name 1'])
    paula_2.set(yml_1[1]['Name 2'])
    paula_3.set(yml_1[1]['Name 3'])
    paula_4.set(yml_1[1]['Name 4'])
    paula_5.set(yml_1[1]['Name 5'])
    paula_6.set(yml_1[1]['Name 6'])
    paula_7.set(yml_1[1]['Name 7'])
    paula_skip.set(yml_2['Name2'])

    jeff_1.set(yml_1[2]['Name 1'])
    jeff_2.set(yml_1[2]['Name 2'])
    jeff_3.set(yml_1[2]['Name 3'])
    jeff_4.set(yml_1[2]['Name 4'])
    jeff_5.set(yml_1[2]['Name 5'])
    jeff_6.set(yml_1[2]['Name 6'])
    jeff_7.set(yml_1[2]['Name 7'])
    jeff_skip.set(yml_2['Name3'])

    poo_1.set(yml_1[3]['Name 1'])
    poo_2.set(yml_1[3]['Name 2'])
    poo_3.set(yml_1[3]['Name 3'])
    poo_4.set(yml_1[3]['Name 4'])
    poo_5.set(yml_1[3]['Name 5'])
    poo_6.set(yml_1[3]['Name 6'])
    poo_7.set(yml_1[3]['Name 7'])
    poo_skip.set(yml_2['Name4'])

    king_1.set(yml_1[4]['Name 1'])
    king_2.set(yml_1[4]['Name 2'])
    king_3.set(yml_1[4]['Name 3'])
    king_4.set(yml_1[4]['Name 4'])
    king_5.set(yml_1[4]['Name 5'])
    king_6.set(yml_1[4]['Name 6'])
    king_7.set(yml_1[4]['Name 7'])
    king_skip.set(yml_2['Pet'])

    steak_1.set(yml_1[5]['Name 1'])
    steak_2.set(yml_1[5]['Name 2'])
    steak_3.set(yml_1[5]['Name 3'])
    steak_4.set(yml_1[5]['Name 4'])
    steak_5.set(yml_1[5]['Name 5'])
    steak_6.set(yml_1[5]['Name 6'])
    steak_7.set(yml_1[5]['Name 7'])
    steak_skip.set(yml_2['Food'])

    rockin_1.set(yml_1[6]['Name 1'])
    rockin_2.set(yml_1[6]['Name 2'])
    rockin_3.set(yml_1[6]['Name 3'])
    rockin_4.set(yml_1[6]['Name 4'])
    rockin_5.set(yml_1[6]['Name 5'])
    rockin_6.set(yml_1[6]['Name 6'])
    rockin_7.set(yml_1[6]['Name 7'])
    rockin_skip.set(yml_2['Thing'])

    enable_skip.set(yml_2['Enable Skip'])
    enable_summary.set(yml_2['Enable Summary'])

    print enable_skip
    print enable_summary
                                   


    skip_but = Tkinter.Checkbutton(name_w,variable= enable_skip,text = "Enable Skip:")
    checkbuttons.append(skip_but)
    skip_but.place(x = 94, y = 320)
 
    summary_but = Tkinter.Checkbutton(name_w,variable= enable_summary, text = "Enable Summary:")
    checkbuttons.append(summary_but)
    summary_but.place(x = 416, y = 320)


    print enable_skip
    print enable_summary

    def saver():
        location = os.getcwd()
        to_dump_1 = open(save_data + "/dont_care_names.yml",'w')
        to_dump_2 = open(save_data + "/naming_skip.yml",'w')
        
        changed_ymls_1 = {
            0: {
                "Name 1" : ness_1.get(), "Name 2" : ness_2.get(), "Name 3" : ness_3.get(),
                "Name 4" : ness_4.get(), "Name 5" : ness_5.get(), "Name 6" : ness_6.get(),
                "Name 7" : ness_7.get()},
            1: {
                "Name 1" : paula_1.get(), "Name 2" : paula_2.get(), "Name 3" : paula_3.get(),
                "Name 4" : paula_4.get(), "Name 5" : paula_5.get(), "Name 6" : paula_5.get(),
                "Name 7" : paula_7.get()},
            2: {
                "Name 1" : jeff_1.get(), "Name 2" : jeff_2.get(), "Name 3" : jeff_3.get(),
                "Name 4" : jeff_4.get(), "Name 5" : jeff_5.get(), "Name 6" : jeff_5.get(),
                "Name 7" : jeff_7.get()},
            3: {
                "Name 1" : poo_1.get(), "Name 2" : poo_2.get(), "Name 3" : poo_3.get(),
                "Name 4" : poo_4.get(), "Name 5" : poo_5.get(), "Name 6" : poo_5.get(),
                "Name 7" : poo_7.get()},
            4: {
                "Name 1" : king_1.get(), "Name 2" : king_2.get(), "Name 3" : king_3.get(),
                "Name 4" : king_4.get(), "Name 5" : king_5.get(), "Name 6" : king_5.get(),
                "Name 7" : king_7.get()},
            5: {
                "Name 1" : steak_1.get(), "Name 2" : steak_2.get(), "Name 3" : steak_3.get(),
                "Name 4" : steak_4.get(), "Name 5" : steak_5.get(), "Name 6" : steak_5.get(),
                "Name 7" : steak_7.get()},
            6: {
                "Name 1" : rockin_1.get(), "Name 2" : rockin_2.get(), "Name 3" : rockin_3.get(),
                "Name 4" : rockin_4.get(), "Name 5" : rockin_5.get(), "Name 6" : rockin_5.get(),
                "Name 7" : rockin_7.get()}
            }
                                
        changed_ymls_2 = {
            "Enable Summary": enable_summary.get(), "Enable Skip": enable_skip.get(),
            "Food": steak_skip.get(), "Name1": ness_skip.get(),"Name2": paula_skip.get(),
            "Name3": jeff_skip.get(),"Name4": poo_skip.get(),"Thing": rockin_skip.get(),
            "Food": steak_skip.get(),"Pet": king_skip.get()}
        
        yaml.dump(changed_ymls_1, to_dump_1, default_flow_style=False)
        yaml.dump(changed_ymls_2, to_dump_2, default_flow_style=False)
        name_w.destroy()

        w_2.remove(w_2[[w[1] for w in w_2].index("name_skip")])
        stram.close()
        strem.close()

    name_w.protocol("WM_DELETE_WINDOW", saver)

def call_name(w_2):
    
    (w_2[[w[1] for w in w_2].index("name_skip")])[0].lift()


