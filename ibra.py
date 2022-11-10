import os

path = ("C:\\Users\\ibroh\\OneDrive\\Documents\\GitHub\\tcp-file-transfer\\files")
arr = os.listdir(path)
for i in arr:
    print(i, end = '\n')