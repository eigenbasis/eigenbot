# Socket.py

import socket
from settings import HOST, PORT, PASS, NICK, CHANNEL


def openSocket():

    s = socket.socket()  # that creates the intial socket
    s.connect((HOST, PORT))  # connect with the host
    sendPASS = "PASS " + PASS + "\r\n"
    s.send(sendPASS.encode())  # "PASS oath:dsfds\r\n"
    sendNICK = "NICK " + NICK + "\r\n"
    s.send(sendNICK.encode())  # after this you should be signed in and connected
    sendJOIN = "JOIN #" + CHANNEL + "\r\n"
    s.send(sendJOIN.encode())
    return s


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
    s.send(messageTemp.encode())  # sends message over socket
    print("Sent: " + messageTemp)
