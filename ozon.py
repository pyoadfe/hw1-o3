#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('longitude', metavar='LON', type=float, help='Longitude, deg')
parser.add_argument('latitude',  metavar='LAT', type=float, help='Latitude, deg')

if __name__ == "__main__":
    args = parser.parse_args()
    print(args.longitude, args.latitude)
import json
from scipy.io import netcdf
import matplotlib.pyplot as plt
import numpy as np
with netcdf.netcdf_file("MSR-2.nc", mmap=False) as netcdf_file:
    for v in netcdf_file.variables:
        var = netcdf_file.variables[v]
    for v in netcdf_file.variables:
        index_lon = np.searchsorted(netcdf_file.variables['longitude'].data, args.longitude)
        index_lat = np.searchsorted(netcdf_file.variables['latitude'].data, args.latitude)
        z = (netcdf_file.variables['Average_O3_column'].data[:, index_lat, index_lon])
    print('min',np.min(z))
    print('max',np.max(z))
    print('avg',np.sum(z)/468)
    for v in netcdf_file.variables:
        n=39
        sum_jan=np.sum(netcdf_file.variables['Average_O3_column'].data[np.arange(0, 468, 12), index_lat, index_lon])
        max_jan=np.max(netcdf_file.variables['Average_O3_column'].data[np.arange(0, 468, 12), index_lat, index_lon])
        min_jan=np.min(netcdf_file.variables['Average_O3_column'].data[np.arange(0, 468, 12), index_lat, index_lon])
    print("min",min_jan)
    print("max",max_jan)
    print('avg',sum_jan/n)
    for v in netcdf_file.variables:
        sum_jul=np.sum(netcdf_file.variables['Average_O3_column'].data[np.arange(6, 468, 12), index_lat, index_lon])
        max_jul=np.max(netcdf_file.variables['Average_O3_column'].data[np.arange(6, 468, 12), index_lat, index_lon])
        min_jul=np.min(netcdf_file.variables['Average_O3_column'].data[np.arange(6, 468, 12), index_lat, index_lon])
    print("min",min_jul)
    print("max",max_jul)
    print('avg',(sum_jul/n))
    fig = plt.gcf()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.set_xlabel('ВРЕМЯ (месяцы)')
    axes.set_ylabel('Единицы Добсона')
    plt.grid()
    fig.set_size_inches(15,10)
    plt.plot(netcdf_file.variables['time'].data, z)
    plt.plot(np.arange(0,468, 12), netcdf_file.variables['Average_O3_column'].data[np.arange(0, 468, 12), index_lat, index_lon])
    plt.plot(np.arange(0,468, 12), netcdf_file.variables['Average_O3_column'].data[np.arange(6, 468, 12), index_lat, index_lon])
    plt.savefig('ozon.png')
coordinates = {'coordinates':[args.lontitude,args.lantitude],
              file = { 'coordinates': [lon, lat],
            'jan': {'min': float('{:.1f}'.format(min_jan)),
                    'max': float('{:.1f}'.format(max_jul)),
                    'mean': float('{:.1f}'.format(sum_jan/39))},
            'jul': {'min': float('{:.1f}'.format(min_jul)),
                    'max': float('{:.1f}'.format(max_jul)),
                    'mean': float('{:.1f}'.format(sum_jul/39))},
            'all': {'min': float('{:.1f}'.format(min(z))),
                    'max': float('{:.1f}'.format(max(z))),
                    'mean': float('{:.1f}'.format(np.mean(z)))}}
with open('ozon.json', 'w') as f:
json.dump(coordinates, f)
