import socket
import sys
import tkinter.filedialog
from tkinter import *

window = Tk()
window.title("enter IP")
window.geometry("250x250")

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

# get file name to send
f_send = "pizza.txt"
# open file
with open(f_send, "rb") as f:
    # send file
    print("[+] Sending file...")
    data = f.read()
    s.sendall(data)

    # close connection
    s.close()
    print("[-] Disconnected")
    sys.exit(0)

