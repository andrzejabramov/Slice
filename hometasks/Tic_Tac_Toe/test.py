from tkinter import *

frm = []; btn = []; who = True

def play(n):
    global who
    btn[n].config(text='X' if who else 'O')
    who = not(who)

for i in range(3):
    frm.append(Frame(background='black'))
    frm[i].pack(expand=YES, fill=BOTH)
    for j in range(3):
        btn.append(Button(frm[i], text=' ', bg='yellow',  fg='blue', font=('mono', 20, 'bold'), width=3, height=3))
        btn[i*3+j].config(command=lambda n=i*3+j: play(n))
        btn[i*3+j].pack(expand=True, fill=BOTH, side=LEFT, padx=3, pady=3, ipadx=1, ipady=1, anchor=NE)


mainloop()
