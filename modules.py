
from numpy import asarray

list_of_numpydata = []


def convert_image(image_to_convert):
    image_to_convert = image_to_convert.convert("L")
    image_to_convert = image_to_convert.resize((400, 400))
    list_of_numpydata.append(asarray(image_to_convert))
    