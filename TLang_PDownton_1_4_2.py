# -*- coding: utf-8 -*-
'''
Tlang_PDownton_1_4_2: Read and show an image.
'''
import PIL.ImageDraw
import PIL
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # “as” lets us use standard abbreviations
import matplotlib.colors as pltc
'''Read the image data'''
# Get the directory of this python script
directory = os.getcwd()
new_directory = os.path.join(directory, 'modified')
try:
    os.mkdir(new_directory)
except OSError:
    pass # if the directory already exists, proceed  
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'pngimg_com.jpg')
# Read the image data into an array
img = plt.imread(filename)
image = PIL.Image.open(filename)
filename2, filetype = image.split('.')
if filetype != 'png':
    new_image_filename = os.path.join(new_directory, filename2 + '.png')
    image.save(new_image_filename)
    img = plt.imread(os.path.join(directory, filename2 + '.png'))
height = len(img)
width = len(img[0])
for r in range(height):
    for c in range(width):
        if sum(img[r][c])==765: # brightness R+G+B goes up to 3*255=765
            img[r][c]=(0,0,0,0)
# Create figure with 2 subplots
fig, axes = plt.subplots(1,1)
# Show the image data in the first subplot
axes.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()
