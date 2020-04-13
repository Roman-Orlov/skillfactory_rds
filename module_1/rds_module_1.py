import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from collections import Counter
data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
year_08 = data[data.release_year==2008]
print ("most profitable film 2008", year_08[year_08.profit == year_08.profit.max()])
