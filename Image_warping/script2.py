import imageio
import matplotlib.pyplot as plt
import numpy as np
#import warpA_check
#import warpA

def warp(im, A, output_shape):
    num_rows = im.shape[0]
    num_cols = im.shape[1]
    im_morphed = np.zeros((num_rows,num_cols))
    x = np.array(list(range(0,num_cols)))
    y = np.array(list(range(0,num_rows)))
    #p_source = []
    for i in range(num_rows-1):
        for j in range(num_cols-1):
            p_source = np.array([x[j],y[i],1])
            cords_result = A@p_source.reshape(3,1)
            x_morph = int(round(cords_result[0][0]))
            y_morph = int(round(cords_result[1][0]))
            #print x_morph
            if x_morph<num_cols-1 and x_morph>0:
                if y_morph<num_rows-1 and y_morph>0:
                    im_morphed[x_morph][y_morph] = im[j][i]

    return im_morphed

# Read the image
im = imageio.imread('../data/mug.jpg')
im = im / 255.0  # convert to float

# convert to grayscale
im_gray = np.dot(im, [0.299, 0.587, 0.114])
print (im_gray.shape[1])

# create figure
f, axes = plt.subplots(2, 2)
f.set_size_inches(8, 8)
axes[0, 0].imshow(im)
axes[0, 0].set_title('original')
axes[0, 1].imshow(im_gray, cmap=plt.get_cmap('gray'))
axes[0, 1].set_title('grayscale')
axes[1, 1].remove()


# define some helper functions
# to create affine transformations
def scalef(s):
    return np.diag([s, s, 1])


def transf(tx, ty):
    A = np.eye(3)
    A[0, 2] = ty
    A[1, 2] = tx
    return A


def rotf(t):
    return np.array([[np.cos(t), np.sin(t), 0],
                     [-np.sin(t), np.cos(t), 0],
                     [0, 0, 1]])


output_shape = im_gray.shape
cx = im_gray.shape[1] // 2
cy = im_gray.shape[0] // 2

A = (transf(output_shape[1]//2, output_shape[0]//2,)
     .dot(scalef(0.8))
     .dot(rotf(- 30 * np.pi / 180))
     .dot(transf(-cx, -cy)))


# plot a dot at the rotation center
axes[0, 1].plot(cx, cy, 'r+')
#warped_im = warpA_check.warp(im_gray, A, output_shape)
warped_im = warp(im_gray,A,output_shape)
axes[1, 0].imshow(warped_im, cmap=plt.get_cmap('gray'))
axes[1, 0].set_title('warped')

# write the plot to an image
plt.savefig('results/transformed_soln.jpg')
plt.show()
