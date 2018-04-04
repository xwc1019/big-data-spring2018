from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
import os
import jsonpickle
import pandas as pd
%matplotlib inline

os.chdir('week-05')

DATA = '/Users/xwc1019/Desktop/github/ws04_materials'


red_path = os.path.join(DATA,'b4.tif')
nir_path = os.path.join(DATA,'b5.tif')

red_data = gdal.Open(red_path)


red_band = red_data.GetRasterBand(1)
red = red_band.ReadAsArray()
print(red)

nir_data = gdal.Open(nir_path)
nir_band = nir_data.GetRasterBand(1)
nir = nir_band.ReadAsArray()
print(nir)

type(nir)

plt.imshow(nir)
plt.colorbar()

def ndvi_calc(red,nir):
    """calculate NDVI"""
    return(nir - red)/(nir + red)

plt.imshow(ndvi_calc(red,nir),cmap="YlGn")
plt.colorbar()

red.dtype
nir.dtype

red = red.astype(np.float32)
nir = nir.astype(np.float32)

plt.imshow(ndvi_calc(red,nir),cmap="YlGn")
plt.colorbar()

ndvi = ndvi_calc(red,nir)

print(ndvi)



tirs_path = os.path.join(DATA,'b10.TIF')

tirs_data = gdal.Open(tirs_path)
tirs_band = tirs_data.GetRasterBand(1)
tirs = tirs_band.ReadAsArray()
tirs = tirs.astype(np.float32)

meta_file = '/Users/xwc1019/Desktop/github/ws04_materials/MTL.txt'

with open(meta_file) as f:
    meta = f.readlines()

matchers = ['RADIANCE_MULT_BAND_10', 'RADIANCE_ADD_BAND_10', 'K1_CONSTANT_BAND_10', 'K2_CONSTANT_BAND_10']
[s for s in meta if any(xs in s for xs in matchers)]

def process_string (st):
    return float(st.split(' = ')[1].strip('\n'))

matching = [process_string(s) for s in meta if any(xs in s for xs in matchers)]
matching

rad_mult_b10, rad_add_b10, k1_b10, k2_b10 = matching

rad = rad_mult_b10 * tirs + rad_add_b10
plt.imshow(rad, cmap='RdYlGn')
plt.colorbar()

bt = k2_b10 / np.log((k1_b10/rad) + 1) - 273.15
plt.imshow(bt, cmap='RdYlGn')
plt.colorbar()
