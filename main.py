from PIL import Image
from modules import *


"""image object"""
img1 = Image.open('cats/cat.0.jpg')
img2 = Image.open('cats/cat.1.jpg')

convert_image(img1)
convert_image(img2)

print_numpy_list(list_of_numpydata)
