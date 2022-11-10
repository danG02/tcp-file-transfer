
import socket
import sys
import tkinter.filedialog
from tkinter import *
import os
import glob
window = Tk()
window.title("enter IP")
window.geometry("200x50")

#filetosend = tkinter.filedialog.askopenfilename()
#with open(filetosend, "r") as f:
#    data = f.read()


HOST = ""
WaitForIP = True

def ConnectIP():
    text = e1.get()
    
    global HOST
    HOST = text
    
    #Label(window, text=text, font = ('Century 15 bold')).grid(row = 4)
    global WaitForIP
    WaitForIP = False

Label(window, text='IP address').grid(row=0)
e1 = Entry(window)
e1.grid(row=0, column=1)
b = Button(window, text="Connect", command=ConnectIP)
b.grid(row=1, column=1)
#b = Button(window, text="Encrypt", command=ceaserEncrypt)
#b.grid(row=2, column=1)
while WaitForIP:
    window.update_idletasks()
    window.update()

window.destroy()
PORT = 5001

s = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("[+] Connected with Server")

keepWindowOpen = True


def CloseWindow():
    global keepWindowOpen
    keepWindowOpen = False
    # close connection
    s.close()
    print("[-] Disconnected")
    sys.exit(0)

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

def UploadFile():
    filepath = tkinter.filedialog.askopenfilename()
    print(filepath)
    # open file
    with open(filepath, "rb") as f:
        # send file
        print("[+] Sending file...")
        data = f.read()
        s.sendall(data)

b1 = Button(connected, text="Upload", command=UploadFile)
b1.grid(row=0, column=0)
b2 = Button(connected, text="Download")
b2.grid(row=2, column=0)
b3 = Button(connected, text="Finish", command=CloseWindow)
b3.grid(row=3, column=0)
e = Entry(connected)
e = grid(row=2, column=1)
l = Label(connected, text=applytoLabel())
l.grid(row = 1, column = 3)
while keepWindowOpen:
    connected.update_idletasks()
    connected.update()

connected.destroy()
