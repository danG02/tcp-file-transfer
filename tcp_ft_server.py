import socket
import sys
import pickle
import os
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
        # f = open('.\\files\\file_'+ str(i)+".txt",'wb') # Open in binary
        # get file bytes
        data = conn.recv(size)
        if size == 4096:
            size = len(data)
        obj = pickle.loads(data)
        if obj['mode'] == "upload":
            f = open('files/' + obj['filename'], "ba")  # uncomment this if on mac
            # write bytes on file
            f.write(obj['data'])
            f.close()
        elif obj['mode'] == "dir":
            size = 4096
            myList = os.listdir(".\\files")
            conn.sendall(pickle.dumps(myList))

        elif obj['mode'] == "download":
            size = 4096
            file = obj['filename']
            print(obj['filename'])
            filepath = (".\\files\\" + file + ".txt")
            print(os.path.isfile(filepath))
            with open(filepath, "rb") as f:
                # send file
                print("[+] Sending file...")
                while True:
                    chunk = f.read()
                    if chunk == '':
                        break
                    obj78 = {'filename': file, 'data': chunk}
                    print(len(pickle.dumps(obj78)))
                    conn.sendall(pickle.dumps(obj78))
                print("Done Sending!")

    # print("[+] Download complete!")

    # close connection
    conn.close()
    print("[-] Client disconnected")
    # sys.exit(0)
