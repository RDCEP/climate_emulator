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
    def __init__(self, model='CCSM4', rcp='RCP26', lag=2):
        super(Emulator, self).__init__(model)
        self.nu = np.zeros(self.T)
        self.rcp = rcp
        self.CO2 = self.co2[self.rcp]
        self.logCO2 = np.log(self.CO2 / 10.**6)
        self.lag = lag
        self.temp = 'relative'
        self._regions = self._all_regions[self.model].drop(['GMT', 'GLL', 'GLO'], axis=1)

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
        if t > self.lag - 1:
            _l = len(self.regions.columns)
            L = (_l, 1)
            exponent = np.empty((_l, t - self.lag + 1))
            coefficient = np.empty((_l, t - self.lag + 1))
            exponent[:] = np.arange(0, t - self.lag + 1)
            coefficient[:] = self.logCO2.iloc[t - self.lag::-1]
            rho = self.regions.loc['rho'].values.reshape(L)
            s = (np.sum(rho ** exponent * coefficient * (1 - rho), axis=1))
            s += (self.logCO2.iloc[0] *
                  self.regions.loc['rho'] ** (t - self.lag + 1))
            return s
        return self.logCO2.iloc[0]

    def error(self, t):
        """
        Calculate error (nu).
        """
        if t > 0:
            self.nu[t] = self.regions.loc['phi'] * self.nu[t-1] + .000001
        return self.nu[t]

    def step(self, t):
        """
        Calculate value for a single year of the matrix.
        """
        if t > 0:
            beta1 = (self.regions.loc['beta1'] * .5 *
                     (self.logCO2.iloc[t] + self.logCO2.iloc[t-1]))
        else:
            beta1 = self.regions.loc['beta1'] * self.logCO2.iloc[0]
        beta2 = (
            self.regions.loc['sig2'] * self.summation(t)
        )
        return self.regions.loc['beta0'] + beta1 + beta2 + self.error(t)

    def curve(self):
        self.nu = np.zeros((len(self.co2), len(self.regions.columns)))
        years = np.linspace(2005, 2100, 96)
        #FIXME: The following line breaks pandas 0.13.0 (a la webDICE)
        data = pd.DataFrame(index=years, columns=self.regions.columns, dtype=np.float64)
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
            #TODO: Get global means from larger dicts
            # self.regions = self._global_regions[model]
            self.regions = self._all_regions[model].loc[:, ('GMT', 'GLL', 'GLO')]
            d = self.curve()
            if self.temp == 'absolute':
                _t = np.around(d[region], decimals=2).tolist()
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
            # self.all_data[model][rcp][region] = pd.Series(_t, index=np.linspace(2005, 2100, 96))
        return data

    def get_model_rcp_output(self, co2=False, model=None, rcp=None, temp=None):
        _input = None
        #TODO: These ifs are shit.
        if model is not None:
            self.model = model
        self.regions = self._all_regions[self.model].drop(['GMT', 'GLL', 'GLO'], axis=1)
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
        data = {'data': []}
        data['input'] = _input
        d = self.curve()
        j = 0
        for region in d:
            if self.temp == 'absolute':
                _t = np.around(d[region], decimals=2).tolist()
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


def foo():
    rho, beta0, beta1, beta2, phi = (0.832341, 257.031747, 7.760533, 7.760533, 0.16191)
    lag = 2
    co2 = np.array([375.11, 377.78, 380.58, 383.52, 386.7, 390.12, 393.8, 397.55, 401.15,
        404.61, 407.97, 411.24, 414.42, 417.5, 420.55, 423.46, 426.14, 428.59,
        430.91, 433.15, 435.33, 437.46, 439.52, 441.51, 443.42, 445.15, 446.62,
        447.94, 449.21, 450.4, 451.52, 452.58, 453.57, 454.49, 455.33, 455.98,
        456.34, 456.52, 456.61, 456.62, 456.56, 456.44, 456.28, 456.07, 455.82,
        455.44, 454.85, 454.15, 453.42, 452.66, 451.86, 451.05, 450.24, 449.42,
        448.6, 447.83, 447.18, 446.56, 445.92, 445.28, 444.62, 443.94, 443.27,
        442.6, 441.95, 441.34, 440.8, 440.3, 439.81, 439.33, 438.85, 438.37,
        437.88, 437.4, 436.94, 436.48, 435.97, 435.47, 435., 434.52, 434.03,
        433.54, 433.03, 432.5, 431.98, 431.47, 431., 430.55, 430.11, 429.68,
        429.25, 428.82, 428.39, 427.95, 427.5, 426.96])
    logco2 = np.log(co2 * 1e-6)
    n = len(co2)
    for i in range(n):
        sum = 0
        if i >= lag:
            for j in range(i - lag + 1):
                sum += rho ** i * logco2[i - lag] * (1 - rho)
        print sum

if __name__ == '__main__':
    # pass
    # import cProfile
    # cProfile.run('foo()')
    e = Emulator()
    # e.regions = e._global_regions
    print e.get_model_rcp_output()
    # print e.curve()
    # foo()