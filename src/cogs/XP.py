from discord.ext import commands
import discord
import Notify

AMOUNT_OF_BARS = 5

class XP(commands.Cog):

	def __init__(self, client):

		self.client = client
	

	def get_current_xp(self, member):

		return 100


	def get_xp_for_next_rank(self, member):

		return 100


	async def print_xp_for_member(self, ctx, member):

		xpEmbed = discord.Embed(
			title = "XP for " + member.name,
			description = "You have 800 xp",
			colour = discord.Colour.light_gray()
		)

		# progres bar to next rank
		current_xp = self.get_current_xp(member)
		needed_xp = self.get_xp_for_next_rank(member)
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

		await ctx.channel.send(embed=xpEmbed)


	# returns the xp for a user
	@commands.command()
	async def xp(self, ctx, *members : discord.Member):

		member = ctx.author

		# if the author has defined multiple people in their request, print info for all users
		if len(members) == 0:
			await self.print_xp_for_member(ctx, member)
		else:
			for member in members:
				await self.print_xp_for_member(ctx, member)


	# gives xp to a user
	@commands.command()
	async def givexp(self, ctx, amount: str, *members : discord.Member):
		# make sure the input is correct
		if len(members) == 0:
			await Notify.warn(ctx, "Please mention the user(s) you want to give XP to")
			return

		# typecheck
		try :
			amount = int(amount)
		except ValueError:
			await Notify.error(ctx, "The amount must be a number!")
			return

		for user in members:
			await ctx.channel.send(f"Give {amount} XP to {user}")


	@commands.command()
	async def test(self, ctx, *, member: discord.Member = None):

		member = member or ctx.author

		await ctx.send(member.name  + "says hello")

def setup(client):
	client.add_cog(XP(client))