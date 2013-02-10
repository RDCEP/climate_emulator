import numpy as np
#import pandas as pd
import json
from data import EmulatorData, EmulatorParams

class Emulator(EmulatorData, EmulatorParams):
    def __init__(self, rcp='RCP60', lag=2):
        EmulatorData.__init__(self)
        EmulatorParams.__init__(self)
        self.nu = np.zeros(self.T)
        self.rcp = rcp
        self.CO2 = getattr(self.co2, self.rcp)
        self.logCO2 = np.log(self.CO2 / 10.**6)
        self.lag = lag

    def rho_sum(self, region_index):
        """
        Unused. Return sum of rho.
        """
        return self.rho_power[region_index].sum()

    def get_omega(self, t, region_index):
        """
         Unused. Return omega.
        """
        return self.omega[region_index][t]

    def summation(self, region_index, t):
        """
        Calculate the summation in the third term of the equation.
        """
        _sum = 0.0
        if t >= self.lag:
            for i in range(t-self.lag):
                _sum += self.rho[region_index]**i * self.logCO2[t-self.lag-i] * \
                       (1 - self.rho[region_index])
            _sum += self.logCO2[0] * self.rho[region_index]**(t-self.lag)
        else:
            _sum = self.logCO2[0]
        return _sum

    def error(self, t, region_index):
        """
        Calculate error (nu).
        """
        if t > 0:
            self.nu[t] = self.phi[region_index] * self.nu[t-1] + .000001
        return self.nu[t]

    def step(self, t, region_index):
        """
        Calculate value for a single year of the matrix.
        """
        if t > 0:
            beta1 = (
                self.beta1[region_index] * .5 * (self.logCO2[t] + self.logCO2[t-1])
            )
        else:
            beta1 = self.beta1[region_index] * self.logCO2[0]
        beta2 = (
            self.beta2[region_index] * self.summation(region_index, t)
        )
        return self.beta0[region_index] + beta1 + beta2 + self.error(t, region_index)

    def curve(self):
        DATA = np.zeros((len(self.boundaries.transpose()), len(self.co2)))
        for j in range(len(self.boundaries.transpose())):
            for i in range(len(self.co2)):
                DATA[j][i] = self.step(i, j)
        return DATA

    def write_rcp_input(self):
        output = []
        for co2 in self.co2:
            output.append(np.array(self.co2[co2]).tolist())
        return output

    def write_rcp_output(self):
        with open('../static/js/newest_output.js', 'a+') as f:
            f.write('var output = [\n')
            e = Emulator()
            for i in ['RCP30', 'RCP45', 'RCP60', 'RCP85']:
                e.rcp = i
                d = e.curve()
                # f.write('  {"name": %s, "output": %s}' % (
                #     i, json.dumps(d.tolist())))
                f.write('  {"name": %s, "output": [\n    ' % i)
                _d = json.dumps(d.tolist())
                for j in range(len(_d)):
                    f.write('{"region": "%s", "output": %s' % (self.boundaries))
                if i != 'RCP85':
                    f.write(',\n')
                else:
                    f.write('\n')
            f.write('}')


def foo():
    e = Emulator()
    e.write_rcp_output()

def run():
    e = Emulator()
    d = e.curve()
    i = e.write_rcp_input()
    with open('../static/js/output.js', 'a+') as f:
        f.write('var output = %s;\n' % json.dumps(d.tolist()))
    with open('../static/js/input.js', 'a+') as f:
        f.write('var inputs = %s;\n' % json.dumps(i))

#    print np.array(e.co2['RCP45']).tolist()

if __name__ == '__main__':
#    import cProfile
#    cProfile.run('run()')
#    run()
    foo()