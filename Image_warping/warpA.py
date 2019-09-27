import numpy as np

def warp(im, A, output_shape):
    num_rows = im.shape[0]
    num_cols = im.shape[1]
    im_morphed = np.zeros((num_rows,num_cols))
    x = np.array(list(range(0,num_cols)))
    y = np.array(list(range(0,num_rows)))
    #p_source = []
    for i in range(num_rows):
        for j in range(num_cols):
            p_source = np.array([x[j],y[i],1])
            cords_result = A@p_source.reshape(3,1)
            x_morph = int(round(cords_result[0][0]))
            y_morph = int(round(cords_result[1][0]))
            #print x_morph
            if x_morph<num_cols and x_morph>-1:
                if y_morph<num_rows and y_morph>-1:
                    im_morphed[x_morph][y_morph] = im[j][i]
                    
            
            #im_morphed[round(cords_result[0])][round(cords_result[1])] = im[i][j]
    
    
            
    
    
    """ Warps (h,w) image im using affine (3,3) matrix A
    producing (output_shape[0], output_shape[1]) output image
    with warped = A*input, where warped spans 1...output_size.
    Uses nearest neighbor interpolation."""

    return im_morphed
