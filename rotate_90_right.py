def rotate_90_right(dummy):
	"""This program rotates Matrix to 90 degrees right
		This is a solution to 1.6 Cracking the Coding Interview"""
	C = len(dummy[0])
	R =  len(dummy)
	#print R, C
	#Creating a 0 matrix
	result = []
	for row in range(C):
		row_list = []
		for column in range(R):
			row_list.append(0)
		result.append(row_list)
	for i in range(R - 1, -1, -1):
		for j in range(C):
			#print i, j
			#print R - 1 - i,j ,dummy[R - 1 - i][j]
			result[j][i] = dummy[R - 1 - i][j]
			print result
	return result