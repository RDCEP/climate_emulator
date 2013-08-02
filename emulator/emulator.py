import numpy as np
from datetime import datetime
import pandas as pd
import json
from data import EmulatorData, EmulatorParams

class Emulator(EmulatorData, EmulatorParams):
    def __init__(self, model='CCSM4', rcp='RCP26', lag=2):
        EmulatorData.__init__(self, model)
        EmulatorParams.__init__(self)
        self.nu = np.zeros(self.T)
        self.rcp = rcp
        self.CO2 = getattr(self.co2, self.rcp)
        self.logCO2 = np.log(self.CO2 / 10.**6)
        self.lag = lag
        self.temp = 'relative'

    def set_rcp(self, rcp):
        self.rcp = rcp
        self.CO2 = getattr(self.co2, self.rcp)
        self.logCO2 = np.log(self.CO2 / 10.**6)

    def summation(self, region, t):
        """
        Calculate the summation in the third term of the equation.
        """
        if t > self.lag:
            return np.sum(
                region['rho'] ** np.arange(0, t-self.lag) *
                self.logCO2[t-self.lag:0:-1] *
                (1 - region['rho'])
            ) + self.logCO2[0] * region['rho']**(t-self.lag)
        return self.logCO2[0]

    def error(self, t, region):
        """
        Calculate error (nu).
        """
        if t > 0:
            self.nu[t] = region['phi'] * self.nu[t-1] + .000001
        return self.nu[t]

    def step(self, t, region):
        """
        Calculate value for a single year of the matrix.
        """
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
                carbon.append(self.step(i, self.boundaries[region]))
            data[region] = carbon
        return data

    def write_rcp_input(self):
        output = []
        for co2 in self.co2:
            output.append(np.array(self.co2[co2]).tolist())
        return output

    def get_model_rcp_output(self, co2=False, model=None, rcp=None, temp=None):
        if model is not None:
            self.model = model
        if rcp is not None:
            self.set_rcp(rcp)
        if temp is not None:
            self.temp = temp
        else:
            self.CO2 = np.array(co2)
            self.logCO2 = np.log(self.CO2 / 10.**6)
            rcp = 'CUSTOM'
        now = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        b = []
        for key in self.boundaries.keys():
            b.append(key)
        data = {'data': []}
        d = self.curve()
        j = 0
        for region in d:
            if self.temp == 'absolute':
                _t = np.around(d[region], decimals=2).tolist()
            else:
                _t = np.around(
                    d[region] - np.linspace(d[region][0],
                    d[region][0], len(d[region])), decimals=2
                ).tolist()
            data['data'].append({
                'region': region,
                'data': _t,
                'temp_type': temp,
            })
            j += 1
        return data


def foo():
    e = Emulator()
    print e.get_model_rcp_output(model='CCSM4', rcp='RCP45')


if __name__ == '__main__':
    import cProfile
    cProfile.run('foo()')
#    run()
#     write_default_rcps()