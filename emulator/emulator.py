import numpy as np
import pandas as pd
from data.co2 import co2
from params.geopolitical import ALL_REGIONS, REGION_INFO


class EmulatorData(object):
    def __init__(self, model, start_year=2005, end_year=2100):
        self.start_year = start_year
        self.end_year = end_year
        self.T = end_year - start_year + 1
        self.indexes0 = np.arange(self.T)
        self.indexes1 = self.indexes0 + 1
        self.model = model
        self.co2 = co2
        self._all_regions = ALL_REGIONS
        # self._global_regions = GLOBAL_REGIONS
        self._region_info = REGION_INFO

    @property
    def models(self):
        return [k for k, v in ALL_REGIONS.iteritems()]


class Emulator(EmulatorData):
    def __init__(self, model='CCSM4', rcp='RCP26'):
        super(Emulator, self).__init__(model)
        self.eta = np.zeros(self.T)
        self.rcp = rcp
        self.CO2 = self.co2[self.rcp]
        self.logCO2 = np.log(self.CO2 / 1e+6)
        self.logCO2pi = -8.1879
        self.temp = 'relative'
        self._regions = self._all_regions[self.model].\
            drop(['GMT', 'GLL', 'GLO'], axis=1)

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
        # beta_0 + beta_1 * (1 - rho) * sum(rho ** i * log(co2/co2pi))
        l = len(self.regions.columns)
        L = (l, 1)
        exponent = np.empty(t + 1)
        coefficient = np.empty(t + 1)
        exponent[:] = np.arange(0, t + 1)
        coefficient[:] = self.logCO2.iloc[t::-1] - self.logCO2pi
        rho = self.regions.loc['rho'].values.reshape(L)
        if t == 3: print(np.sum(rho ** exponent * coefficient, axis=1))
        return np.sum(rho ** exponent * coefficient, axis=1)

    def error(self, t):
        """
        Calculate error (eta).
        """
        if t > 0:
            self.eta[t] = self.regions.loc['phi'] * self.eta[t-1] + .000001
        return self.eta[t]

    def step(self, t):
        """
        Calculate value for a single year of the matrix.
        """
        return self.regions.loc['beta0'] + (
            self.regions.loc['beta1'] * (1 - self.regions.loc['rho']) *
            self.summation(t)) + self.error(t)

    def curve(self):
        self.eta = np.zeros((len(self.co2), len(self.regions.columns)))
        years = np.linspace(2005, 2100, 96)
        #FIXME: The following line breaks pandas 0.13.0 (a la webDICE)
        data = pd.DataFrame(index=years,
                            columns=self.regions.columns, dtype=np.float64)
        for i in xrange(len(self.co2)):
            data.iloc[i] = self.step(i)
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
            rcp = 'CUSTOM'
            self.co2[rcp] = pd.Series(np.array(co2), index=self.co2.index)
            self.CO2 = self.co2[rcp]
            self.logCO2 = np.log(self.CO2 / 10.**6)
            _input = co2
        data = dict(data=list())  # {'data': []}
        data['input'] = _input
        j = 0
        for model in self.models:
            self.regions = self._all_regions[model].\
                               loc[:, ('GMT', 'GLL', 'GLO')]
            d = self.curve()
            if self.temp == 'absolute':
                _t = np.around(d[region] - 273.15, decimals=2).tolist()
            else:
                _t = np.around(
                    d[region] - np.linspace(d[region].iloc[0],
                    d[region].iloc[0], len(d[region])), decimals=2
                ).tolist()
            data['data'].append({
                'abbr': model,
                'name': model,
                'data': _t,
                'temp_type': temp,
            })
            j += 1
        return data

    def get_model_rcp_output(self, co2=False, model=None, rcp=None, temp=None):
        _input = None
        #TODO: These ifs are shit.
        if model is not None:
            self.model = model
        self.regions = self._all_regions[self.model].\
            drop(['GMT', 'GLL', 'GLO'], axis=1)
        if rcp is not None:
            self.set_rcp(rcp)
        if temp is not None:
            self.temp = temp
        else:
            rcp = 'CUSTOM'
            self.co2[rcp] = pd.Series(np.array(co2), index=self.co2.index)
            self.CO2 = self.co2[rcp]
            self.logCO2 = np.log(self.CO2 / 10.**6)
            _input = co2
        data = dict(data=[], input=_input)
        d = self.curve()
        j = 0
        for region in d:
            if self.temp == 'absolute':
                _t = np.around(d[region] - 273.15, decimals=2).tolist()
            else:
                _t = np.around(
                    d[region] - np.linspace(
                        d[region].iloc[0], d[region].iloc[0], len(d[region])
                    ), decimals=2).tolist()
            data['data'].append({
                'abbr': region,
                'data': _t,
                'temp_type': temp,
                'name': self._region_info[region]['name'],
                'class': self._region_info[region]['class'],
            })
            j += 1
        return data


if __name__ == '__main__':
    pass
    # import cProfile
    # cProfile.run('foo()')
    # e = Emulator()
    # print e.curve()