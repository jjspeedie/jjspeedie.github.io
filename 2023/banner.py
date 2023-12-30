import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib as mpl
import cmasher as cmr

im = fits.getdata('f3d2c_dust0_orbit2000_EOSadi_EPSTEIN_2D_CPD0_intens_rt.fits')

im_t = np.tile(im, 2)

disk = np.tile(np.mean(im_t, axis=1), (im_t.shape[1], 1) ).transpose()

fig = plt.figure(figsize=(12, 8))

norm = mpl.colors.PowerNorm(gamma=0.5)

print(np.min(im_t-disk), np.max(im_t-disk))

# plt.imshow(im_t-disk, cmap='RdGy', origin='lower', vmin=-0.28, vmax=0.28)
cmap = cmr.get_sub_cmap('cmr.ocean_r', 0., 1.0)
plt.imshow(im_t, cmap=cmap, origin='lower')

# cmap = cmr.get_sub_cmap('cmr.ember_r', 0., .5)
# print(np.min(1/disk), np.max(1/disk))
# plt.imshow(1/disk, cmap=cmap, origin='lower', vmin=0.5, vmax=20, alpha=0.1)


plt.imshow(im_t-disk, cmap='Greys', origin='lower', vmin=0, vmax=0.12, alpha=0.7)


plt.axis('off')
plt.tight_layout()
plt.savefig('ban.png', dpi=700)
