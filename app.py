import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk

root = Tk()
root.geometry('350x606')
root.title('Mood Calculator Questions')

v = tk.IntVar()
w = tk.IntVar()
x = tk.IntVar()
y = tk.IntVar()
z = tk.IntVar()

l1 = Label(root, text='Please do not resize this window.\nThis is not reusable (launch again to use again).\nQuestion 1:\n Did you greet someone when you went near them today?', fg='black')
l1.pack()

rb11 = Radiobutton(root, variable=v, value=4, text='yes', fg='green')
rb12 = Radiobutton(root, variable=v, value=2, text='no ', fg='red'  )
rb11.pack()
rb12.pack()

l2 = Label(root, text='Question 2:\n Did you accomplish something today?', fg='black')
l2.pack()

rb21 = Radiobutton(root, variable=w, value=4, text='yes', fg='green')
rb22 = Radiobutton(root, variable=w, value=2, text='no ', fg='red')
rb21.pack()
rb22.pack()

l3 = Label(root, text='Question 3:\n Did you have a hard time today?', fg='black')
l3.pack()

rb31 = Radiobutton(root, variable=x, value=2, text='yes', fg='red')
rb32 = Radiobutton(root, variable=x, value=4, text='no ', fg='green')
rb31.pack()
rb32.pack()

l4 = Label(root, text='Question 4:\n Did you get bullied or harassed today?', fg='black')
l4.pack()

rb41 = Radiobutton(root, variable=y, value=2, text='yes', fg='red')
rb42 = Radiobutton(root, variable=y, value=4, text='no ', fg='green')
rb41.pack()
rb42.pack()

l5 = Label(root, text='Question 5:\n Pick a word to describe your day.', fg='black')
l5.pack()

rb51 = Radiobutton(root, variable=z, value=8, text='fantastic', fg='lime')
rb52 = Radiobutton(root, variable=z, value=4, text='good     ', fg='green')
rb53 = Radiobutton(root, variable=z, value=2, text='bad      ', fg='red')
rb54 = Radiobutton(root, variable=z, value=1, text='chaotic  ', fg='crimson')
rb51.pack()
rb52.pack()
rb53.pack()
rb54.pack()

mood = Label(root, text='Your mood will appear under "done".')
mood.pack()

def CALCULATE():
    number = v.get()+w.get()+x.get()+y.get()+z.get()
    if number == 24:
        mood = Label(root, text='You are in an ultra cheerful mood!', fg='lime')
        mood.pack()
    elif number > 12:
        mood = Label(root, text='You are in a good mood!', fg='green')
        mood.pack()
    elif number < 12:
        mood = Label(root, text='You are in a bad mood.', fg='red')
        mood.pack()

Done = Button(root, text='Done', fg='turquoise', command=CALCULATE)
Done.pack()

edna_mode = Label(root, text='Credits:\nMade by Yunus Pirim', fg='grey', font=('Times', 8))
edna_mode.pack(side = BOTTOM)

root.mainloop()




