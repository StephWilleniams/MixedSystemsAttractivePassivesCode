
"""
Created on Mon Oct 17 13:43:25 2022

Various functions to implement the particle motion.

@author: steve
"""

#%% Imports

import numpy as np

#%% Input/output

# Inputs...
# 
    
# Outputs... 
# 

#%% Function

def move_active(acTemp,dt,V1,D1,Xmin1,Xmax1,Ymin1,Ymax1):
    
    # Create a store for the new positions.
    newPos = np.zeros(np.shape(acTemp))
    
    newPos[:,0] = acTemp[:,0] + dt*V1*np.cos(acTemp[:,2])
    newPos[:,1] = acTemp[:,1] + dt*V1*np.sin(acTemp[:,2])
    newPos[:,2] = acTemp[:,2] + D1*np.random.randn(len(acTemp[:,2]))
    
    # Imeplement boundary conditions.
    # Could be changed to remove the for loop?
    for i in range(len(newPos[:,0])):
    
        # X boundaries
        if(newPos[i,0] < Xmin1):
            newPos[i,0] = Xmax1 + (newPos[i,0] % Xmin1)
            newPos[i,6] -= int(newPos[i,0]/Xmin1)
        elif(newPos[i,0] > Xmax1):
            newPos[i,0] = Xmin1 + (newPos[i,0] % Xmax1)
            newPos[i,6] += int(newPos[i,0]/Xmax1)
            
        # Y boundaries
        if(newPos[i,1] < Ymin1):
            newPos[i,1] = Ymax1 + (newPos[i,1] % Ymin1)
            newPos[i,7] -= int(newPos[i,0]/Ymin1)
        elif(newPos[i,1] > Ymax1):
            newPos[i,1] = Ymin1 + (newPos[i,1] % Ymax1)
            newPos[i,7] += int(newPos[i,1]/Ymax1)
            
    return newPos

#%% Input/output

# Inputs...
# 
    
# Outputs... 
# 

#%% Function

def move_passive(paTemp,dt,D1,Xmin1,Xmax1,Ymin1,Ymax1):

    newPos = np.zeros(np.shape(paTemp))
    
    newPos[:,0] = paTemp[:,0] + D1*np.random.randn(len(paTemp[:,2]))
    newPos[:,1] = paTemp[:,1] + D1*np.random.randn(len(paTemp[:,2]))
    
    # Imeplement boundary conditions.
    # Could be changed to remove the for loop?
    for i in range(len(newPos[:,0])):
    
        # X boundaries
        if(newPos[i,0] < Xmin1):
            newPos[i,0] = Xmax1 + (newPos[i,0] % Xmin1)
            newPos[i,4] -= int(newPos[i,0]/Xmin1)
        elif(newPos[i,0] > Xmax1):
            newPos[i,0] = Xmin1 + (newPos[i,0] % Xmax1)
            newPos[i,4] += int(newPos[i,0]/Xmax1)
            
        # Y boundaries
        if(newPos[i,1] < Ymin1):
            newPos[i,1] = Ymax1 + (newPos[i,1] % Ymin1)
            newPos[i,5] -= int(newPos[i,0]/Ymin1)
        elif(newPos[i,0] > Ymax1):
            newPos[i,1] = Ymin1 + (newPos[i,1] % Ymax1)
            newPos[i,5] += int(newPos[i,1]/Ymax1)
    
    return newPos