from tkinter import Tk, Label, Button


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title('Мой первый GUI')

        self.label = Label(master, text='Мой первый GUI, Ура!!!')
        self.label.pack()

        self.greet_button = Button(master, text='Привет', command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text='Закрыть', command=master.quit)
        self.close_button.pack()

    def greet(self):
        print('Приветствую!!!')


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
