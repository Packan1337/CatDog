import os
import random

import numpy as np
from PIL import Image
from numpy import asarray
from knn import KNN, euclidean_distance

# Data containers.
dogs_numpydata = []
cats_numpydata = []
mix_numpydata = []


# Function that specifically adds new object to a list, used in other functions.
def append_to_list(item_to_append, a_list: list):
    a_list.append(item_to_append)


# Convert image to certain template.
def convert_and_store_image(image_to_convert, animal):
    image_to_convert = image_to_convert.convert("L")
    image_to_convert = image_to_convert.resize((400, 400))
    if animal == "dog":
        append_to_list(asarray(image_to_convert), dogs_numpydata)
    elif animal == "cat":
        append_to_list(asarray(image_to_convert), cats_numpydata)
    elif animal == "mix":
        append_to_list(asarray(image_to_convert), mix_numpydata)


# Create a select amount of dog images and add their k-value to dogs_numpydata list.
def make_dogs(amount_of_images_to_scan: int):
    for _ in range(amount_of_images_to_scan):
        dog_img = Image.open("dogs/" + random.choice(os.listdir("dogs")))
        convert_and_store_image(dog_img, "dog")


# Create a select amount of cat images and add their k-value to dogs_numpydata list.
def make_cats(amount_of_images_to_scan: int):
    for _ in range(amount_of_images_to_scan):
        cat_img = Image.open("cats/" + random.choice(os.listdir("cats")))
        convert_and_store_image(cat_img, "cat")


# Create a select amount of both dog and cat images and add their k-value to dogs_numpydata list.
def make_mix(amount_of_images_to_scan: int):
    for _ in range(amount_of_images_to_scan):
        mix_img = Image.open("mix/" + random.choice(os.listdir("mix")))
        convert_and_store_image(mix_img, "mix")


# Function to print entire list of k-values.
def print_numpydata(list_to_print):
    for k in list_to_print:
        print(f"{k[0, 0]} ", end="")

# TODO fix mix_numpydata value.
def get_accuracy():
    clf = KNN(k=3)
    clf.fit(dogs_numpydata, cats_numpydata)
    predictions = clf.predict(mix_numpydata)

    acc = np.sum(predictions == mix_numpydata / len(mix_numpydata))
    print(acc)