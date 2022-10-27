#En este segundo ejercicio, tendréis que crear una interfaz sencilla
# la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Ejercicio - 2')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

lista = ['Peugeot', 'Ford', 'Fiat', 'Mercedes', 'Chevrolet', 'BMW']

label = ttk.Label(window, text='Escoja un modelo de automovil')
label.grid(column=0, row=0)


var = tkinter.Variable(value=lista)

selection = tkinter.Listbox(window,  listvariable=var, height= len(lista))
selection.grid(column=0, row=1)

def selected(a):
    selected_indices = selection.curselection()
    show = selection.get(selected_indices)
    result.config(text="Escogiste: {}".format(show))

selection.bind('<<ListboxSelect>>', selected)

result = ttk.Label(window)
result.grid(column=0, row=3)

window.mainloop()