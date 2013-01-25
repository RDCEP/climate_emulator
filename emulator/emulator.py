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
        self.lag = lag
        self.CO2 = getattr(self.co2, self.rcp)
        self.logCO2 = np.log(self.CO2 / 10.**6)

    def change_input(self, rcp='RCP26'):
        """
        Update CO
        """
        self.rcp = rcp
        self.CO2 = getattr(self.co2, self.rcp)
        self.logCO2 = np.log(self.CO2 / 10.**6)

    def summation(self, region_index, t):
        """
        Calculate the summation in the third term of the equation.
        """
        sum = 0.0
        if t >= self.lag:
            for i in range(t-self.lag):
                sum += self.rho[region_index]**i * self.logCO2[t-self.lag-i] * \
                       (1 - self.rho[region_index])
            sum += self.logCO2[0] * self.rho[region_index]**(t-self.lag)
        else:
            sum = self.logCO2[0]
        return sum

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
        REGIONS = [
            'ARL', 'ANL', 'ALA', 'CGI', 'WNA', 'CNA', 'ENA', 'CAM', 'AMZ', 'SSA', 'NEU',
            'SEU', 'SAH', 'WAF', 'EAF', 'SAF', 'NAS', 'CAS', 'TIB', 'EAS', 'SAS', 'SEA',
            'SAU', 'NAU', 'CAR', 'IND', 'SPW', 'SPE', 'EPW', 'EPE', 'NPW', 'NPE', 'NAT',
            'SAT', 'EAT', 'SIO', 'NNE', 'NNW', 'WPE', 'WPS', 'HBO', 'WPN', 'NNA', 'ARO',
            'AOP', 'AOI', 'MED', 'ANL',
            ]
        with open('../static/js/newoutput.js', 'w') as f:
            f.write('var newoutput = [\n')
            e = Emulator()
            for i in ['RCP26', 'RCP45', 'RCP60', 'RCP85']:
                e.change_input(i)
                d = e.curve()
                f.write('  {"name": "%s", "output": [\n' % i)
                for j in range(len(d)):
                    f.write(
                        '    {"region": "%s",\n' % REGIONS[j]
                    )
                    f.write(
                        '     "values": %s}' % json.dumps(d.tolist()[j])
                    )
                    if j == len(d)-1:
                        f.write('\n')
                    else:
                        f.write(',\n')

                if i != 'RCP85':
                    f.write(']},\n')
                else:
                    f.write(']}\n')
            f.write(']')

def foo():
    e = Emulator()
    e.write_rcp_output()

def run():
    e = Emulator()
    d = e.curve()
    print d

if __name__ == '__main__':
    import cProfile
#    cProfile.run('run()')
    cProfile.run('foo()')
#    run()
#    foo()