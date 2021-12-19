def insertionSort(arr):

	arrLength = len(arr)

	for index in range(1,arrLength):
		key = arr[index]
		j = index - 1

		while (j >= 0) and (key < arr[j]):

			arr[j+1] = arr[j]
			j -= 1

		arr[j+1] = key
		print(arr)