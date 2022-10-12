def bucketSort(arr):
	# Assuming that the input is in finite range from (0 - 2)
	counts = [0, 0, 0]

	# Count the number of occurrences of every element
	for e in arr:
		counts[e] += 1

	# Fill each bucket in the original array
	i = 0
	for e in range(len(counts)):
		for j in range(counts[e]):
			arr[i] = e
			i += 1

	return arr
