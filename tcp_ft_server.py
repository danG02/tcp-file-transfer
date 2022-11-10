import socket
import sys
import pickle

HOST = ""
PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Listening ...")

while True:
    conn, addr = s.accept()
    print("[+] Client connected: ", addr)

    size = 4096
    while True:
        # get file name to download
        # Read shove it in a dictionary -> {file name: ~, data: ~}
        #f = open('.\\files\\file_'+ str(i)+".txt",'wb') # Open in binary
        # get file bytes
        data = conn.recv(size)
        if size == 4096:
            size = len(data)
        obj = pickle.loads(data)
        f = open('files/' + obj['filename'],"ba") #uncomment this if on mac
        # write bytes on file
        f.write(obj['data'])
        f.close()

    #print("[+] Download complete!")

    # close connection
    conn.close()
    print("[-] Client disconnected")
    #sys.exit(0)