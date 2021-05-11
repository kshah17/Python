def three(input): 
    return input.lower() in [A, E, I, O, U]

def vowels(str):
	count = 0
	for i in range(len(str)):
		if three(str[i]):
			count += 1
		return count
