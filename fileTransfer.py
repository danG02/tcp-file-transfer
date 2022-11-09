import socket
import sys
import tkinter.filedialog


filetosend = tkinter.filedialog.askopenfilename()
with open(filetosend, "r") as f:
    data = f.read()

HOST = "192.168.1.100"
PORT = 9999

s = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("[+] Connected with Server")

# get file name to send
f_send = "file_to_send.mp3"
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

