import pandas as pd
import numpy as np
from model_data import ALL_REGIONS, GLOBAL_REGIONS, CO2, REGION_INFO


class EmulatorData(object):
    def __init__(self, model, start_year=2005, end_year=2100):
        self.start_year = start_year
        self.end_year = end_year
        self.T = end_year - start_year + 1
        self.indexes0 = np.arange(self.T)
        self.indexes1 = self.indexes0 + 1
        self.model = model
        self.co2 = pd.DataFrame(
            CO2, index=np.linspace(2005, 2100, 96),
            columns=['RCP26', 'RCP45', 'RCP60', 'RCP85', 'EXP1600']
        )
        self._all_regions = ALL_REGIONS
        self._global_regions = GLOBAL_REGIONS
        self._region_info = REGION_INFO

    @property
    def models(self):
        return [k for k, v in ALL_REGIONS.iteritems()]

