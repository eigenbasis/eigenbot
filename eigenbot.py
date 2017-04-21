# Open up a connection with the chat - a socet
import string
from commands import get_user, get_message
from Socket import openSocket, sendMessage
from initialize import joinRoom
import random
import threading
from info import facts

s = openSocket()
joinRoom(s)  # initializing, can do it in while loop as well
readbuffer = ""


def print_fact():  # why need to initalize with !wr for it to start working?
    threading.Timer(420.0, print_fact).start()
    sendMessage(s, random.choice(facts))

print_fact()

while True:
    bites = s.recv(1024)
    readbuffer = readbuffer + bites.decode()  # read info from the buffer
    temp = readbuffer.split("\n")
    readbuffer = temp.pop()

    for line in temp:
        print(line)
        if "PING" in line:
            s.send(bytes(line.replace("PING", "PONG"), "UTF-8"))  # could do so check if sent by twitch
            print("PONG sent!")
            break
        user = get_user(line)
        message = get_message(line)
        print(user + " typed: " + message)
        if "!wr" in message or "!WR" in message:  # just replyies to everything like that
            sendMessage(s, "Syberia's WR is 2:00:16 by Nicko!")
            break
        else:
            pass
