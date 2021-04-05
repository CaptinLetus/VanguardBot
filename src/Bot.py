#
# Created on Tue Mar 30 2021
#
# Copyright (c) 2021 Letus Entertainment
#


from discord.ext import commands
import os
import Secrets

PREFIX = "!"
client = commands.Bot(command_prefix = PREFIX)


@client.event
async def on_ready():
	print("We have logged in!")


# don't run with unit tests
if __name__ == '__main__':
	for filename in os.listdir("./src/cogs"):
		if filename.endswith(".py"):
			client.load_extension(f"cogs.{filename[:-3]}")

	client.run(Secrets.getToken())