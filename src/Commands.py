import CommandFunctions.Test1 as Test1

commands = [
	"Test1",
	"Test2"
]

# determine which command module should be run
async def run_command(name, message, other_words):
	name = name.lower() # use a lowercase string for comparing

	if name == "test1":
		await Test1.run(message, other_words)
