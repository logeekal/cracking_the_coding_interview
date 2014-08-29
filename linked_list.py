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
		self.size = 1

	def __add__(self, data):
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
		self.size += 1
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
		return self.size

	def __getitem__(self,index):
		"""
		Create a built-in so that list element can be get by
		instance[index]
		"""
		if index > self.length() -1:
			raise IndexError('Index out of range : Invalid Value for index provided')
		else:
			count = 0
			current = self.first
			while current.next is not None:
				if count == index:
					return current.data
				current = current.next
				count += 1
			else:
				return current.data

	def insert(self, data, index=-1):
		"""
		Insert data at any position.
		Format instance.insert(data[, index]).
		Index is optional and if provided value is -1 data will be inserted at the end
		"""
		#Type Check
		if type(index) != int or index < -1:
			raise TypeError('Index should be an integer and greater than or equal to -1')
		new_node =  LLNode(data)

		if index == 0:
			new_node.next = self.first
			self.first = new_node
			return True
		elif index == -1:
			self.__add__(data)
			return True

		current = self.first
		count = 0
		while current.next is not None:
			if count == index - 1:
				new_node.next =  current.next
				current.next = new_node
				print "Node inserted at position %d " % count
			current = current.next
			count += 1
	def dedup(self):
		"""
		Deduplicates an unsorted LinkedList
		"""
		current = self.first
		while current.next is not None:
			cur_child = current
			dedup_cnt = 0
			while cur_child.next is not None:
				while cur_child.next.data == current.data:
					cur_child.next = cur_child.next.next
					dedup_cnt += 1
					self.size -= 1
				else:
					cur_child = cur_child.next 
			print "%d duplicates removed for %d" % (dedup_cnt, current.data)
			current = current.next