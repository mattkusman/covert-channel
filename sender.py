import fs_emulator as fs

file = False
fs.set_free('./file.txt')

while(True):
    print("Enter a 1 or 0")
    msg = bool(int(input()))

    if not msg:
        while(not file):
            file = fs.my_open("./file.txt", "r")
    else:
        if (file):
            fs.my_close(file)
