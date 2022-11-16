  
import socket
import sys
import tkinter.filedialog
from tkinter import *
import os
import glob
import pickle
import tkinter.messagebox as box
window = Tk()
window.title("enter IP")
window.geometry("200x50")

#filetosend = tkinter.filedialog.askopenfilename()
#with open(filetosend, "r") as f:
#    data = f.read()
nameFile =""
filename = StringVar()
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
connected.geometry("500x200")


#def applytoLabel():
    #path = (".\\files")
 #   path = ("files") #uncomment this line if on mac
  #  arr = os.listdir(path)
   # n = len(arr)
    #element = ''
    #for i in range(n):
    #    element = element + arr[i] + '\n'
   # return element

def UploadFile():
    filepath = tkinter.filedialog.askopenfilename()
    print(filepath)
    # open file
    with open(filepath, "rb") as f:
        # send file
        print("[+] Sending file...")
        n = 1000
        while True:
            chunk = f.read(n)
            if chunk == '':
                break
            obj = {'filename': filepath.split('/')[-1], 'data': chunk, 'mode': "upload"}
            print(len(pickle.dumps(obj)))
            s.sendall(pickle.dumps(obj))
        print("Done Sending!")


def getDirectory():
    global nameFile
    obj = {'mode': "dir"}
    s.sendall(pickle.dumps(obj))
    rcv = s.recv(1024)
    obj2 = pickle.loads(rcv)

    window = Tk()
    window.title('Downloads')
    frame = Frame(window)
    myListBox = Listbox(window)
    for file in obj2:
        myListBox.insert(END, file)
    myListBox.pack()

    def dialog():
        global nameFile
        box.showinfo('Selection', 'Your Choice: ' + \
                     myListBox.get(myListBox.curselection()) + ' was downloaded successfully')
        nameFile = myListBox.get(myListBox.curselection())
    btn = Button(frame, text='Download File', command=dialog)
    btn.pack(side=RIGHT, padx=5)
    myListBox.pack(side=LEFT)
    frame.pack(padx=30, pady=30)
    print(nameFile)

    obj3 = {'filename': myListBox.get(myListBox.curselection()), 'mode': "download"}
    s.sendall(pickle.dumps(obj3))


    finalFile = s.recv(1024)
    objFinal = pickle.loads(finalFile)
    f = open(".\\files2" + objFinal['filename'], "ba")  # uncomment this if on mac
    f.write(objFinal['data'])
    f.close()

#def downloadFile():


b1 = Button(connected, text="Upload", command=UploadFile)
b1.grid(row=0, column=0)
b2 = Button(connected, text="Download", command=getDirectory)
b2.grid(row=2, column=0)
b3 = Button(connected, text="Finish", command=CloseWindow)
b3.grid(row=3, column=0)



while keepWindowOpen:
    connected.update_idletasks()
    connected.update()

connected.destroy()
