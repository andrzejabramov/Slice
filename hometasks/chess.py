from tkinter import *

root = Tk()
root.title('Шашки')

canvas = Canvas(root, width=700, height=700)
canvas.pack()


def square():
    y = 0
    while y < 700:
        x = 0
        while x < 700:
            canvas.create_rectangle(x, y, x+88, y+88, fill='#fff', outline='#000')
            x += 88

        y += 88


def board():
    fill = '#FECD72'
    outline = '#825100'
    for i in range(0, 8):
        for j in range(0, 8):
            canvas.create_rectangle(i*88, j*88, i*88 + 88, j*88 + 88, fill=fill, outline=outline)
            fill, outline = outline, fill

        fill, outline = outline, fill


# def checkers():
#     fill = '#fff'
#     outline = '#000'
#     for check in range(0, 8, 2):
#         oval =canvas.create_oval(check * 88, check * 88, check * 88 + 88, check * 88 + 88, fill=fill, outline=outline)


square()
board()
#checkers()
root.mainloop()