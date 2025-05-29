import netCDF4 as nc
import numpy as np

fn = "/home/voland/Documents/NetCdf4/daymet_v4_vp_monavg_na_2023.nc"
ds = nc.Dataset(fn)

print(ds)
