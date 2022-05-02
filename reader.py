import fs_emulator as fs

message = list()

while(True):
    print("read?")
    input()
    file = fs.my_open("./file.txt", "r")

    if file:
        message.append(1)
        print(1)
        fs.my_close(file)
    else:
        message.append(0)
        print(0)

    print(message)