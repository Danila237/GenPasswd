import random
from tkinter import *
import string

def generate_password():
    password = []
    for i in range(16):
        alpha = random.choice(string.ascii_letters)
        simbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(simbol)
        password.append(numbers)
        y = "".join(str(x) for x in password)
    lbl.config(text = y)

root = Tk()
root.geometry('600x200')
btn = Button(root, text = 'Generate password', command = generate_password)
btn.grid(row = 2, column = 2)
lbl = Label(root, font = ('times', 15, 'bold'))
lbl.grid(row = 4, column = 2)
root.mainloop()
