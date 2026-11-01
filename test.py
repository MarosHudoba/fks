import matplotlib.pyplot as plt
import scipy
import scipy.interpolate

G = 9.81
mass = 0.45
Coe = 0.66
air = 1.2
crosssec = 0.02

times = []
H = [3,7,29,582,3365,6424,7809,8237,8391,7932,6805,5224,3130,1986,1508,1207,1007,863,740,628,531,447,372,301,226,145,50,0]

state = [0, 0] #initial state

for i,v in enumerate(H):
    H[i] = (v/1000) * G 
    times.append(i/10)

interpolated = scipy.interpolate.CubicSpline(times, H)

def thrust(t): #thrust function
    return 0.0 if t > times[-1] else interpolated(t)

def idkfun(t, state): #derivation func
    x, v = state
    a = (thrust(t) - (mass * G) - (0.5*Coe*crosssec*air*abs(v)*v))/mass
    if a < 0 and x <= 0: return [0, 0] # accounts for ground force since i am lazy to do that
    return [v, a]

def groundhit(t, state): return state[0]
groundhit.terminal = True
groundhit.direction = -1

res = scipy.integrate.solve_ivp(idkfun,t_span=(0,15), y0=[0,0], max_step = 0.01) #events = groundhit

print(res)

plt.plot(res.t, res.y[0]) 
plt.show()

