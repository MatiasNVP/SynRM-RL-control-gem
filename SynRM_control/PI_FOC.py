import numpy as np

class PIControlador:

    def __init__(self, kp, ki, limite, dt):
        self.kp      = kp
        self.ki      = ki
        self.limite  = limite
        self.dt      = dt
        self.integral = 0.0

    def reset(self):
        self.integral = 0.0  #Para reiniciar el controlador

    def calcular(self, setpoint, actual):
        error = setpoint - actual
        self.integral += error * self.dt

        #Anti windup
        if self.ki > 0:
            self.integral = np.clip(self.integral,
                                    -self.limite / self.ki,
                                     self.limite / self.ki)
        return float(np.clip(self.kp*error + self.ki*self.integral,
                             -self.limite, self.limite))