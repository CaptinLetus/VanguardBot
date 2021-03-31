#
# Created on Wed Mar 31 2021
#
# Copyright (c) 2021 Letus Entertainment
#

#import Notify
import CommandFunctions.Notify as Notify 
import discord

AMOUNT_OF_BARS = 5

# returns the xp for a user
async def get_xp(message, other_words):
	xpEmbed = discord.Embed(
		title = "Your XP!",
		description = "You have 800 xp",
		colour = discord.Colour.light_gray()
	)

	# progres bar to next rank
	current_xp = 80
	needed_xp = 100
	percentage_to_next_level = (current_xp/needed_xp)

	# build the progress bar
	bar = ""
	for i in range(AMOUNT_OF_BARS):
		if i/AMOUNT_OF_BARS < percentage_to_next_level:
			bar += "🟩"
		else:
			bar += "⬜"

	# add bar info to the embed
	xpEmbed.add_field(name="Next rank", value="Trooper", inline=True)
	xpEmbed.add_field(name="Progress", value=bar, inline=True)

	await message.channel.send(embed=xpEmbed)


# gives xp to a user
async def give_xp(message, other_words):
	# make sure the input is correct
	if len(other_words) == 0:
		await Notify.warn(message, "Please specify the amount of XP to award")
		return

	if len(other_words) == 1:
		await Notify.warn(message, "Please mention the user(s) you want to give XP to")
		return

	amount = other_words[0]

	# typecheck
	if not isinstance(amount, int):
		await Notify.error(message, "The amount must be a number!")
		return

	# perform the give
	other_words.remove(amount)
	awardTo = other_words

	for user in awardTo:
		await message.channel.send(f"Give {amount} XP to {user}")
