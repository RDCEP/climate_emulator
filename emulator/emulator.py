import numpy as np
import pandas as pd
from data import EmulatorData

class Emulator(EmulatorData):
    def __init__(self, model='CCSM4', rcp='RCP26', lag=2):
        super(Emulator, self).__init__(model)
        self.nu = np.zeros(self.T)
        self.rcp = rcp
        self.CO2 = self.co2[self.rcp]
        self.logCO2 = np.log(self.CO2 / 10.**6)
        self.lag = lag
        self.temp = 'relative'
        self._regions = self._all_regions[self.model]

    @property
    def regions(self):
        return self._regions

    @regions.setter
    def regions(self, value):
        self._regions = value

    def set_rcp(self, rcp):
        self.rcp = rcp
        self.CO2 = self.co2[self.rcp]
        self.logCO2 = np.log(self.CO2 / 10.**6)

    def summation(self, t):
        """
        Calculate the summation in the third term of the equation.
        """
        if t > self.lag:
            _l = len(self.regions.columns)
            L = (_l, 1)
            exponent = np.empty((_l, t - self.lag))
            coefficient = np.empty((_l, t - self.lag))
            exponent[:] = np.arange(0, t - self.lag)
            coefficient[:] = self.logCO2[t-self.lag:0:-1]
            return (np.sum(
                self.regions.ix['rho'].values.reshape(L) ** exponent *
                coefficient * (1 - self.regions.ix['rho'].values.reshape(L)),
                axis=1
            ) + (self.logCO2[0] * self.regions.ix['rho']**(t-self.lag)))
        return self.logCO2[0]

    def error(self, t):
        """
        Calculate error (nu).
        """
        if t > 0:
            self.nu[t] = self.regions.ix['phi'] * self.nu[t-1] + .000001
        return self.nu[t]

    def step(self, t):
        """
        Calculate value for a single year of the matrix.
        """
        if t > 0:
            beta1 = (self.regions.ix['beta1'] * .5 * (self.logCO2[t] + self.logCO2[t-1]))
        else:
            beta1 = self.regions.ix['beta1'] * self.logCO2[0]
        beta2 = (
            self.regions.ix['beta2'] * self.summation(t)
        )
        return self.regions.ix['beta0'] + beta1 + beta2 + self.error(t)

    def curve(self):
        self.nu = np.zeros((len(self.co2), len(self.regions.columns)))
        years = np.linspace(2005, 2100, 96)
        data = pd.DataFrame(index=years, columns=self.regions, dtype=np.float64)
        for i in xrange(len(self.co2)):
            data.ix[i] = self.step(i)
        return data

    def write_rcp_input(self):
        output = []
        for co2 in self.co2:
            output.append(np.array(self.co2[co2]).tolist())
        return output

    def get_mean_rcp_output(self, co2=False, rcp=None, temp=None, region='GMT'):
        _input = None
        if rcp is not None:
            self.set_rcp(rcp)
        if temp is not None:
            self.temp = temp
        else:
            self.CO2 = np.array(co2)
            self.co2['CUSTOM'] = pd.Series(co2, index=self.co2.index)
            self.logCO2 = np.log(self.CO2 / 10.**6)
            rcp = 'CUSTOM'
            _input = co2
        data = {'data': []}
        data['input'] = _input
        j = 0
        for model in self.models:
            self.regions = self._global_regions[model]
            d = self.curve()
            if self.temp == 'absolute':
                _t = np.around(d[region], decimals=2).tolist()
            else:
                _t = np.around(
                    d[region] - np.linspace(d[region][0],
                    d[region][0], len(d[region])), decimals=2
                ).tolist()
            data['data'].append({
                'region': model,
                'data': _t,
                'temp_type': temp,
            })
            j += 1
            # self.all_data[model][rcp][region] = pd.Series(_t, index=np.linspace(2005, 2100, 96))
        return data

    def get_model_rcp_output(self, co2=False, model=None, rcp=None, temp=None):
        _input = None
        #TODO: These ifs are shit.
        if model is not None:
            self.model = model
        self.regions = self._all_regions[self.model]
        if rcp is not None:
            self.set_rcp(rcp)
        if temp is not None:
            self.temp = temp
        else:
            self.CO2 = np.array(co2)
            self.co2['CUSTOM'] = pd.Series(co2, index=self.co2.index)
            self.logCO2 = np.log(self.CO2 / 10.**6)
            rcp = 'CUSTOM'
            _input = co2
        data = {'data': []}
        data['input'] = _input
        d = self.curve()
        j = 0
        for region in d:
            if self.temp == 'absolute':
                _t = np.round(d[region], decimals=2).tolist()
            else:
                _t = np.around(
                    d[region] - np.linspace(
                        d[region][0], d[region][0], len(d[region])
                    ), decimals=2).tolist()
            data['data'].append({
                'region': region,
                'data': _t,
                'temp_type': temp,
            })
            j += 1
        return data


def foo():
    e = Emulator()
    print e.get_mean_rcp_output(rcp='RCP45', temp='relative')


if __name__ == '__main__':
    pass
    # import cProfile
    # cProfile.run('foo()')
    # e = Emulator()
    # e.regions = e._global_regions
    # print e.curve()
    # foo()