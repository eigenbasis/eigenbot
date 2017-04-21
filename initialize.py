# initialize.py

import string
from Socket import sendMessage


def joinRoom(s):
    readbuffer = ""
    Loading = True  #
    while Loading:
        bites = s.recv(1024)
        readbuffer = readbuffer + bites.decode()  # read info from the buffer
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(s, "Reporting in!")


def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
