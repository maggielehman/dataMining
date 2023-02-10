# Data Mining Semester Project
# Group Members:
# Maggie Lehman
# Sofia Bzhilyanskaya

# import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import warnings

from cleaning import plot_missing_data, clean_data
from Outliers import plot_outliers

warnings.filterwarnings("ignore")
# from scipy.stats import ttest_ind, ttest_rel
# from scipy import stats

# read data using pandas
data = pd.read_csv("twcs.csv")

# plot_missing_data(data)
clean_data(data)
plot_outliers(data)
