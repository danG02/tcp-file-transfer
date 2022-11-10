import os
from tkinter import *


connected = Tk()
connected.title("Server")
connected.geometry("200x75")
def applytoLabel():
    path = ("..\\tcp-file-transfer\\files")
    arr = os.listdir(path)
    n = len(arr)
    element = ''
    for i in range(n):
        element = element + arr[i] + '\n'
    return element

l = Label(connected, text=applytoLabel())
l.grid(row = 1, column = 3)
connected.mainloop()