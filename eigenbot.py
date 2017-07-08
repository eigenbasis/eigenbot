# Open up a connection with the chat - a socet
# TODO add quotes from chat to list
import string
from commands import get_user, get_message
from Socket import openSocket, sendMessage
from initialize import joinRoom
import random
import threading
import time
from info import facts
from info import game_wr

s = openSocket()
joinRoom(s)  # initializing, can do it in while loop as well
readbuffer = ""

current_game = str(input("What game are you playing?: "))


def print_fact():
	while True:
		# why need to initalize with !wr for it to start working?
		sendMessage(s, random.choice(facts))
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
			s.send(bytes(line.replace("PING", "PONG"), "UTF-8"))  # could do so check if sent by twitch
			print("PONG sent!")
			break
		user = get_user(line)
		message = get_message(line)
		print(user + " typed: " + message)
		# COMMANDS
		if "!wr" in message or "!WR" in message:  # just replyies to everything like that
			sendMessage(s, game_wr[current_game])
			break
		else:
			pass

