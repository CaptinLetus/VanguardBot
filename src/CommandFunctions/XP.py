#
# Created on Wed Mar 31 2021
#
# Copyright (c) 2021 Letus Entertainment
#

#import Notify
import CommandFunctions.Notify as Notify 
from Bot import client
import discord

AMOUNT_OF_BARS = 5

def get_current_xp(member):
	return 100

def get_xp_for_next_rank(member):
	return 100

async def print_xp_for_member(message, member):
	xpEmbed = discord.Embed(
		title = "XP for " + member.name,
		description = "You have 800 xp",
		colour = discord.Colour.light_gray()
	)

	# progres bar to next rank
	current_xp = get_current_xp(member)
	needed_xp = get_xp_for_next_rank(member)
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

# returns the xp for a user
async def print_xp(message, other_words):
	member = message.author

	# if the author has defined multiple people in their request, print info for all users
	if len(other_words) == 0:
		await print_xp_for_member(message, message.author)
	else:
		print(other_words)
		for member in other_words:
			memberId = member.strip("<!@>")
			member = client.get_user(int(memberId))

			await print_xp_for_member(message, member)


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
