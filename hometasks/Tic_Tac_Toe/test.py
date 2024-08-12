from tkinter import *

frm = []; btn = []; who = True

def play(n):
    global who
    btn[n].config(text='X' if who else 'O')
    who = not(who)

for i in range(3):
    frm.append(Frame())
    frm[i].pack(expand=YES, fill=BOTH)
    for j in range(3):
        btn.append(Button(frm[i], text=' ', font=('mono', 20, 'bold'), width=3, height=2))
        btn[i*3+j].config(command=lambda n=i*3+j: play(n))
        btn[i*3+j].pack(expand=YES, fill=BOTH, side=LEFT, padx=1, pady=1)


mainloop()
