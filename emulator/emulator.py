import numpy as np
from datetime import datetime
import pandas as pd
import json
from data import EmulatorData, EmulatorParams

class Emulator(EmulatorData, EmulatorParams):
    def __init__(self, rcp='RCP26', lag=2):
        EmulatorData.__init__(self)
        EmulatorParams.__init__(self)
        self.nu = np.zeros(self.T)
        self.rcp = rcp
        self.CO2 = getattr(self.co2, self.rcp)
        self.logCO2 = np.log(self.CO2 / 10.**6)
        self.lag = lag

    def set_rcp(self, rcp):
        self.rcp = rcp
        self.CO2 = getattr(self.co2, self.rcp)
        self.logCO2 = np.log(self.CO2 / 10.**6)

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

    def summation(self, region, t):
        """
        Calculate the summation in the third term of the equation.
        """
        _sum = 0.0
        if t >= self.lag:
            for i in range(t-self.lag):
                _sum += region['rho']**i * self.logCO2[t-self.lag-i] * \
                       (1 - region['rho'])
            _sum += self.logCO2[0] * region['rho']**(t-self.lag)
        else:
            _sum = self.logCO2[0]
        return _sum

    def error(self, t, region):
        """
        Calculate error (nu).
        """
        if t > 0:
            self.nu[t] = region['phi'] * self.nu[t-1] + .000001
        return self.nu[t]

    def step(self, t, r):
        """
        Calculate value for a single year of the matrix.
        """
        region = self.boundaries[r]
        if t > 0:
            beta1 = (region['beta1'] * .5 * (self.logCO2[t] + self.logCO2[t-1]))
        else:
            beta1 = region['beta1'] * self.logCO2[0]
        beta2 = (
            region['beta2'] * self.summation(region, t)
        )
        return region['beta0'] + beta1 + beta2 + self.error(t, region)

    def curve(self):
        years = np.linspace(2005, 2100, 96)
        data = pd.DataFrame(index=years)
        # DATA = np.zeros((len(self.boundaries.transpose()), len(self.co2)))
        for region in self.boundaries:
            carbon = []
            for i in range(len(self.co2)):
                carbon.append(self.step(i, region))
            data[region] = carbon
        return data

    def write_rcp_input(self):
        output = []
        for co2 in self.co2:
            output.append(np.array(self.co2[co2]).tolist())
        return output

    def write_rcp_output(self):
        now = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        b = []
        for key in self.boundaries.keys():
            b.append(key)
        with open('../static/js/output_%s.js' % now, 'a+') as f:
            f.write('var output = [\n')
            for i in ['RCP26', 'RCP45', 'RCP60', 'RCP85']:
                self.set_rcp(i)
                d = self.curve()
                f.write('  {"name": "%s", "output": [\n' % i)
                j = 0
                for region in d:
                    f.write(
                        '    {"region": "%s",\n     "absolute": %s,\n     "relative": %s}'
                        % (region, json.dumps(d[region].tolist()), json.dumps(
                            (d[region] - np.linspace(d[region][0],
                             d[region][0], len(d[region]))).tolist()
                        ))
                    )
                    j += 1
                    if j < len(d.transpose()):
                        f.write(',')
                    f.write('\n')
                if i != 'RCP85':
                    f.write('  ]},\n')
                else:
                    f.write('  ]}\n')
            f.write('];')


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