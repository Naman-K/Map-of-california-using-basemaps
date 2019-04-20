# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:55:40 2019

@author: NamanK
"""
#Required for basemap
import os
os.environ['PROJ_LIB'] = r'C:\Users\NamanK\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'

#Required modules
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#Make figure
plt.figure(figsize=(14,14))

#Initialize the basemap
m= Basemap(llcrnrlat=30,llcrnrlon=-126,urcrnrlat=45,urcrnrlon=-114,resolution='h')

#Using the service Imagery World of Arcgis server, verbose returns the running of the server values
m.arcgisimage(service='ESRI_Imagery_World_2D',verbose=True,xpixels=2500,alpha=.6)
#Alpha 0.6 represents 40% transparency
#Draw the coasts
m.drawcoastlines(linewidth=3,linestyle='solid')

m.drawstates(color='yellow',linestyle='solid',linewidth=3)

