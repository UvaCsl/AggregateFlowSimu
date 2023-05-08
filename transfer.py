import czifile
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import ndimage, misc

# Start layer
layer = 2

name = '5'

img = czifile.imread(name+'.czi')

img = np.squeeze(img)

labelimg = img[0,layer:,:,:]

resultlist = np.empty([0,2208,2752])
for i in range(labelimg.shape[0]):
    result = ndimage.uniform_filter(labelimg[i,:,:], size=44, mode='constant')
    print(np.max(result),np.min(result))
    resultlist = np.append(resultlist, np.expand_dims(result,axis=0), axis=0)
print(resultlist.shape)

# np.save(name+".npy", img[0,:,:,:])

np.savetxt("avinten.txt", resultlist.reshape(1,-1), fmt='%1.1f')

# Transfer to vtk for segmentation
filtered_image = sitk.GetImageFromArray(img[1,layer:,:,:])
sitk.WriteImage(filtered_image, name+".vtk")

plt.imshow(resultlist[0,:,:])
plt.colorbar()
plt.show()
