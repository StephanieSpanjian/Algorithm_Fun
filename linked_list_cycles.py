# Interview cake

from linked_list import Linked_List
def check_linked_list_cycle(first_node):
	# """Returns True if the linked list is a circular linked list, else
	# it returns False. 
	# >>> check_linked_list_cycle(first_node)
	# False
	# """
	ll = Linked_List()
	first_node = ll.first_node()
	slow_runner = first_node
	fast_runner = first_node

	while fast_runner != None and fast_runner.next != None:
		slow_runner = slow_runner.next
		fast_runner = fast_runner.next.next

		if fast_runner == slow_runner:
			return True
	return False

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    check_linked_list_cycle(9)