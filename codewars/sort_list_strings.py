list_ = "bill, bell, ball, bull"
n = 2

def sort_it(list_, n):
	"""Return a list given in string format sorted by the nth letter in the words.
	>>> sort_it("bill, bell, ball, bull", 2)
	'ball, bell, bill, bull'
	"""
    #your code here
	list_1 = list_.split(", ")

	list_2_spliced = []
	for item in list_1:
		list_2_spliced.append(item[(n-1):])
	list_2_sorted = sorted(list_2_spliced)

	list_3_sorted = []
	for item_2 in list_2_sorted:
		for item_1 in list_1:
			if item_1[(n-1):] in item_2:
				list_3_sorted.append(item_1)

	list_3_joined = ", ".join(list_3_sorted)
	return list_3_joined

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	sort_it(list_, n)