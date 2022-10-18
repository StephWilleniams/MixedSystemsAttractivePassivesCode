#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:43:25 2022

Functions to initialise the arrays for the active and passive particles.

@author: steve
"""

#%% Imports

import numpy as np

#%% Input/output

# Inputs...
# Nac1 = Number of active particles to initialise 
# N1 = Total number of time steps
# type1 = Type of initial condition
# Xmin1,Xmax1,Ymin1,Ymax1 = System geometry
    
# Outputs... 
# active = array of active coordinates, with t=0 initialised.

#%%

def active_seed(Nac1,N1,type1,Xmin1,Xmax1,Ymin1,Ymax1):
    
    active = np.zeros([Nac1,8,N1])
    
    if(type1 == 'u'):
        
        active[:,0,0] = np.random.uniform(Xmin1,0,Nac1)
        active[:,1,0] = np.random.uniform(Ymin1,Ymax1,Nac1)
        active[:,2,0] = np.random.uniform(-np.pi,np.pi,Nac1)
        
        #(TBD) extra check that nothing is overlapping here! 
    
    return active

#%% Input/output

# Inputs...
# Npa1 = Number of passive particles
# N1 = Total number of time steps
# type1 = Type of initial condition
# Xmin1,Xmax1,Ymin1,Ymax1 = System geometry
    
# Outputs... 
# passive = array of passive coordinates, with t=0 initialised.

#%%
    
def passive_seed(Npa1,N1,type1,Xmin1,Xmax1,Ymin1,Ymax1):
    
    passive = np.zeros([Npa1,6,N1])
    
    if(type1 == 'u'):
        
        passive[:,0,0] = np.random.uniform(0,Xmax1,Npa1)
        passive[:,1,0] = np.random.uniform(Ymin1,Ymax1,Npa1)
    
    return passive
