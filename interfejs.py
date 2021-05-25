from tkinter import Tk, Button, mainloop, Label, Entry
from create_map import *

def interfejs():
    window = Tk()
    window.geometry("500x200")
    label1 = Label(window, text="Wpisz liczbę wierszy:")
    label2 = Label(window, text="Wpisz liczbę kolumn:")
    label3 = Label(window, text="Wpisz masowość zielonych obszarów:")
    label1.grid(row=0, column=0, padx=5, pady=5)
    label2.grid(row=1, column=0, padx=5, pady=5)
    label3.grid(row=2, column=0, padx=5, pady=5)
    entry2 = Entry(window)
    entry2.grid(row=1, column=1, padx=5, pady=5)
    e = Entry(window)
    e.grid(row=0, column=1, padx=5, pady=5)
    e1 = Entry(window)
    e1.grid(row=2, column=1, padx=5, pady=5)
    button = Button(text="Generuj mapę", command=lambda: create_map(int(e.get()), int(entry2.get()), int(e1.get())))
    button.grid(row=4, column=0, padx=10, pady=10)

    mainloop()
