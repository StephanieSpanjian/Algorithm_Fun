from linked_list import linked_list
def check_linked_list_cycle(first_node):
	"""Returns True if the linked list is a circular linked list, else
	it returns False. 
	>>>check_linked_list_cycle(5)
	True
	"""
	slow_runner = first_node
	fast_runner = first_node

	while fast_runner != None and fast_runner.next != None:
		slow_runner = slow_runner.next
		fast_runner = fast_runner.next.next

		if fast_runner == slow_runner:
			return True
	return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()