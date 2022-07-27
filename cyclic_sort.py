def cyclicSort(arr: list[int]) -> None:

	# the starting point
	i = 0

	while (i < len(arr)):
		correctIdx = arr[i] - 1

		# IF arr[i] is NOT in the correct position
		if arr[i] != arr[correctIdx]:
			swap(arr, i, correctIdx)
		else:
			# means arr[i] in the correct index move i
			i += 1



def swap(array, i, j):
  array[i], array[j] = array[j], array[i]

 

arr = [3,1,5,2,4]

cyclicSort(arr)
print(arr)
