"""
File: prove08.py
Prove: 08
Topic: Image Pixel 
Author: Glory Ozonuwe

Purpose: Use this idea of looping, or iterating, through each pixel in an image to produce a green screen effect.
"""

# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable 
image_beach = Image.open("beach.jpg")
image_cactus = Image.open("cactus.jpg")
image_cat = Image.open("cat_small.jpg")

# Iterate through the pixels
pixels_beach = image_beach.load()
pixels_cactus = image_cactus.load()
pixels_cat = image_cat.load()
#print(pixels_beach[200, 300])

# Changes green screen
for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_cactus[x, y]
        (rd, grn, bl) = pixels_cat[x, y]

        if grn <= 210:
            pixels_cactus[x, y] = pixels_cat[x, y]
        if g >= 210 and r < 200 and b < 200 and grn >= 211:
            pixels_cactus[x, y] = pixels_beach[x, y]


# This line attempts to open a new window to display the image.
image_cactus.show()

# Save the new updated image
image_cactus.save("image_new.jpg")