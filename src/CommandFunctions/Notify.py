#
# Created on Wed Mar 31 2021
#
# Copyright (c) 2021 Letus Entertainment
#
# This module is used to notify the person using the bot of different errors

import discord

icon = "https://cdn.discordapp.com/attachments/811651953657774130/826796628462927872/CaptinLetusGroupLogo.png"

async def warn(message, warning): 
	newEmbed = discord.Embed(
		title = "Warning!",
		description = warning,
		colour = discord.Colour.gold()
	)

	newEmbed.set_thumbnail(url=icon)
	newEmbed.set_author(name="Vanguard Bot", icon_url=icon)

	await message.channel.send(embed=newEmbed)
