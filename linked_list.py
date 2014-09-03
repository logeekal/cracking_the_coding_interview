class Node(object):
	def __init__(self, data):
		self.data = data

class LLNode(Node):
	def __init__(self, data):
		super(LLNode, self).__init__(data)
		self.next = None
		
class LinkedList(object):
	def __init__(self, data=None):
		self.first = LLNode(data)
		self.last = self.first
		self.size = 1

	def __add__(self, data):
		"""
		Add any element in the LinkedList
		Function call -> instance.add(data)
		"""
		if self.first.data is None:
			self.first.data = data 
			print "Node added Succesfully"
			return True
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
			print str(current.data) + ' --> ' ,
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
		
		if self.first.data is None: #This will be the case when there is no element in the LinkedList
			if self.__add__(data):
				return True
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
				print cur_child.data
				while cur_child.next.data == current.data:
					cur_child.next = cur_child.next.next
					dedup_cnt += 1
					self.size -= 1
					if cur_child.next is None:
						break
				else:
					cur_child = cur_child.next 
			print "%d duplicates removed for %d" % (dedup_cnt, current.data)
			current = current.next
	
	def move(self, from_index, to_index):
		"""
		Instance.move(from_index,to_index)        .
		Move an element from one location to the other
		It picks the element at from_index and puts it at 
		the location just before to_index.
		
		Time Complexity : O(N)
		"""
		current_main = self.first
		index = 0
		if from_index >= self.size or to_index >= self.size:
			raise IndexError("Both index should not be greater than 10")
		if from_index == 0:
			source_node == self.first
			self.first =  self.first.next
		else:
			cur_child =  current_main
			while cur_child.next is not None:
				if index == from_index - 1:
					source_node = cur_child.next
					cur_child.next = cur_child.next.next
					self.size = self.size - 1
					break
				else:
					cur_child = cur_child.next
					index += 1
			
		#Now Source node has been assigned. Now it need to be moved to to_index
		index  = 0
		cur_child =  current_main
		while cur_child is not None: #cur_child is used instead of cur_child.next so as to traverse to last element as well
			if index == to_index - 1:
				source_node.next = cur_child.next
				cur_child.next = source_node
				self.size += 1
				break
			else:
				cur_child =  cur_child.next
				index += 1
				
	def index_of(self, p_data):
		"""
		Finds the first occurence of the data provided.
		
		Time Complexity : O(N)
		"""
		current = self.first
		index = 0
		while current is not None:
			if current.data == p_data:
				return index
			else:
				current = current.next
				index += 1
		else:
			print "Not Found"
	def reverse(self):
		"""
		Reverses the LinkedList .. Uses extra buffer but with Time Complexity of O(N)
		
		If we do not use extra buffer, time complexity will be O(N**2)
		"""
		length =  self.size
		res = LinkedList()
		current = self.first
		while current is not None:
			res.insert(current.data,0)
			current = current.next
		return res
			
		