message = "!hello boomer"
splitMessage = message.split(" ")

commandWordWithPrefix = splitMessage[0]
len = len(splitMessage[0])

command = commandWordWithPrefix[1:]
print(command)

splitMessage.remove(commandWordWithPrefix)

print(splitMessage)