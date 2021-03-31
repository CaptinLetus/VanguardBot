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

	split_message = message.content.split(" ")
	command_word_with_prefix = split_message[0]
	command = command_word_with_prefix[1:]

	split_message.remove(command_word_with_prefix)

	# push heavy lifting off to the commands module
	if message.content.startswith(prefix):
		await Commands.run_command(command, message, split_message)

# don't run with unit tests
if __name__ == '__main__':
	client.run("Njk2MTk0NTIxNTk1MjQ4NjUx.XolLrA.pAiKuEdrDnzU0Fwx0ScG3wurwl4")