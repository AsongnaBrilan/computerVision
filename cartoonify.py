### step 1 ### importing required modules ###

from string import whitespace
import cv2
from django.template import Origin  #for image processing
import numpy as np #to store images
import easygui #to open the filebox
import imageio #to read images stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import*
from PIL import ImageTk, Image

### step 2 ### building a file box to choose a particular file ###
### this opens a a box to choose a file 
### and help us store path as string

def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    # read image
    originalImage = cv2.imread (ImagePath) # reads image
    originalImage = cv2.cvColor(originalImage, cv2.COLOR_BGR2RGB)
    #confirming that image is choosen
    if originalImage is None:
        print("can not find any image. choose appropriate file")
        sys.exit()
    
    Resized1 = cv2.resize(originalImage, (960, 540))

    # converting an image to grayscale
    grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (960, 540))
    #plt.imshow(ReSized2, cmap = 'grey')

    #smoothing the gray scale image 
    #applying median blur to smoothen an image 
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    Resized3 = cv2.resize(smoothGrayScale, (960, 540))
    #plt.imshow(ReSized2, cmap = 'grey')

    #retriving the edges of an image to produce the cartoon effect
    #by using threshold technigue
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 225, cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY, 9, 9)

    Resized4 = cv2.resize(getEdge, (960, 540))
    #plt.imshow(ReSized2, cmap = 'grey')

    #preparing a mask image by applying 
    #bilateral filter to remove noise
    #and keep edge as required
    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    Resized5 = cv2.resize(colorImage, (960, 540))
    #plt.imshow(ReSized2, cmap = 'grey')

    #giving a cartoon effect
    #masking edged image with our "beautiful" image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    Resized6 = cv2.resize(cartoonImage, (960, 540))
    #plt.imshow(ReSized2, cmap = 'grey')

    #plotting all transitions together
    images = [Resized1, ReSized2, Resized3, Resized4, Resized5, Resized6]
    fig, axes = plt.subplots(3, 2, figsize = (8,8), subplot_kw = 
    {'xticks':[], 'yticks':[]}, gripspec_kw=dict(hspace=0.1, wspace=0.1))

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
        #save button code
        plt.show()

#making a save button

def save (Resized6, ImagePath):
    #saving image using imwrite()
    newName = "cartoonified_Image"

    path1 = os.path.dirname(ImagePath)
    extension = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(Resized6, cv2.COLOR_RGB2BGGR))
    I = "Image saved by name " + newName + "at"+ path, tk.messagebox.showinfo(
        title=None, message=I)




