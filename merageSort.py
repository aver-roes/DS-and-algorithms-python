# Info:
# - Stable (A.K.A preserve spatial position).
"""The time complexity of MergeSort is O(n*Log n) in all the 3 cases 
(worst, average and best).
As the mergesort always divides the array into two halves 
and takes linear time to merge two halves.
"""

def merge_sort(arr, start, end):
	# Check if it has only one element(the base case)
	if end - start + 1 <= 1:
		return arr

	# Get the middle
	mid = (end + start) // 2

	# Divide the arr into two half(the recursive calls)

	# Sort the first half (start to the middle)
	merge_sort(arr, start, mid)

	# Sort the right half (from middle+1 till the end)
	merge_sort(arr, mid + 1, end)

	# Merge sorted halfs:  arr[start], arr[mid], arr[end]
	merge(arr, start, mid, end)

	return arr


# Merge in-place
def merge(arr, start, mid, end):
	# Create a copy of the sorted left & right halfs to temp arrays
	left = arr[start:mid + 1]
	right = arr[mid + 1: end + 1]

	i = 0 # index for the left
	j = 0 # index for the right
	k = start # index for the arr(parent arr)

	# Merge the two sorted halfs into the original array
	while i < len(left) and j < len(right):
		# Here it achieve stability
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1	
		k += 1


	# One of the halfs will have elements remaining
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1
