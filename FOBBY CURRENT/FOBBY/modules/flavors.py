import Tkinter
def f(windows,labels,buttons,listboxes,entries,scalers,radiobuttons,checkbuttons,frames,w_2,bgc,f,ab,af):
    for w in windows:
        try:
            if w.winfo_exists() == True:
                w.config(bg = bgc)
        except AttributeError:
            print "not an object"
    for l in labels:
        if l.winfo_exists() == True:
            l.config(bg = bgc, fg = f, highlightbackground= f)
    for b in buttons:
        if b.winfo_exists() == True:
            b.config(activebackground = ab, activeforeground = af, bg = bgc, fg = f, highlightbackground= f)
    for i in listboxes:
        if i.winfo_exists() == True:
            i.config(bg = bgc, fg = f, highlightbackground= f)
    for e in entries:
        if e.winfo_exists() == True:
            e.config(bg = bgc, fg = f, highlightbackground= f)
    for s in scalers:
        if s.winfo_exists() == True:
            s.config(activebackground = ab, bg = bgc, fg = f, showvalue= 0, highlightbackground= f, troughcolor= bgc)
    for r in radiobuttons:
        if r.winfo_exists() == True:
            r.config(bg = bgc, activebackground = bgc, activeforeground = af,fg = f, highlightbackground= f, disabledforeground = f, selectcolor= bgc)
    for c in checkbuttons:
        if c.winfo_exists() == True:
            c.config(bg = bgc, activebackground = bgc, activeforeground = af,fg = f, highlightbackground= f, disabledforeground = f ,selectcolor=bgc)        
    for fr in frames:
        if fr.winfo_exists() == True:
            fr.config(bg = bgc, activebackground = bgc, activeforeground = af,fg = f, highlightbackground= f, disabledforeground = f )
