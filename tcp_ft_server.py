import socket
import sys

HOST = ""
PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Listening ...")

while True:
    conn, addr = s.accept()
    print("[+] Client connected: ", addr)

    i=1
    while True:
        # get file name to download
        f = open('.\\files\\file_'+ str(i)+".txt",'wb') # Open in binary
        #f = open('./files/file_' + str(i)+".txt","wb") #uncomment this if on mac
        i=i+1
        # get file bytes
        data = conn.recv(4096)
        if not data:
            break
        # write bytes on file
        f.write(data)
    f.close()
    print("[+] Download complete!")

    # close connection
    conn.close()
    print("[-] Client disconnected")
    #sys.exit(0)