import CommandFunctions.Test1 as Test1
import CommandFunctions.XP as XP

commands = [
	"Test1",
	"Test2"
]

# determine which command module should be run
async def run_command(command, message, other_words):	
	command = command.lower() # use a lowercase string for comparing

	if command == "test1":
		await Test1.run(message, other_words)

	if command == "givexp":
		await XP.give_xp(message, other_words)

	if command == "xp":
		await XP.print_xp(message, other_words)
