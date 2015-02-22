import Tkinter, re, sys, yaml, tkMessageBox, os, unicodedata
sys.path.append(os.getcwd()[:-7])
import FOBBY
 
def adress_index(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,path,save_data):
    x_path = path[:-13]
    index = Tkinter.Toplevel()
    index.geometry('500x500+300+300')
    windows.append(index)
    w_2.append((index,"adress_index"))

    to_search = Tkinter.StringVar()
    search_for_type = Tkinter.StringVar()
    adresses = open(os.getcwd() + "/modules/adresses.txt", mode = 'r')


    code_adresses = []
    text_adresses = []
    descs = []

    state = 0
    for a in adresses:
        state = 0
        while state != 3:
            state += 1
            if state == 1:
                code_adress = re.findall(r'\$c[0-9a-f]+',a)
                code_adresses.append(([code_adress[0][1:],(len(code_adresses))]))
                a = a[len(code_adress[0]):]
            elif state == 2:
                text_adress = re.findall(r'\$[0-9a-f]+',a)
                text_adresses.append(([text_adress[0][1:],(len(text_adresses))]))
            elif state == 3:
                desc = re.findall(r'- .+',a)
                desc = desc[0][2:]
                descs.append(([desc,(len(descs))]))

    searcher = Tkinter.Listbox(index, width = 75)
    listboxes.append(searcher)
    searcher.place(x = 16, y = 16)
    searchable = []

    label_code = Tkinter.Label(index, text = "Code Adress:")
    label_code.place(x=16, y= 282)
    labels.append(label_code)
    label_text = Tkinter.Label(index, text = "Text Adress:")
    label_text.place(x=16, y= 314)
    labels.append(label_text)
    label_desc = Tkinter.Label(index, text = "Description:")
    label_desc.place(x=16, y= 346)
    labels.append(label_desc)

    index_scroller = Tkinter.Scale(index, from_=0, to=1)
    index_scroller.place(x=446 , y=74 )
    scalers.append(index_scroller)
           
    def labeler():
        global searchable
        try:
            code = ""
            text = ""
            description = ""
            
            selection_val = searchable[int(searcher.curselection()[0])][1]
            print selection_val
            
            for c in code_adresses:
                if c[1] == int(selection_val):
                    code = c[0]

            for t in text_adresses:
                if t[1] == int(selection_val):
                    text = t[0]

            for d in descs:
                if d[1] == int(selection_val):
                    description = d[0]

                    
            label_code.config(text = "Code Adress: " + code)
            label_text.config(text = "Text Adress: " + text)
            label_desc.config(text = "Description: " + description)

        except IndexError:
            return


    def searcher_update():
        global searchable
        searchable = []
        searcher.delete(0,"end")
        recieve_search_type = search_for_type.get()
        recieve_search = to_search.get()
        if recieve_search != "":
            if recieve_search_type == "desc":
                i = -1
                for d in descs:
                    i += 1
                    if d[0].find(recieve_search) > -1:
                        searchable.append([d[0],i])
            elif recieve_search_type == "code":
                i = -1
                for c in code_adresses:
                    i += 1
                    if c[0].find(recieve_search) > -1:
                        searchable.append([c[0],i])
            elif recieve_search_type == "text":
                i = -1
                for t in text_adresses:
                    i += 1
                    if t[0].find(recieve_search) > -1:
                        searchable.append([t[0],i])
        else:
            if recieve_search_type == "desc":
                i = -1
                for d in descs:
                    i += 1
                    searchable.append([d[0],i])
            elif recieve_search_type == "code":
                i = -1
                for c in code_adresses:
                    i += 1
                    searchable.append([c[0],i])
            elif recieve_search_type == "text":
                i = -1
                for t in text_adresses:
                    i += 1
                    searchable.append([t[0],i])

        for s in searchable:
            searcher.insert(s[1],s[0])
        labeler()

        index_scroller.config(command=searcher.yview, to = len(searchable)-1)
        

    def searcher_update_trigger(event):
        searcher_update()

    def relabler(event):
        labeler()
        print "Event recieved"

    search_by_desc = Tkinter.Radiobutton(index, var = search_for_type, text ="Search by description", value = "desc", command = searcher_update)
    search_by_desc.place(x = 150, y = 180)
    radiobuttons.append(search_by_desc)
    search_by_code = Tkinter.Radiobutton(index, var = search_for_type, text ="Search by code adress", value = "code", command = searcher_update)
    search_by_code.place(x = 150, y = 212)
    radiobuttons.append(search_by_code)
    search_by_text = Tkinter.Radiobutton(index, var = search_for_type, text ="Search by text adress", value = "text", command = searcher_update)
    search_by_text.place(x = 150, y = 244)
    radiobuttons.append(search_by_text)
    search_by_desc.select()

    search_box = Tkinter.Entry(index, textvariable = to_search)
    search_box.place(x= 16, y = 180)
    entries.append(search_box)
    search_box.bind("<KeyRelease>",searcher_update_trigger)
    searcher.bind("<<ListboxSelect>>", relabler)
    searcher_update()
    labeler()

    def close_confirm():
        print w_2
        w_2.remove(w_2[[w[1] for w in w_2].index("adress_index")])
        index.destroy()

    index.protocol("WM_DELETE_WINDOW", close_confirm)

def call_adress_index(w_2):
    (w_2[[w[1] for w in w_2].index("adress_index")])[0].lift()
        

    

