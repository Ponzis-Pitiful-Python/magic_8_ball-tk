#Orig code: https://stackoverflow.com/questions/34793321/how-to-display-an-output-using-entry-widget-in-python
import random
import time
from tkinter import *
from tkinter.messagebox import *


def show_answer():

    answer = random.randint(0, 19)
    time.sleep(1.6)
    if answer == 0:
        puff = "It is certain."
    elif answer == 1:
        puff = "It is decidedly so."
    elif answer == 2:
        puff = "Without a doubt."
    elif answer == 3:
        puff = "Yes - definitely."
    elif answer == 4:
        puff = "You may rely on it."
    elif answer == 5:
        puff = "As I see it, yes."
    elif answer == 6:
        puff = "Most likely."
    elif answer == 7:
        puff = "Outlook good."
    elif answer == 8:
        puff = "Yes."
    elif answer == 9:
        puff = "Signs point to yes."
    elif answer == 10:
        puff = "Reply hazy, try again"
    elif answer == 11:
        puff = "Ask again later."
    elif answer == 12:
        puff = "Better not tell you now."
    elif answer == 13:
        puff = "Cannot predict now."
    elif answer == 14:
        puff = "Concentrate and ask again."
    elif answer == 15:
        puff = "Don't count on it."
    elif answer == 16:
        puff = "My reply is no."
    elif answer == 17:
        puff = "My sources say no."
    elif answer == 18:
        puff = "Outlook not so good."
    elif answer == 19:
        puff = "Very doubtful."

    blank.insert(0, puff)


def clear_answer():

    blank.delete('0', END)


main = Tk()
Label(main, text=" I am magic 8 ball, ask your question. ").grid(row=0, columnspan=3, sticky=W, pady=1)

blank = Entry(main)

blank.grid(row=1, column=0, columnspan=2, sticky=W)

Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=1)
Button(main, text='Show answer', command=show_answer).grid(row=4, column=1, sticky=W, pady=1)
Button(main, text='Clear', command=clear_answer).grid(row=4, column=2, sticky=W, pady=1)

mainloop()