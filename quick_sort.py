# - In-Place sorting unlike Merage Sort
# - Not Stable (A.K.A Do not preserve spatial position).
""" On average is O(n log n) like Merge sort,
BUT if the array is already sorted OR if the pivot
is the smallest or greatest item it will be
O(n^2) the reason for that is it will lead to one branch tree(level = n)
"""


arr = [1,2,4,3,9,1,3]

def quick_sort(arr, start, end):

	# The base case
	if end - start + 1 <= 1:
		return arr

	pivot = arr[end]

	# A pointer where to move the element less than the pivot
	left = start 

	# Partition: elements smaller than pivot on left side
	for i in range(start, end):
		if arr[i] < pivot:
			arr[i], arr[left] = arr[left], arr[i]
			left += 1

	# Move pivot in-between left & right sides
	arr[end] = arr[left]
	arr[left] = pivot

	# Quick sort left side
	quick_sort(arr, start, left - 1)

	# Quick sort right side
	quick_sort(arr, left + 1, end)

	return arr


quick_sort(arr, 0, len(arr) - 1)
print(arr)
