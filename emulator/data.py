import pandas as pd
import numpy as np
from model_data import all_boundaries, co2


class EmulatorParams(object):
    pass


class CarbonModel(object):
    pass


class EmulatorData(object):
    def __init__(self, model, start_year=2005, end_year=2100):
        self.start_year = start_year
        self.end_year = end_year
        self.T = end_year - start_year + 1
        self.indexes0 = np.arange(self.T)
        self.indexes1 = self.indexes0 + 1
        self.model = model
        self.co2 = pd.DataFrame(
            co2, index=np.linspace(2005, 2100, 96),
            columns=['RCP26', 'RCP45', 'RCP60', 'RCP85']
        )

    @property
    def boundaries(self):
        return all_boundaries[self.model]

    @property
    def models(self):
        return [k for k, v in all_boundaries.iteritems()]
