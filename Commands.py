import CommandFunctions.Test1 as Test1

commands = [
	"Test1",
	"Test2"
]

async def runCommand(name, message, otherWords):
	if name == "Test1":
		await Test1.run(message, otherWords)
