from alignChannels import alignChannels
import numpy as np
from PIL import Image
# Problem 1: Image Alignment

# 1. Load images (all 3 channels)
red = np.load('red.npy')
green = np.load('green.npy')
blue = np.load('blue.npy')

def ncc(array1,array2):         #NCC based alignment
    flat_arr1 = array1.flatten()
    flat_arr2 = array2.flatten()
    norm_arr1 = np.linalg.norm(flat_arr1)
    norm_arr2 = np.linalg.norm(flat_arr2)
    prod_array = flat_arr1 * flat_arr2
    sum_prod_array = sum(prod_array)
    NCC = sum_prod_array/(norm_arr1*norm_arr2)
    return NCC  

ncc_blue_red_col = []
ncc_blue_green_col = []
ncc_blue_red_row = []
ncc_blue_green_row = []
red_updated = []
green_updated = []
red_col = []
red_row  = []
green_col = []
green_row = []

for i in range(0,61):
    ncc_val_red = ncc(np.roll(red,i-30,axis=1),blue)
    ncc_val_green = ncc(np.roll(green,i-30,axis=1),blue)
    ncc_blue_red_col.append(ncc_val_red)
    ncc_blue_green_col.append(ncc_val_green)

red_col = np.roll(red,np.argmax(ncc_blue_red_col)-30,axis=1)
green_col = np.roll(green,np.argmax(ncc_blue_green_col)-30,axis=1)    


for i in range(0,61):
    ncc_val_red = ncc(np.roll(red,i-30,axis=0),blue)
    ncc_val_green = ncc(np.roll(green,i-30,axis=0),blue)
    ncc_blue_red_row.append(ncc_val_red)
    ncc_blue_green_row.append(ncc_val_green)    

red_row = np.roll(red,np.argmax(ncc_blue_red_row)-30,axis=0)
green_row = np.roll(green,np.argmax(ncc_blue_green_row)-30,axis=0)

red_updated = red_row
green_updated = green_row


if max(ncc_blue_red_col)>max(ncc_blue_red_row):
    red_updated = red_col

if max(ncc_blue_green_col)>max(ncc_blue_green_row):
    green_updated = green_col

# 2. Find best alignment
rgbResult = alignChannels(blue,red_updated,green_updated)

# 3. save result to rgb_output.jpg (IN THE "results" FOLDER)
img = Image.fromarray(rgbResult)
img.save('hello.jpg')


