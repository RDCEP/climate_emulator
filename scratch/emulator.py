import numpy as np
import pandas as pd
from data import EmulatorData, EmulatorParams

class Emulator(EmulatorData, EmulatorParams):
    def __init__(self, rcp='RCP45', lag=2):
        EmulatorData.__init__(self)
        EmulatorParams.__init__(self)
        self.nu = np.zeros(self.T)
        self.rcp = rcp
        self.CO2 = getattr(self.co2, self.rcp)
        self.logCO2 = np.log(self.CO2)
        self.lag = lag

    def rho_sum(self, region_index):
        return self.rho_power[region_index].sum()

    def get_omega(self, t, region_index):
        return self.omega[region_index][t]

    def summation(self, region_index, t):
        sum = 0.0
        for i in range(self.T):
            if i > self.lag:
                sum += self.get_omega(i-2, region_index) * self.logCO2[t-i]
            else:

        return sum

    def error(self, t, region_index):
        if t > 0:
            self.nu[t] = self.phi[region_index] * self.nu[t-1] + .000001
        return self.nu[t]

    def step(self, t, region_index):
        foo = self.beta0[region_index] + (
            self.beta1[region_index] * .5 * (self.logCO2[t] + self.logCO2[t-1])
        )
        beta2 = (
            self.beta2[region_index] * self.summation(region_index, t)
        )
        return foo + beta2 + self.error(t, region_index)

    def curve(self):
        DATA = np.zeros((len(self.boundaries.transpose()), len(self.CO2)))
        for j in range(len(self.boundaries.transpose())):
            for i in range(len(self.CO2)):
                DATA[j][i] = self.step(i, j)
        return pd.DataFrame(DATA)

def run():
    e = Emulator()
    print e.curve()[10]


if __name__ == '__main__':
#    import cProfile
#    cProfile.run('run()')
    run()
