import Basemap
import numpy as np
import matplotlib.pyplot as plt
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
f = plt.figure(figsize=(8,4))
m = Basemap(projection='robin',lon_0=0,resolution='c')
m.shadedrelief(scale=0.2)
plt.title("Robinson Projection")
plt.show()