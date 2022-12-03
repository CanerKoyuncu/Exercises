from PIL import Image

import bubleSort
import insertionSort
import selectionSort

new_image = Image.new(mode="RGB", size=((picSize + 1), (picSize + 1)))
new_image.putdata(pictureResult)
new_image.save("new.jpg")

if __name__ == '__main__':
    # turnRight90Degree("cat.jpg","hello")
    # funnyFunc("cat.jpg")
    A = [64, 25, 12, 22,11]
    # selectionSort.selectionSort(A)
    # bubleSort.bubleSort(A)
    insertionSort.insertionSort(A)


