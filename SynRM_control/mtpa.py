import numpy as np

def mtpa_synrm(iq_cmd, i_max):
    """
    MTPA de corriente simplificado
    """
    id_ref = abs(iq_cmd)
    iq_ref = iq_cmd

    current_norm = np.hypot(id_ref, iq_ref)

    if current_norm > i_max:
        scale = i_max / current_norm
        id_ref *= scale
        iq_ref *= scale

    return float(id_ref), float(iq_ref)