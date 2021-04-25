import sqlite3
from discord.ext import commands
import discord

connection = sqlite3.connect('servers.db')

cursor = connection.cursor()


def create_server_if_not_exists(serverId):

	cursor.execute(f"SELECT * from servers WHERE ServerId = :serverId", {
		"serverId": serverId
	})

	doesNotExist = cursor.fetchone() == None

	if (doesNotExist):
		cursor.execute("INSERT INTO servers VALUES (:serverId, 0)", {
			"serverId": serverId
		})


def get_server_info(serverId):

	create_server_if_not_exists(serverId)
	cursor.execute(f"SELECT * from servers WHERE ServerId = :serverId", {
		"serverId": serverId
	})

	return cursor.fetchone()


def set_group_id(serverId, groupId):

	create_server_if_not_exists(serverId)

	cursor.execute("""UPDATE servers
	SET ServerID = :serverId, RobloxGroupID = :groupId
	WHERE ServerID = :serverId""", {
		"serverId": serverId, 
		"groupId": groupId
	})

	connection.commit()

class ServerSettings(commands.Cog):

	def __init__(self, client):

		self.client = client

	@commands.command()
	async def updateGroupId(self, ctx, groupId : int):

		set_group_id(ctx.message.guild.id, groupId)
		serverId, newGroupId = get_server_info(ctx.message.guild.id)
		await ctx.send("GroupID has been updated to " + str(newGroupId))
	
	@commands.command()
	async def getGroupID(self, ctx):

		serverId, groupId = get_server_info(ctx.message.guild.id)
		await ctx.send(f"The group ID for this server, {serverId}, is {groupId}")
	
def setup(client):

	cursor.execute("""CREATE TABLE IF NOT EXISTS servers (
		ServerId integer PRIMARY KEY,
		RobloxGroupID integer DEFAULT 0
	)""")

	client.add_cog(ServerSettings(client))