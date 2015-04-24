
"""
This is user interface? when user input data
"""

from tkinter import *
import sys
from tkinter.ttk import Style
import sqlite3
from model.modeling_process import modeling_with_method, modeling_without_method
from channel.channel import checking_mistake
import numpy as np
import matplotlib.pyplot as plt

def modeling(enter_message, mistake_of_channel, asked_with, asked_without, receiver, receiver2, conn):


    #conn.execute("DROP TABLE EXPERIMENTS;")

    #conn.execute('''CREATE TABLE EXPERIMENTS
    #   (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #   PROBABILITY1           REAL    NOT NULL,
    #   ASKED1            INT     NOT NULL,
    #   ASKED2            INT     NOT NULL);''')

    message = int(enter_message.get('1.0', END))
    mist = mistake_of_channel.get('1.0', END)


    print('Mist', mist)
    print("Message", message)

    ask_without, receiv_val2 = modeling_without_method(message, mist)
    ask_with, receiv_val1 = modeling_with_method(message, mist)

    print('as_with', ask_with, 'rec1', receiv_val1)
    print('as_without', ask_without, 'rec2', receiv_val2)

    asked_with.set(ask_with)
    asked_without.set(ask_without)
    receiver.set(receiv_val1)
    receiver2.set(receiv_val2)

    insert = " INSERT INTO EXPERIMENTS (PROBABILITY1, ASKED1, ASKED2) VALUES (" + str(checking_mistake(mist)) +\
        ", " + str(ask_with) + ", " + str(ask_without) + ");"
    conn.execute(insert)


    print('click')


def show_graphic(conn):
    select = "SELECT PROBABILITY1, ASKED1, ASKED2 FROM EXPERIMENTS;"
    as2 = conn.execute(select)
    probs = []
    ask1 = []
    ask2 = []
    for x in as2:
        print("with", x)
        probs.append(x[0])
        ask1.append(x[1])
        ask2.append(x[2])

    plt.xlabel( "X values" )
    plt.ylabel( "Y values" )
    plt.plot(ask1, probs, "r--", ask2, probs, ":b^")
    plt.show()

    print('Show graphic')


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        conn = sqlite3.connect('test.db')
        conn1 = sqlite3.connect('test.db')
        print("Opened database successfully")

        self.parent.title("Двухканальная система передачи данных")

        self.style = Style()

        #self.pack(fill=BOTH, expand=1)
        self.style.configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')
        self.style.configure("TLabel", padding=(0, 5, 0, 5),
            font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.rowconfigure(8, pad=3)
        self.rowconfigure(9, pad=3)
        self.rowconfigure(10, pad=3)

        """
            Column = 0
        """
        enter_send_message_label = Label(self, text='Значение посылки', width=30, height=1, font='Arial 12 bold')
        enter_send_message_label.grid(row=0, column=0)

        enter_message_text = Text(self, height=1, width=10, font='Arial 12')
        enter_message_text.grid(row=1, column=0)

        modelling_button = Button(self, text='Моделировать', bg='#7DC6FC', fg='black', width=15, height=1, command=
    (lambda: modeling(enter_message_text, enter_probability, asked_with, asked_without, received_message, received_message1, conn)), font='Arial 12 bold')
        modelling_button.grid(row=10, column=0)

        """
            Column = 1
        """
        probability_channel_label = Label(self, text='Вероятность ошибки в каналах\n Например: 10^-5', width=30, height=2, font='Arial 12 bold')
        probability_channel_label.grid(row=0, column=1)

        enter_probability = Text(self, height=1, width=10, font='Arial 12')
        enter_probability.grid(row=1, column=1)

        """
            Column = 2
        """
        label1 = Label(self, text='Результаты без применения способа', font='Arial 12 bold')
        label1.grid(row=0, column=2)

        asked_without_label = Label(self, text='Количество переспросов', width=40, height=3, font='Arial 12')
        asked_without_label.grid(row=1, column=2)

        asked_without = StringVar()
        asked_without_text = Label(self, textvariable=asked_without, font='Arial 12')
        asked_without_text.grid(row=1, column=3)

        received_mess_label = Label(self, text='Полученная посылка', width=40, height=3, font='Arial 12')
        received_mess_label.grid(row=2, column=2)

        received_message1 = StringVar()
        received_message_text1 = Label(self, textvariable=received_message1, width=15, height=3, font='Arial 12')
        received_message_text1.grid(row=2, column=3)

        label2 = Label(self, text='Результаты с применением способа', font='Arial 12 bold')
        label2.grid(row=3, column=2)

        asked_with_label = Label(self, text='Количество переспросов', width=40, height=1, font='Arial 12')
        asked_with_label.grid(row=4, column=2)

        asked_with = StringVar()
        asked_with_text = Label(self, textvariable=asked_with, font='Arial 12')
        asked_with_text.grid(row=4, column=3)

        received_mess_label = Label(self, text='Полученная посылка', width=40, height=3, font='Arial 12')
        received_mess_label.grid(row=5, column=2)

        received_message = StringVar()
        received_message_text = Label(self, textvariable=received_message, width=15, height=3, font='Arial 12')
        received_message_text.grid(row=5, column=3)


        show_diagramm_button = Button(self, text='Показать график', bg='#7DC6FC', fg='black', width=15, height=1,
                                      command=(lambda: show_graphic(conn)), font='Arial 12 bold')
        show_diagramm_button.grid(row=10, column=2)

        self.pack()

def main():

    root = Tk()
    #root.geometry('700x500')
    root['bg'] = '#D4FCF0'
    root.configure(background='#D4FCF0')
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()