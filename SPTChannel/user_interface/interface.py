__author__ = 'sergey'

"""
This is user interface? when user input data
"""

from tkinter import *
import sys

def quit():
    print('Hello, I must be going...')
    sys.exit()
def inputs_param(text):
    print(text)
'''
root = Tk()
message_label = Label(root, text='Iputs message')
message_label.pack()
text = Text(root)
text.pack()
widget = Button(None, text='Hello GUI world', command=(lambda : inputs_param(text)))
widget.pack()
widget.mainloop()

'''
def handler(name):
    print(name)

def func():
    root = Tk()
    labelfont = ('times', 20, 'bold')
# семейство, размер, стиль
    widget = Label(root, text='Hello config world')

    widget.config(bg='black', fg='yellow') # желтый текст на черном фоне
    widget.config(font=labelfont)
# использовать увеличенный шрифт
    widget.config(height=3, width=20)
# начальный размер: строк,символов
    widget.pack(expand=YES, fill=BOTH)

    root.mainloop()
    print('Tab button')
root = Tk()
labelfont = ('times', 20, 'bold')
# семейство, размер, стиль
widget = Label(root, text='Hello config world')
label = Button(root, text='My button', command=func)
widget.config(bg='black', fg='yellow') # желтый текст на черном фоне
widget.config(font=labelfont)
# использовать увеличенный шрифт
widget.config(height=3, width=20)
# начальный размер: строк,символов
widget.pack(expand=YES, fill=BOTH)
label.pack()
root.mainloop()

