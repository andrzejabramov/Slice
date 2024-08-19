import tkinter as tk
from tkinter import ttk, colorchooser


count = 0
root = tk.Tk()
root.geometry('350x350')
root.resizable
style = ttk.Style()
frame = ttk.Frame()
frame.pack(expand=True)
style.configure('TFrame', background='green')
style.configure('BW.TLabel', foreground='pink', background='black')
frame_m = ttk.Frame()
frame_m.pack(expand=True)
label = ttk.Label(frame_m, text='Hello, Tkinter', style='BW.TLabel')
label.pack(expand=True)
# #colorchooser.askcolor()

def click():
    global count
    count += 1
    letter = 'X' if count == 1 or count % 2 != 0 else 'O'
    btn['text'] = letter
    btn.configure(state='disable')
    return letter

for i in range(3):
     frame.rowconfigure(index=i, weight=1)
     for j in range(3):
         frame.columnconfigure(index=j, weight=1)
         btn = tk.Button(frame, text='  ', fg='black', font='Arial 44', background='black', highlightbackground='black')
         btn.configure(command=click)
         btn.grid(row=i, column=j, ipadx=30, ipady=30, padx=0.1, pady=0.1)

root.mainloop()