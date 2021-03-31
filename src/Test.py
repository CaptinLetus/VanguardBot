current_xp = 80
needed_xp = 100
amount_of_bars = 5

percentage_to_next_level = (current_xp/needed_xp)

print(percentage_to_next_level/5)

print(percentage_to_next_level)

str = ""
for i in range(amount_of_bars):
	if i/amount_of_bars < percentage_to_next_level:
		str += "🟩"
	else:
		str += "⬜"

print(str)