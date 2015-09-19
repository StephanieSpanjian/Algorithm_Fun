def bubbleSort(alist):
	for passnum in range(len(alist)-1, 0, -1):
			for i in range(passnum):
				if alist[i] > alist[i+1]:
					temp = alist[i]
					alist[i] = alist[i+1]
					alist[i+1] = temp

a list = [54, 26, 93, 27, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

def bubble_sort(list1):
	for passnum in range(len(list1)-1, 0, -1:
		for i in range(passnum):
			if list1[i] > list1[i+1]:
				temp = list1[i]
				list1[i] = list1[i+1]
				list1[i+1] = temp