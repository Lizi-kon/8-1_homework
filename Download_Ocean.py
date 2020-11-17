import pathlib
import shutil
import os
import requests

path = str(pathlib.Path().absolute()) + '\\Taghiyev_Sea'
print(path)


try:
    shutil.rmtree(path)
except OSError:
    print("Deletion of directory %s failed" % path)
else:
    print("Succerfuly deleted the directory %s" % path)
try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)



    #https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/year/monthday/AQUA_MODIS.yearmonthday.L3m.DAY.SST.sst.KM.NRT.nc.png

km = ['4km','9km']
year = '2020'
month = '09'

for key in km:

    photoPath = path + '\\' + key
   
    try:
          os.mkdir(photoPath)
    except OSError:
          print("Creation of the directory %s failed" % photoPath)
    else:
          print("Successfully created the directory %s" % photoPath)

for day in range(2,18):
    name = str(day) + '.png'
    r = requests.get('https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/' + year + "/" + month + str(day) + '/AQUA_MODIS.'+ year + month + str(day) +'.L3m.DAY.SST.sst.'+ km[0] +'.NRT.nc.png')
    open(path +'\\'+ km[0] + '/' + name, 'wb').write(r.content)
    
    r1 = requests.get('https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/' + year + "/" + month + str(day) + '/AQUA_MODIS.'+ year + month + str(day) +'.L3m.DAY.SST.sst.'+ km[1] +'.NRT.nc.png')
    open(path +'\\'+ km[1] + '/' + name, 'wb').write(r1.content)