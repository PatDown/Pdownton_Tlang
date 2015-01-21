# -*- coding: utf-8 -*-
'''
Tlang_PDownton_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'pngimg_com.jpg')
# Read the image data into an array
img = plt.imread(filename)
height = len(img)
width = len(img[0])
for r in range(height):
    for c in range(width):
        if sum(img[r][c])==765: # brightness R+G+B goes up to 3*255=765
            img[r][c][img[r][c]]=[255]
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 1)
# Show the image data in the first subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()
