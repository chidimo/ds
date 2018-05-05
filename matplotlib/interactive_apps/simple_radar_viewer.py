"""Viewer"""

import matplotlib.pyplot as plt
from scipy.io.netcdf import netcdf_file

ncf = netcdf_file('KTLX_20100510_22Z.nc')
data = ncf.variables['Reflectivity']
lats = ncf.variables['lat']
lons = ncf.variables['lon']

i = 0

cmap = plt.get_cmap('gist_ncar')
cmap.set_under('lightgrey')

fig, ax = plt.subplots(1, 1)
im = ax.imshow(data[1], origin='lower',
               extent=(lons[0], lons[-1], lats[0], lats[-1]),
               vmin=0.1, vmax=80, cmap='gist_ncar')

cb = fig.colorbar(im)
cb.set_label('Reflectivity (dBZ)')
ax.set_xlabel('Longitute')
ax.set_ylabel('Latitude')

plt.show()
