import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    geo = '450x450'
    def __init__(self):
        super().__init__()
        self.title('Крестики-нолики')
        self.geometry(self.geo)
        self.btn_sq = float(self.geo.split('x')[0]) / 3
        self.area()

    def click(self):
        print('X')

    def area(self):
        btn = tk.Button(padx=0, pady=0, height=8, width=10)
        # n = m = 0
        # for i in range(0, 3):
        #     for j in range(0, 3):
        #         btn = tk.Button(padx=n+i*self.btn_sq, pady=m+j*self.btn_sq, height=100, width=100)
        #         tk.Button.pack(btn)
        btn.pack()

        # self.btn = tk.Button(self, text='', command=self.click())
        # self.btn.pack(padx=120, pady=30)

