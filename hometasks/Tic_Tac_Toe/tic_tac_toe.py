from tkinter import *
from tkinter import ttk

conut = 0
root = Tk()
root.title("Крестики-нолики")
root.geometry("350x300")
root.resizable(height=None, width=None)
for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)
for r in range(3):
    for c in range(3):
        conut += 1
        btn = ttk.Button(text=f"{conut}")
        btn.grid(row=r, column=c)
        btn.grid(row=r, column=c, ipadx=20, ipady=20, padx=2, pady=2, sticky=E)

root.mainloop()