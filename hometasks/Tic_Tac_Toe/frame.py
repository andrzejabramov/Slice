import tkinter as tk
from tkinter import ttk


def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

window = create_widget(None, tk.Tk)
window.title('GUI Example')

frame = create_widget(window, tk.Frame, bg='red',
                      bd=3, highlightcolor='green', highlightbackground='blue')
frame.pack(padx=200, pady=200)


window.mainloop()