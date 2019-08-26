import telepot

bot = telepot.Bot("760095507:AAFrFf2r4es8dWeK49lMlcs3v7hIvsf48Fg")

def receiveMsg(msg):
	print (msg["text"])

bot.message_loop(receiveMsg)

while True:
	pass