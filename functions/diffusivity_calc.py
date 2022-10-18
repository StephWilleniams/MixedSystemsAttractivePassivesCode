
"""
Created on Mon Oct 17 13:43:25 2022

Stokes Einstein calculator for the passive particle thermal diffusivity.

@author: steve
"""

#%% Imports

import numpy as np

#%% Input/output

# Inputs...
# R1 = Particle radius (um).
# T1 = Temperature (K).
# eta1 = Dynamic viscocity of medium (Pa/s).
    
# Outputs... 
# D = thermal diffusivity (um^2/s).

#%% Function

def stokes_einstein(R1,T1,eta1):
    
    kb = 1.380649 * 10**(-23) # Boltzman constant (m^2 kg s^-2 K^-1).
    
    R = 10**(-6)*np.copy(R1) # Convert particle radius to m from um.
    
    D = kb*T1/(6*np.pi*eta1*R) # Get diffusivity.
    
    D = D*10**(12) # Convert from m to um.
    
    return D
