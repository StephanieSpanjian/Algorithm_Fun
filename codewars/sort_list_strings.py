from operator import itemgetter

list_ = 'a, ba, cat, wax, yellow, zephyr'
n = 1

def sort_it(list_1, n):
	"""Return a list given in string format sorted by the nth letter in the words.
	>>> sort_it('a, a, ba, a, cat, wax, a, yellow, zephyr', 1)
	'a, ba, cat, wax, yellow, zephyr'
	"""
    #your code here
	return ', '.join(sorted(list_1.split(', '), key=itemgetter(n - 1)))

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	sort_it(list_, n)