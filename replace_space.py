def replace_space(string):
	""" Question 1.4 for Cracking the Coding Interview
		This code replaces the space of the string to %20"""
	import time
	start_time = time.time()
	result  = '%20'.join(string.split(' '))
	end_time =  time.time()
	print "Time Taken : " + str(end_time - start_time)
	return result
	

	
def replace_space_costly(string):
	"""This is just another method to replace spaces without
		using advanced python functions """
	start_time = time.time()
	result = ''
	for letter in string:
		if letter == ' ':
			result = result + '%20'
		else:
			result = result + letter
	print "End Time : " + str(time.time())
	end_time =  time.time()
	print "Time Taken : " + str(end_time - start_time)
	return result