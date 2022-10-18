#%% Preamble

"""
Title: Phototactic active particles interacting with fluorescent passive particles.
Author: Stephen Willams.
History: (1) Started 17th October 2022.
"""

#%% Notes...
    
"""

# Swimmer orientation: values range from -pi to pu. 
# x = (1,0) defines theta=0 and x=(0,1) defines theta = pi/2.
    
# Periodic boundary conditions.

# Ghost colloids?

# Initalises the active particles in the left side of the system, the passive in the left. There ~must~ then be an equillibration time. 
# (TBD) a load type that loads in an initial condition that has been pre-equillibrated?

# Currently 1'o solver, change to RK 2'o?

"""

#%% File pathing

# can use %cd to get the working directory from this
mypath = '/Users/steve/Google Drive/Academia/p_projects/a_c_ActivePassiveMixsedSystemsAttraction/c-attractiveColloids/Active-AttractivePassive_py'
    
#%% Imports

# Premade
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

# Handmade
from functions.diffusivity_calc import stokes_einstein
from functions.positional_seeds import active_seed,passive_seed
from functions.particle_motion import move_active,move_passive
from movies.movie_maker import movie_maker

#%% Constants

# Time
dt = 0.01 # time step (s).
T = 10. # total runtime (s).
N = int(T/dt) # number of steps.

# Geometry 
Lsystem = 50. # Systen characteristic lenth
# Square system.
Xmax = Lsystem 
Xmin = -Xmax 
Ymax = Lsystem
Ymin = -Ymax 
## other geometries here TBD?
## Note: this is largely here in case boundaries need to be implemented.

# Active particle
Nac = 4 # Number of active particles.
R_active = 5. # Radius of the active particle (um).
D_rot = 1. # Active particle rotational diffusivity (Rad/s). Note: 1/D gives the characteristic re-orientation time. 
sqrt2DrotDt = np.sqrt(2*D_rot*dt) # Get the diffusion size.
V_swim = 100. # Swim speed of the active particles (um/s).
acIVPtype = 'u'

# Passive particle
Npa = 1 # Number of passive particles.
R_passive = 5. # Radius of the passive particle (um).
D_therm = stokes_einstein(R_passive, 300., 8.9*10**(-4)) # Passive particle thermal diffusivity (um^2/s).
sqrt2DthermDt = np.sqrt(2*D_therm*dt) # Get the diffusion size.
paIVPtype = 'u'

# Potentials 


#%% Preallocation.

active = active_seed(Nac,N,acIVPtype,Xmin,Xmax,Ymin,Ymax) # Active particle's coordinates (x,y,theta,dU/dx,dU/dx,dU/dtheta,wraps).
passive = passive_seed(Npa,N,paIVPtype,Xmin,Xmax,Ymin,Ymax) # Passive particle's coordinates (x,y,dU/dx,dU/dx,wraps).

#%% Main loop

###

# Loop on total number of steps.
for n in range(1,N):
    
    # Get the actual time.
    time = dt*n 
    
    # Get the values of Du/di for all particles.
    #(TBD) this will be done with a function.
    
    
    # Increment the motion.
    active[:,:,n] = move_active(active[:,:,n-1],dt,V_swim,sqrt2DrotDt,Xmin,Xmax,Ymin,Ymax)
    passive[:,:,n] = move_passive(passive[:,:,n-1],dt,sqrt2DthermDt,Xmin,Xmax,Ymin,Ymax)

#%% Plotting tools

###

movie_maker(active,passive,Xmin,Xmax,Ymin,Ymax)
    
