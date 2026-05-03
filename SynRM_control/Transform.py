import numpy as np

"""
dq to alpha-beta
"""

def park_inv(vd, vq, theta):
   return (vd*np.cos(theta) - vq*np.sin(theta),
            vd*np.sin(theta) + vq*np.cos(theta))

"""
alpha-beta to abc
"""

def clarke_inv(va, vb):
    return (va, -0.5*va + (np.sqrt(3)/2)*vb, -0.5*va - (np.sqrt(3)/2)*vb)

"""
dq to abc normalizado
"""

def dq_a_abc_gem(vd, vq, theta_e, V_max):
    va, vb     = park_inv(vd, vq, theta_e)
    va, vb, vc = clarke_inv(va, vb)
    return np.clip(np.array([va, vb, vc]) / V_max, -1.0, 1.0)