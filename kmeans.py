from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import sys
import os


from k_means_plus_plus import *


# We create a data set with three sets of 500 points each chosen from a normal distrubution with a standard deviation of 10.
# The means for the distributions from which we sample are:
data=pd.read_csv('/Desktop/Seminar/myy.csv')
# Grab a scatterplot
import matplotlib.pyplot as plt

# Cluster
kmpp = KMeansPlusPlus(data, 3)
kmpp.cluster()
