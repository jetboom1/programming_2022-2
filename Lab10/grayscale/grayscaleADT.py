import copy

from PIL import Image


class GrayscaleImage:
    def __init__(self, numRows, numCols):
        self._theRows = numRows
        self._theCols = numCols
        self.theData = [[0] * numCols for row in range(numRows)]

    def height(self):
        return self._theRows

    def width(self):
        return self._theCols

    def clear(self, value):
        for r in range(self._theRows):
            for c in range(self._theCols):
                self.theData[r][c] = value

    def getitem(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert 0 <= row < self._theRows and 0 <= col < self._theCols, "Array subscripts out of range."
        return self.theData[row][col]

    def setitem(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert 0 <= row < self._theRows and 0 <= col < self._theCols, "Array subscripts out of range."
        self.theData[row][col] = value

    def lzw_compression(self)->str:
        """Compress the image using LZW compression and return the compressed textstring"""
        textdata = ''
        for rows in self.theData:
            textdata += ';'
            for col in rows:
                textdata += (str(col)) + ','
        return LZW.compress(textdata[1:])

    def lzw_decompression(self, compressed)-> bool:
        '''Decompress the image, compressed by LZW compression and replace the image with it'''
        decompressed = LZW.decompress(compressed)
        decompressed = decompressed.split(';')
        for row in range(len(decompressed)):
            decompressed[row] = decompressed[row].split(',')[:-1]
            for col in range(len(decompressed[row])):
                decompressed[row][col] = int(decompressed[row][col])
        self.theData = decompressed
        return True


def from_file(path):
    """Створення екземпляру класу на основі зображення збереженого у форматі png чи jpg."""
    with Image.open(path) as img:
        img = img.convert('L')
    width = img.width
    height = img.height
    data = list(img.getdata())
    image_array = GrayscaleImage(height, width)
    for i in range(height):
        for j in range(width):
            image_array.setitem((i, j), data[i * width + j])
    return image_array

if __name__ == '__main__':
    grayscale_image = from_file('img.png')
    compressed = grayscale_image.lzw_compression()
    grayscale_image.lzw_decompression(compressed)
    original_image = from_file('img.png')
    assert grayscale_image.theData == original_image.theData, "Оригінальне і декомпресоване зображення не співпадають"
    assert grayscale_image.height() == original_image.height(), "Не співпадають зображення після декомпресії і після компресії"
    assert grayscale_image.width() == original_image.width(), "Не співпадають зображення після декомпресії і після компресії"
    assert grayscale_image.getitem((42,234)) == original_image.getitem((42,234)), "Оригінальне і декомпресоване зображення не співпадають"

    image_to_be_cleared = copy.deepcopy(original_image)
    image_to_be_cleared.clear(0)

    assert image_to_be_cleared.theData == GrayscaleImage(original_image.height(), original_image.width()).theData, \
        "Не відбувається очищення зображення"
