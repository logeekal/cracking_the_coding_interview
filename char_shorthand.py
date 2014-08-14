def compress_string(string):
	"""
	This is Question 1.5 of Cracking the code interview and its main job is to
	compress the string to a shorthand notation. For example : aaaabb -> a4b2
	
	Time Complexity -->	O(N)
	
	"""
	length =  len(string)
	result = ''
	for count in range(length):
		index = count
		chr_count= 1
		while string[index] == string[index + 1]:
			chr_count += 1
			index += 1
		result 	= result + string[count]
		if chr_count != 0:
			result =  result + str(count)
			if index == length - 2:
				break
		else:
			if index == length - 2:
				result = result + string [index + 1]
				break
	return result