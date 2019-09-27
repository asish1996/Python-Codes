import numpy as np

  
    

def alignChannels(red, green, blue):
    rgb = np.array([red,green,blue])
    rgb1 = np.swapaxes(rgb,0,1)
    rgb2 = np.swapaxes(rgb1,1,2)
    
    
    """Given 3 images corresponding to different channels of a color image,
    compute the best aligned result with minimum abberations

    Args:
      red, green, blue - each is a HxW matrix corresponding to an HxW image

    Returns:
      rgb_output - HxWx3 color image output, aligned as desired"""
      

    return rgb2
