
"""
This is user interface? when user input data
"""

from tkinter import *
import sys


def modeling(enter_message, polynom, send_message, mistake_of_channel):
    print('click')
    polynom.set(enter_message.get('1.0', END))
    send_message.set('Send message')
    print('Mistake', mistake_of_channel.get('1.0', END))


def show_graphic():
    print('Show graphic')

root = Tk()
root.geometry('700x500')
root['bg'] = 'gray'

"""
Frame #1. There are enter message of user, view choice polynomial,
send message
"""
frame = Frame(root, width=100, height=50)

label1 = Label(frame, text='My label')
label1.pack()
enter_message = Text(frame, height=1, width=10, fg='red', font='Arial 14')
enter_message.pack()

polynomial = StringVar()
label = Label(frame, textvariable=polynomial)
label.pack()

send_message = StringVar()
send_message_label = Label(frame, textvariable=send_message)
send_message_label.pack()

"""
Frame #2. There are symbolic channel #1, channel #2, label for enter
mistake of channel, button for modeling
"""
frame1 = Frame(root, width=100, height=50)

channel1 = Label(frame1, text="CHANNEL #1")
channel1.pack()

channel2 = Label(frame1, text="CHANNEL #2")
channel2.pack()

mistake_label = Label(frame1, text='Вероятность ошибки в каналах\n Например: 10^-5')
mistake_label.pack()

enter_mistake_of_channel = Text(frame1, height=1, width=10, fg='black',
                                font='Arial 14')
enter_mistake_of_channel.pack()

modeling_button = Button(frame1, text='Modeling', width=5, height=2,
                         bg='gray', fg='white', command=
    (lambda: modeling(enter_message, polynomial, send_message, enter_mistake_of_channel)))
modeling_button.pack()




"""
Frame #3. There are received_message_label, number_of_asked without
my method, number_of_asked with my method.
"""
frame2 = Frame(root, width=100, height=50)

received_message = StringVar()
received_message_label = Label(frame2, textvariable=received_message, fg='blue')
received_message_label.pack()

number_asked_without = StringVar()
number_asked_without_label = Label(frame2, textvariable=number_asked_without,
                                   fg='green', width=20, height=1)
number_asked_without_label.pack()

number_asked_with = StringVar()
number_asked_with_label = Label(frame2, textvariable=number_asked_with, fg='black')
number_asked_with_label.pack()

button2 = Button(frame2, text='Показать график зависимости', command=(lambda: show_graphic()))
button2.pack()




"""
Pack frame
"""
frame.pack(side=LEFT, expand=YES)
frame1.pack(side=LEFT, expand=YES)
frame2.pack(side=LEFT, expand=YES)
root.mainloop()

