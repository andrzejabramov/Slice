from classes import TicTacToe
#https://adior.ru/index.php/robototekhnika/261-bulls-cows-2

if __name__ == '__main__':
    game = TicTacToe()
    game.mainloop()



# root = tk.Tk()
# game = TicTacToe(root)
# root.mainloop()


# root.title("Крестики-нолики")
# canvas = tk.Canvas(root, width=450, height=450, bg='white')
# canvas.pack()
#
#
# def square():
#     y = 0
#     while y < 450:
#         x = 0
#         while x < 450:
#             canvas.create_rectangle(x, y, x + 150, y + 150, fill = "lightgreen")
#             #canvas.create_rectangle(x, y, x+150, y+150, fill='#FFF', outline='#000')
#             x += 150
#         y += 150
#
#
# def board():
#     #fill = '#FECD72'
#     #outline = '#825100'
#     fill = '#FFDAB9'
#     outline = '#FFDAB9'
#
#     for i in range(0, 3):
#         for j in range(0, 3):
#             canvas.create_rectangle(i*150, j*150, i*150 + 150, j*150 + 150, fill=fill, outline=outline)
#             fill, outline = outline, fill
#         fill, outline = outline, fill
#

# def checkers():
#     fill = '#fff'
#     outline = '#000'
#     for check in range(0, 8, 2):
#         oval =canvas.create_oval(check * 88, check * 88, check * 88 + 88, check * 88 + 88, fill=fill, outline=outline)


#square()
#board()

