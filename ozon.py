#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import netcdf_file
import json


with netcdf_file('MSR-2.nc', mmap = False) as netcdf_file:
    variables = netcdf_file.variables

#Antofagasta city    
x = -23.6523600
y = -70.3954000
lat_i = variables['latitude'].data.searchsorted(x)
long_i = variables['longitude'].data.searchsorted(y)

whole_time = variables['time'][:]
whole_O3 = variables['Average_O3_column'][:, lat_i, long_i]

jan_time = variables['time'][::12]
jan_O3 = variables['Average_O3_column'][::12, lat_i, long_i]

jul_time = variables['time'][6::12]
jul_O3 = variables['Average_O3_column'][6::12, lat_i, long_i]

plt.plot(whole_time, whole_O3, label = 'whole time')
plt.plot(jan_time, jan_O3, label = 'all januaries')
plt.plot(jul_time, jul_O3, label = 'all julies')
plt.title('Ozon level in Antofagasta')
plt.xlabel('months (since 1970-01-15)')
plt.ylabel('DU')
plt.legend()
plt.grid()
plt.savefig('ozon.png')

d = {
    "city": "Antofagasta",
    "coordinates": [-23.6523600, -70.3954000],
    "jan": {
        "min": float(np.min(jan_O3)),
        "max": float(np.max(jan_O3)),
        "mean": float(np.mean(jan_O3))
    },
    "jul": {
        "min": float(np.min(jul_O3)),
        "max": float(np.max(jul_O3)),
        "mean": float(np.mean(jul_O3))
    },
    "all": {
        "min": float(np.min(whole_O3)),
        "max": float(np.max(whole_O3)),
        "mean": float(np.mean(whole_O3))
    }
}

with open('ozon.json', 'w') as f:
    json.dump(d, f)
