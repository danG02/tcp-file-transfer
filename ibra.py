import os
from tkinter import *
import tkinter.messagebox as box

connected = Tk()
connected.title("Server")
connected.geometry("500x200")
def downloadFile():
    window = Tk()
    window.title('Downloads')
    frame = Frame(window)
    myList = os.listdir(".\\files")
    myListBox = Listbox(window)
    for file in myList:
        myListBox.insert(END, file)
    myListBox.pack()

    def dialog():
        box.showinfo('Selection', 'Your Choice: ' + \
                     myListBox.get(myListBox.curselection()) + ' was downloaded successfully')

    btn = Button(frame, text='Download File', command=dialog)
    btn.pack(side=RIGHT, padx=5)
    myListBox.pack(side=LEFT)
    frame.pack(padx=30, pady=30)

b2 = Button(connected, text="Download", command=downloadFile)
b2.grid(row=2, column=0)

connected.mainloop()