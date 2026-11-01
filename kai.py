
import matplotlib.pyplot as plt
import scipy
import scipy.interpolate
import numpy as np

state = [0, 0]

u = 2
v = 3
L = 80

def dfunction(t, state): 
    xp, yp = state
    xp = u*t - xp 
    yp = L - yp

    dist = np.hypot(xp, yp) # velkost vektora d pouzita na normalizovanie

    return [xp/dist * v, yp/dist * v]

def meeting(t, state): 
    return np.hypot(u*t - state[0], L - state[1]) - 0.01

meeting.terminal = True

res = scipy.integrate.solve_ivp(dfunction,t_span=(0,60), y0=[0,0], events=meeting, max_step = 0.001) 

print(res.t_events[0])



