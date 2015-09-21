
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Linked_List(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def print_list(self):
		node = self.head

		while node is not None:
			print node.data
			node = node.next

	def find_node(self, data):
		current = self.head

		while current is not None:
			if current.data == data:
				return True
			current = current.next
		return False

	def add_node(self, data):
		new_node = Node(data)

		if self.head == None:
			self.head = new_node

		if self.tail != None:
			self.tail.next = new_node

		self.tail = new_node

	def remove_node(self, index):
		current = self.head
		i = 1

		while (current.next != None) and (i < index):
			current = current.next
			i += 1

		if index == 0:
			self.head = current.next
		else:
			current.next = current.next.next		



if __name__ == '__main__':
	ll = Linked_List()
	ll.add_node(9)
	ll.add_node(2)
	ll.add_node(93)
	ll.add_node(933)
	ll.print_list()
