#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:43:25 2022

Functions to produce movies of the particles

@author: steve
"""

import matplotlib.pyplot as plt
import matplotlib.animation as manimation

# Can this be changed to show a .png of the active particle with its orientation (and size) indicated?

def movie_maker(active1,passive1,Xmin1,Xmax1,Ymin1,Ymax1):

    # Define the meta data for the movie
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='Movie Test', artist='Matplotlib',
                    comment='a red circle following a blue sine wave')
    writer = FFMpegWriter(fps=15, metadata=metadata)
    
    # Initialize the movie
    fig = plt.figure()
    
    with writer.saving(fig, "movies/writer_test.mp4", 100):
        for i in range(int(len(active1[0,0,:])/10)):
            plt.cla()
            # Need to find a consistent way to do s= to give 10um particles?
            plt.scatter(active1[:,0,i],active1[:,1,i],c='g',s=2250)
            plt.scatter(passive1[:,0,i],passive1[:,1,i],c='k',s=2250) 
            ax = plt.gca()
            ax.set_xbound(lower = Xmin1, upper = Xmax1)
            ax.set_ybound(lower = Ymin1, upper = Ymax1)
            writer.grab_frame()
            