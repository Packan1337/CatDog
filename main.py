from PIL import Image
from modules import *


"""image object"""
img1 = Image.open('cat.jpg')
img2 = Image.open('cat.jpg')

convert_image(img1)
convert_image(img2)
# Skriv ut pixel-värde i pixel 0,0
for k in list_of_numpydata:
    print(k[0, 0])
