#
# Created on Wed Mar 31 2021
#
# Copyright (c) 2021 Letus Entertainment
#

#import Notify
import CommandFunctions.Notify as Notify 

# returns the xp for a user
async def get_xp(message, other_words):
	await message.channel.send("Getting xp...")


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

	other_words.remove(amount)
	awardTo = other_words

	for user in awardTo:
		await message.channel.send(f"Give {amount} XP to {user}")
