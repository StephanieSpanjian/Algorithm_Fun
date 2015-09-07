def do_search(list1, target_value):
	min = 0
	max = len(list1) - 1
	while True:
		if max < min:
			return -1
		m = (min + max)//2
		if list1[m] < target_value:
			min = m + 1
		elif list1[m] > target_value:
			max = m - 1
		else:
			return m

def do_search(list1, target_value):
	min = 0
	max = len(list1) - 1
	while True:
		if max < min:
			return - 1
		m = (min + max)//2
		if list1[m] < target_value:
			min = min + 1
		elif list1[m] > target_value:
			max = m - 1
		else: 
			return m

def do_search(list1, target_value):
	min = 0 
	max = len(list1) - 1
	while True:
		if max < min:
			return - 1
		m = (min + max)//2
		if list1[m] < target_value:
			min = min + 1
		elif list1[m] > target_value:
			max = m - 1
		else:
			return m