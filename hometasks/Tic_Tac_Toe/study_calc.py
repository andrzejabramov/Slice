import tkinter as tk
from tkinter import ttk


class Calc:
    root = tk.Tk()
    def __init__(self, x, y, color, naming):
        self.x = x
        self.y = y
        self.color = color
        self.naming = naming

    def window(self):
        self.root.title(self.naming)
        self.root['bg'] = self.color
        self.root.geometry(str(self.x)+'x'+str(self.y))
        return self.root

    def __entry(self, width_ent):
        ent = ttk.Entry()
        ent.width = width_ent
        ent.bg = 'yellow'
        ent.fg = 'red'
        return ent.pack()

    def __frame(self):
        fr = self.root.Frame(self.window, padx=10, pady=10)
        return fr.pack(expend=True, full=Y, bg='pink')

    def start(self):
        self.__frame()
        self.__entry(20)
        self.window().mainloop()



c = Calc(350, 350, 'green', 'Мой калькулятор')
c.start()
