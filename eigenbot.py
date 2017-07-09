# Open up a connection with the chat - a socet
# TODO add quotes from chat to list
import string
from commands import get_user, get_message
from Socket import openSocket, sendMessage
import socket
from initialize import joinRoom
import random
import threading
import time
from info import facts
from info import game_wr
from info import bad_words

mutex = threading.Lock()


def reconnect():
    try:
        s = openSocket()
        joinRoom(s)  # initializing, can do it in while loop as well
        return s
    except socket.error as e:
        print(e)
        return e
s = reconnect()
readbuffer = ""

current_game = str(input("What game are you playing?: "))


def timeout(s, user, sec):
    sendMessage(s, "/timeout ".format(user, sec))
    time.sleep(2)
    sendMessage(s, ("Sorry " + str(user) + ", you've been sent to the thoughtful corner."))


def print_fact():
    global s
    while True:
        # why need to initalize with !wr for it to start working?
        try:
            sendMessage(s, random.choice(facts))
        except socket.error as e:
            print(e)
            with mutex:
                s = reconnect()
        time.sleep(420)

threading.Timer(10.0, print_fact).start()

while True:
    bites = s.recv(1024)
    readbuffer = readbuffer + bites.decode()  # read info from the buffer
    temp = readbuffer.split("\n")
    readbuffer = temp.pop()
    
    for line in temp:
        print(line)
        if "PING" in line:
            try:
                s.send("PONG :tmi.twitch.tv\r\n".encode())
                # s.send(bytes(line.replace("PING", "PONG"), "UTF-8"))  # could do so check if sent by twitch
                print("PONG sent!")
            except socket.error as e:
                print(e)
                s = reconnect()
            break
        user = get_user(line)
        message = get_message(line)
        print(user + " typed: " + message)
        # COMMANDS
        if "!wr" in message or "!WR" in message:  # just replyies to everything like that
            try:
                sendMessage(s, game_wr[current_game])
            except socket.error as e:
                print(e)
                s = reconnect()
            break
        else:
            pass
        for word in bad_words:
            if word in message:
                timeout(s, user, 30)
                break
