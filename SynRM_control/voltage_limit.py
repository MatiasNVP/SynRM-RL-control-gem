import numpy as np

def limit_voltage(vd, vq, v_max):
    """
    Limit el dq voltage vector
    """
    v_norm = np.hypot(vd, vq)
    
    if v_norm > v_max:
        factor = v_max / v_norm
        vd *= factor
        vq *= factor
        