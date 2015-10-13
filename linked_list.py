
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
				return data
			current = current.next
		return False

	def add_node(self, data):
		new_node = Node(data)
		node = self.first_node

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

	def check_linked_list_cycle(self, first_node):
		# """Returns True if the linked list is a circular linked list, else
		# it returns False. 
		# >>> check_linked_list_cycle(first_node)
		# False
		# """
		ll = Linked_List()
		# first_node = ll.first_node()
		node = self.first_node
		slow_runner = first_node
		fast_runner = first_node

		while fast_runner != None and fast_runner.next != None:
			slow_runner = slow_runner.next
			fast_runner = fast_runner.next.next

			if fast_runner == slow_runner:
				return True
		return False	


if __name__ == '__main__':
	ll = Linked_List()
	ll.add_node(9)
	ll.add_node(2)
	ll.add_node(93)
	ll.add_node(933)
	ll.print_list()
	ll.check_linked_list_cycle()
