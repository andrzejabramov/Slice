import tkinter as tk


class Tic_Tac_Toe:
    root = tk.Tk()
    count = 1
    btn = []

    def window(self):
        self.root.title('Крестики-Нолики')
        self.root.geometry('250x250')
        self.root.resizable(False, False)
        self.root.configure(bg='black')
        self.__buttons()
        return self.root

    def __buttons(self):
        for i in range(3):
            self.root.rowconfigure(index=i, weight=1)
            for j in range(3):
                self.root.columnconfigure(index=j, weight=1)
                self.btn = tk.Button(self.root, text='    ', font='Arial 24')
                self.btn.configure(command=self.__click)
                self.btn.grid(row=i, column=j, ipadx=20, ipady=18, padx=0.5, pady=0.5, sticky='nsew')

    def __click(self):
        self.count += 1
        letter = 'X' if self.count == 1 or self.count % 2 != 0 else 'O'
        self.btn['text'] = letter
        self.btn.configure(state='disable')
        return letter









t = Tic_Tac_Toe()
t.window().mainloop()

