# En este ejercicio tenéis que crear una lista de RadioButton 
# que muestre la opción que se ha seleccionado y
# que contenga un botón de reinicio para que deje todo como al principio.

#Al principio no tiene que haber una opción seleccionada.

import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Ejercicio 10 - Open Bootcamp')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

label = tkinter.Label(window, text='Estaria dispuesto a aprender Python?')
label.grid(row=0, column = 0)

# variable que almacena la opcion seleccionada
selected = tkinter.IntVar()

def showresult():
 print(selected.get())
 show.config(text="{}".format(selected.get()))

def reset():
    selected.set(None)
    show.config(text="Escoja uno")

r1 = ttk.Radiobutton(window, text='Si', value=1, variable=selected, command=showresult)
r2 = ttk.Radiobutton(window, text='No', value=2, variable=selected, command=showresult)
r3 = ttk.Radiobutton(window, text='Tal vez', value=3, variable=selected, command=showresult)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)




button = tkinter.Button(window, text='Reset', command=reset)
button.grid(column=1, row=1, pady=5, padx=5)

show = tkinter.Label(window)
show.grid(row=2, column = 1, pady=5, padx=5)
window.mainloop()

