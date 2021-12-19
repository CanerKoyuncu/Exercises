def bubleSort(arr):

	arrayLength = len(arr)

	for minIndex in range(arrayLength):
		swapped = False

		print(arr)
		for i in range(arrayLength-minIndex-1):

			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				swapped = True



		if(swapped == False):
			break
