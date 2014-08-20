class Node(object):
	def __init__(self, data):
		self.data = data

class LLNode(Node):
	def __init__(self, data):
		super(LLNode, self).__init__(data)
		self.next = None
		
class LinkedList(object):
	def __init__(self, data):
		self.first = LLNode(data)
		self.last = self.first
		
	def add(self, data):
		"""
		Add any element in the LinkedList
		Function call -> instance.add(data)		
		"""
		new_node = LLNode(data)
		current = self.first
		while current.next is not None:
			current = current.next
		current.next = new_node
		self.last = new_node
		self.last.next = None
		print "Node added Succesfully"
		
	def __call__(self):
		"""
		Prints the LinkedList
		Function call -> instance()		
		"""
		current = self.first
		while current.next is not None:
			print current.data
			current = current.next
		else:
			print current.data
	
	def length(self):
		count = 1
		current = self.first
		while current.next is not None:
			current = current.next
			count += 1
		return count
	
	def __getitem__(self,index):
		"""
		Create a built-in so that list element can be get by
		instance[index]
		"""
		if index > self.length() -1:
			raise IndexError
		else:
			count = 0
			current = self.first
			while current.next is not None:
				if count == index:
					return current.data
				current = current.next
			else:
				return current.data
			
	def insert(self, data, index)