import os
import random
from PIL import Image
from numpy import asarray

# Data containers.
dogs_numpydata = []
cats_numpydata = []
mixed_numpydata = []


# Function that specifically adds new object to a list, used in other functions.
def append_to_list(item_to_append, a_list: list):
    a_list.append(item_to_append)


# Convert image to certain template.
def convert_and_store_image(image_to_convert):
    image_to_convert = image_to_convert.convert("L")
    image_to_convert = image_to_convert.resize((400, 400))
    append_to_list(asarray(image_to_convert), dogs_numpydata)


# Create a select amount of dog images and add their k-value to dogs_numpydata list.
def make_dogs(amount_of_images_to_scan: int):
    for _ in range(amount_of_images_to_scan):
        img = Image.open("dogs/" + random.choice(os.listdir("dogs")))
        convert_and_store_image(img)


# Create a select amount of cat images and add their k-value to dogs_numpydata list.
def make_cats(amount_of_images_to_scan: int):
    for _ in range(amount_of_images_to_scan):
        img = Image.open("cats/" + random.choice(os.listdir("cats")))
        convert_and_store_image(img)


# Create a select amount of both dog and cat images and add their k-value to dogs_numpydata list.
def make_mix(amount_of_images_to_scan: int):
    for _ in range(amount_of_images_to_scan):
        img = Image.open("mix/" + random.choice(os.listdir("mix")))
        convert_and_store_image(img)


    # Function to print entire list of k-values.
def print_numpydata(list_to_print):
    for k in list_to_print:
        print(k[0, 0])

