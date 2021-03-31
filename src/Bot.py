#
# Created on Tue Mar 30 2021
#
# Copyright (c) 2021 Letus Entertainment
#


import Commands
import discord
import os

client = discord.Client()

prefix = "!"

@client.event
async def on_ready():
	print("We have logged in!")


# fires everytime a user sends a message
# determine if the message was a commands, and then utilize the commands module
# to determine what happens with the command
@client.event
async def on_message(message):
	if message.author == client.user:
			return

	splitMessage = message.content.split(" ")
	commandWordWithPrefix = splitMessage[0]
	command = commandWordWithPrefix[1:]

	splitMessage.remove(commandWordWithPrefix)

	# push heavy lifting off to the commands module
	if message.content.startswith(prefix):
		await Commands.runCommand(command, message, splitMessage)

client.run("Njk2MTk0NTIxNTk1MjQ4NjUx.XolLrA.pAiKuEdrDnzU0Fwx0ScG3wurwl4")