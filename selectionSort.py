
def selectionSort(array):

	arrayLength = len(array)

	for minIndex in range(arrayLength):
		selectedIndex = minIndex

		for index in range(minIndex+1,arrayLength):

			if array[selectedIndex] > array[index]:

				selectedIndex = index

		if array[selectedIndex] < array[minIndex]:
			array[selectedIndex], array[minIndex] = array[minIndex], array[selectedIndex]

		elif array[selectedIndex] == array[minIndex]:
			break

		print(array)




