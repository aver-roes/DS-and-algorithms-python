def bubbleSort(array):
	n = len(array)

	for i in range(n-1):
		for j in range(0,n-i-1):
			if array[j] > array[j+1]:
				(array[j], array[j+1]) = (array[j+1], array[j])
	return array


array = [50,40,30,20,10,1]
print(bubbleSort(array))
