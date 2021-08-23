"""
Public interface to the data
Contains accessor functions for getting probabilities of trips from workplaces to residential zones.
Further information is contained in each function description.
"""

import pandas as pd
import numpy as np
import pickle
from globals import *
import os
from analytics import graphProbabilities
from geojson import dump, FeatureCollection, Feature, GeometryCollection, LineString, MultiLineString
from sklearn.metrics import mean_squared_error   # Mean square error
from sklearn.metrics import r2_score   # To get the R^2 from a linear fit
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

################################################################################
# Utilities
################################################################################

"""
Load a numpy matrix from a file
"""
def loadMatrix(filename):
    with open(filename,'rb') as f:
        matrix = pickle.load(f)
    return matrix

################################################################################
# Globals
################################################################################
# 2 MODES

# Observed flows:
# JtW_OD_pu = loadMatrix('model-runs/ODPu.bin')
# JtW_OD_pr = loadMatrix('model-runs/ODPr.bin')

# Predicted flows
JtW_predOD_pu = loadMatrix(data_jobs_Tij_pu_2019)
JtW_predOD_pr = loadMatrix(data_jobs_Tij_pr_2019)


################################################################################
# Interface
################################################################################

# Create Geojson file with flows

threshold = 0.2 #  The threshold below which to ignore low probability trips

# 2019 model - private flows
print("Creating flows for 2019 - private")
dfPointsPopulation_2019 = pd.read_csv(os.path.join(datadir_ex,'zones_data_coordinates.csv'), usecols=["zonei", "zone", "pop_tot_2019", "employment_2019", "Greek_Grid_east", "Greek_Grid_north"]) # create df from csv
pointsProbSij_2019_pr = loadMatrix('model-runs/jobsProbTij_pr.bin') # pointsProbSij matrix of probabilities
geojson_flows_2019_pr = graphProbabilities(threshold, dfPointsPopulation_2019, pointsProbSij_2019_pr)

# Now save the flows into a file:
print("Saving 2019-private flows to file")
with open(os.path.join(modelRunsDir, 'flows_2019_pr.geojson'), 'w') as f:
    dump(geojson_flows_2019_pr, f)

# 2019 model - public flows
print("Creating flows for 2019 - private")
pointsProbSij_2019_pu = loadMatrix('model-runs/jobsProbTij_pu.bin') # pointsProbSij matrix of probabilities
geojson_flows_2019_pu = graphProbabilities(threshold, dfPointsPopulation_2019, pointsProbSij_2019_pu)

# Now save the flows into a file:
print("Saving 2019-public flows to file")
with open(os.path.join(modelRunsDir, 'flows_2019_pu.geojson'), 'w') as f:
    dump(geojson_flows_2019_pu, f)

# 2030 model - private flows
print("Creating flows for 2030 - private")
dfPointsPopulation_2030 = pd.read_csv(os.path.join(datadir_ex,'zones_data_coordinates.csv'), usecols=["zonei", "zone", "pop_tot_2030", "employment_2030", "Greek_Grid_east", "Greek_Grid_north"]) # create df from csv
pointsProbSij_2030_pr = loadMatrix('model-runs/jobsProbTij_pr_2030.bin') # pointsProbSij matrix of probabilities
geojson_flows_20309_pr = graphProbabilities(threshold, dfPointsPopulation_2030, pointsProbSij_2030_pr)

# Now save the flows into a file:
print("Saving 2030-private flows to file")
with open(os.path.join(modelRunsDir, 'flows_2030_pr.geojson'), 'w') as f:
    dump(geojson_flows_20309_pr, f)

# 2030 model - public flows
print("Creating flows for 2030 - public")
pointsProbSij_2030_pu = loadMatrix('model-runs/jobsProbTij_pu_2030.bin') # pointsProbSij matrix of probabilities
geojson_flows_2030_pu = graphProbabilities(threshold, dfPointsPopulation_2030, pointsProbSij_2030_pu)

# Now save the flows into a file:
print("Saving 2030-public flows to file")
with open(os.path.join(modelRunsDir, 'flows_2030_pu.geojson'), 'w') as f:
    dump(geojson_flows_2030_pu, f)

# 2045 model - private flows
print("Creating flows for 2045 - private")
dfPointsPopulation_2045 = pd.read_csv(os.path.join(datadir_ex,'zones_data_coordinates.csv'), usecols=["zonei", "zone", "pop_tot_2045", "employment_2045", "Greek_Grid_east", "Greek_Grid_north"]) # create df from csv
pointsProbSij_2045_pr = loadMatrix('model-runs/jobsProbTij_pr_2045.bin') # pointsProbSij matrix of probabilities
geojson_flows_2045_pr = graphProbabilities(threshold, dfPointsPopulation_2045, pointsProbSij_2045_pr)

# Now save the flows into a file:
print("Saving 2045-private flows to file")
with open(os.path.join(modelRunsDir, 'flows_2045_pr.geojson'), 'w') as f:
    dump(geojson_flows_2045_pr, f)

# 2045 model - public flows
print("Creating flows for 2045 - public")
pointsProbSij_2045_pu = loadMatrix('model-runs/jobsProbTij_pu_2045.bin') # pointsProbSij matrix of probabilities
geojson_flows_2045_pu = graphProbabilities(threshold, dfPointsPopulation_2045, pointsProbSij_2045_pu)

# Now save the flows into a file:
print("Saving 2045-public flows to file")
with open(os.path.join(modelRunsDir, 'flows_2045_pu.geojson'), 'w') as f:
    dump(geojson_flows_2045_pu, f)

############################################################################################################
# Print the observed and predicted matrices:
'''
# print("OD public:")
# print(JtW_OD_pu)
# print()
print("PRED public:")
pd.options.display.float_format = '{:.1f}'.format # to display only 1 decimal point
print(JtW_predOD_pu)
print()

############################################################################################################
# Look at how many people you have by adding every value in the Sij predicted matrix together
# (for all modes and separately) to check that the total numbers of commuters are right

# print("OD Sum each column (public):")
# print(df_OD_pu.sum(axis=0))
# print()
# print("OD Sum each row (public):")
# print(df_OD_pu.sum(axis=1))
# print()
print("PRED Sum each column (public):")
print(df_PRED_pu.sum(axis=0))
print()
print("PRED Sum each row (public):")
print(df_PRED_pu.sum(axis=1))

# total trips

sum_PRED_trips_pu = df_PRED_pu.sum(axis=0)
tot_PRED_pu = sum_PRED_trips_pu.sum(axis=0)

# sum_OD_trips_pu = df_OD_pu.sum(axis=0)
# tot_OD_pu = sum_OD_trips_pu.sum(axis=0)

sum_PRED_trips_pr = df_PRED_pr.sum(axis=0)
tot_PRED_pr = sum_PRED_trips_pr.sum(axis=0)

# sum_OD_trips_pr = df_OD_pr.sum(axis=0)
# tot_OD_pr = sum_OD_trips_pr.sum(axis=0)


print()
print("tot PRED trips (public): %.1f" % tot_PRED_pu)
# print("tot OD trips (public): %.1f" % tot_OD_pu)
# print("difference (public): %.1f" % (tot_PRED_pu - tot_OD_pu))
print()
print("tot PRED trips (private): %.1f" % tot_PRED_pr)
# print("tot OD trips (private): %.1f" % tot_OD_pr)
# print("difference (private): %.1f" % (tot_PRED_pr - tot_OD_pr))
print()
print("tot PRED trips (all modes): %.1f" % (tot_PRED_pu + tot_PRED_pr))
# print("tot OD trips (all modes): %.1f" % (tot_OD_pr + tot_OD_pu))
# print("difference (all modes): %.1f" % ((tot_PRED_pu + tot_PRED_pr) - (tot_OD_pr + tot_OD_pu)))
# print()

############################################################################################################
# Zero/negative values

print("Check zero/negative values:")
print()
# df_OD_pu = df_OD_pu[(df_OD_pu <= 0).all()]
df_PRED_pu = df_PRED_pu[(df_PRED_pu <= 0).all()]
# print("OD (public) <= 0 :")
# print(df_OD_pu)
# print()
print("PRED (public) <= 0 :")
pd.options.display.float_format = '{:.1f}'.format # to display only 1 decimal point
print(df_PRED_pu)
print()

############################################################################################################

# Check constraints on total trips on roads:
# print("Check constraints on total trips:")
# SOD_k = [JtW_OD_pu, JtW_OD_pr]  # list of obs trips matrices
# m, n = JtW_OD_pu.shape
n_modes = 2
#
# OiOD = np.zeros(m)
# for k in range(n_modes):
#     OiOD += SOD_k[k].sum(axis=1)
# print("OiOD: ", OiOD)
# print("sum of OiOD: %.1f" % sum(OiOD))
# print()
#
# DjOD = np.zeros(n)
# for k in range(n_modes):
#     DjOD += SOD_k[k].sum(axis=1)
# print("DjOD: ", DjOD)
# print("sum of DjOD: %.1f" % sum(DjOD))
# print()

print("Now check predicted sums:")
SPred_k = [JtW_predOD_pu, JtW_predOD_pr]
m, n = JtW_predOD_pu.shape
OiPred = np.zeros(m)
for k in range(n_modes):
    OiPred += SPred_k[k].sum(axis=1)
print("OiPred: ", OiPred)
print("sum of OiPred: %.1f" % sum(OiPred))
print()

DjPred = np.zeros(n)
for k in range(n_modes):
    DjPred += SPred_k[k].sum(axis=1)
print("DjPred: ", DjPred)
print("sum of DjPred: %.1f" % sum(DjPred))
print()

############################################################################################################
# Check Root Mean Square Error and R^2
# This is calculated on sum_OBS/PRED_trips_roads/bus/rail as this is the sum on axis 0 of the tot flow matrix
# i.e. they are vectors containing the total trips per zone
print("R^2 public: %.2f" % r2_score(sum_OD_trips_pu, sum_PRED_trips_pu))
print("R^2 private: %.2f" % r2_score(sum_OD_trips_pr, sum_PRED_trips_pr))
print()
print("RMSE public: %.2f" % np.sqrt(mean_squared_error(sum_OD_trips_pu, sum_PRED_trips_pu)))
print("RMSE private: %.2f" % np.sqrt(mean_squared_error(sum_OD_trips_pr, sum_PRED_trips_pr)))

# Scatter plots with seaborn
f = plt.figure()
f, (ax1, ax2) = plt.subplots(1,2)
sns.regplot(x=sum_OD_trips_pu, y=sum_PRED_trips_pu, ax=ax1, scatter_kws={'s':8})
sns.regplot(x=sum_OD_trips_pr, y=sum_PRED_trips_pr, ax=ax2, scatter_kws={'s':8})
ax1.set_xlabel('OD public')
ax1.set_ylabel('PRED public')
ax2.set_xlabel('OD private')
ax2.set_ylabel('PRED private')
plt.show()

# Histograms
sns.distplot(sum_OD_trips_pu, hist=True, kde=True,
             bins=30, color = 'darkblue',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})
plt.savefig('ODpu')

sns.distplot(sum_OD_trips_pr, hist=True, kde=False,
             bins=30, color = 'darkblue',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})
plt.savefig('ODpr')

sns.distplot(sum_PRED_trips_pu, hist=True, kde=False,
             bins=30, color = 'darkblue',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})
plt.savefig('PREDpu')

sns.distplot(sum_PRED_trips_pr, hist=True, kde=False,
             bins=30, color = 'darkblue',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})
plt.savefig('PREDpr')

#residuals
f_res = plt.figure()
f_res, (ax1, ax2) = plt.subplots(1,2)
sns.residplot(x=sum_OD_trips_pu, y=sum_PRED_trips_pu, ax=ax1, scatter_kws={'s':80})
sns.residplot(x=sum_OD_trips_pr, y=sum_PRED_trips_pr, ax=ax2, scatter_kws={'s':80})
ax1.set_xlabel('OD public residuals')
ax1.set_ylabel('PRED public residuals')
ax2.set_xlabel('OD private residuals')
ax2.set_ylabel('PRED private residuals')
plt.show()


'''