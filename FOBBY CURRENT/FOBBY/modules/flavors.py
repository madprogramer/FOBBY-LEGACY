import Tkinter
def f(widgets,bgc,f,ab,af):

    for w in widgets:
        try:
            if widgets[w].winfo_exists() == True:
                w.config(bg = bgc)
        except AttributeError:
            print "not an object"
            pass

        for tab in widgets[w]:
            if current = True:
                for l in widgets[w][tab][labels]:
                    if l.winfo_exists():
                        l.config(bg = bgc, fg = f, highlightbackground= f)
                for b in widgets[w][tab][buttons]:
                    if b.winfo_exists():
                        b.config(activebackground = ab, activeforeground = af, bg = bgc, fg = f, highlightbackground= f)
                for i in widgets[w][tab][messageboxes]:
                    if i.winfo_exists():
                        i.config(bg = bgc, fg = f, highlightbackground= f)
                for e in widgets[w][tab][entries]:
                    if e.winfo_exists():
                        e.config(bg = bgc, fg = f, highlightbackground= f)
                for s in widgets[w][tab][scalers]:
                    if s.winfo_exists():
                        s.config(activebackground = ab, bg = bgc, fg = f, showvalue= 0, highlightbackground= f, troughcolor= bgc)
                for r in widgets[w][tab][radiobuttons]:
                    if r.winfo_exists():
                        r.config(bg = bgc, activebackground = bgc, activeforeground = af,fg = f, highlightbackground= f, disabledforeground = f, selectcolor= bgc)
                for c in widgets[w][tab][checkbuttons]:
                    if c.winfo_exists():
                        c.config(bg = bgc, activebackground = bgc, activeforeground = af,fg = f, highlightbackground= f, disabledforeground = f ,selectcolor=bgc)        
                for fr in widgets[w][tab][frames]:
                    if fr.winfo_exists():
                        fr.config(bg = bgc, activebackground = bgc, activeforeground = af,fg = f, highlightbackground= f, disabledforeground = f )
