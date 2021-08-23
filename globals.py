"""
globals.py

Globals used by model
"""
import os

################################################################################
#setup consts
datadir_ex = "./external-data"
modelRunsDir = "./model-runs"
data_zone_shapefile = os.path.join(datadir_ex, "geography/Athens_zone.shp")
data_link_shapefile = os.path.join(datadir_ex, "geography/Athens_link.shp")
data_node_shapefile = os.path.join(datadir_ex, "geography/Athens_node.shp")
data_connector_shapefile = os.path.join(datadir_ex, "geography/Athens_connector.shp")
data_centroid_shapefile = os.path.join(datadir_ex, "geography/Athens_zone_centroid.shp")

# census data
data_census_pop = os.path.join(datadir_ex,"Census2011/popdistr.csv")
pop_2045 = os.path.join(datadir_ex,"Census2011/popdistr_2045.csv")

# Employment
data_employment = os.path.join(datadir_ex,"Employment/employment_ath.csv")
data_employment_2030 = os.path.join(datadir_ex,"Employment/employment_ath_2030.csv")
data_employment_2045 = os.path.join(datadir_ex,"Employment/employment_ath_2045.csv")
HH_floorspace = os.path.join(datadir_ex,"Employment/hh_floorspace.csv")
HH_floorspace_2045 = os.path.join(datadir_ex,"Employment/hh_floorspace_2045.csv")

#output files
data_HH_zones = os.path.join(modelRunsDir,"jobs_Pop_Zones.csv")
data_HH_attractors = os.path.join(modelRunsDir,"jobs_HH_Attractors.csv")
data_jobs_cij = os.path.join(modelRunsDir,"jobs_Cij.bin")

# Probabilities matrices:
# data_jobs_probTij = os.path.join(modelRunsDir,"jobsProbTij.bin")
data_jobs_probTij_public_2019 = os.path.join(modelRunsDir,"jobsProbTij_pu.bin")
data_jobs_probTij_public_2019_csv = os.path.join(modelRunsDir,"jobs_probTij_public_2019.csv")
data_jobs_probTij_private_2019 = os.path.join(modelRunsDir,"jobsProbTij_pr.bin")
data_jobs_probTij_private_2019_csv = os.path.join(modelRunsDir,"jobs_probTij_private_2019.csv")
data_jobs_probTij_public_2030 = os.path.join(modelRunsDir,"jobsProbTij_pu_2030.bin")
data_jobs_probTij_public_2030_csv = os.path.join(modelRunsDir,"jobs_probTij_public_2030.csv")
data_jobs_probTij_private_2030 = os.path.join(modelRunsDir,"jobsProbTij_pr_2030.bin")
data_jobs_probTij_private_2030_csv = os.path.join(modelRunsDir,"jobs_probTij_private_2030.csv")
data_jobs_probTij_public_2045 = os.path.join(modelRunsDir,"jobsProbTij_pu_2045.bin")
data_jobs_probTij_public_2045_csv = os.path.join(modelRunsDir,"jobs_probTij_public_2045.csv")
data_jobs_probTij_private_2045 = os.path.join(modelRunsDir,"jobsProbTij_pr_2045.bin")
data_jobs_probTij_private_2045_csv = os.path.join(modelRunsDir,"jobs_probTij_private_2045.csv")

# People flows matrices:
data_jobs_Tij_pu_2019 = os.path.join(modelRunsDir,"jobsTij_pu.bin")
data_jobs_Tij_pu_2019_csv = os.path.join(modelRunsDir,"jobs_Tij_public_2019.csv")
data_jobs_Tij_pr_2019 = os.path.join(modelRunsDir,"jobsTij_pr.bin")
data_jobs_Tij_pr_2019_csv = os.path.join(modelRunsDir,"jobs_Tij_private_2019.csv")
data_jobs_Tij_pu_2030 = os.path.join(modelRunsDir,"jobsTij_pu_2030.bin")
data_jobs_Tij_pu_2030_csv = os.path.join(modelRunsDir,"jobs_Tij_public_2030.csv")
data_jobs_Tij_pr_2030 = os.path.join(modelRunsDir,"jobsTij_pr_2030.bin")
data_jobs_Tij_pr_2030_csv = os.path.join(modelRunsDir,"jobs_Tij_private_2030.csv")
data_jobs_Tij_pu_2045 = os.path.join(modelRunsDir,"jobsTij_pu_2045.bin")
data_jobs_Tij_pu_2045_csv = os.path.join(modelRunsDir,"jobs_Tij_public_2045.csv")
data_jobs_Tij_pr_2045 = os.path.join(modelRunsDir,"jobsTij_pr_2045.bin")
data_jobs_Tij_pr_2045_csv = os.path.join(modelRunsDir,"jobs_Tij_private_2045.csv")

################################################################################

ZoneCodesFilename = 'ATH_ZoneCodes.csv'

#cost matrix names
CijPublicMinFilename = "cij_pu.bin"
CijPrivateMinFilename = "cij_pr.bin"
CijPublicMinFilename_csv = "Cij_public.csv"
CijPrivateMinFilename_csv = "Cij_private.csv"

#ODPuFilename = 'ODPu.bin'
#ODPrFilename = 'ODPr.bin'
ODPuFilename_csv = 'ODPu.csv'
ODPrFilename_csv = 'ODPr.csv'

intrazone_dist_csv = "intrazone_distances.csv"

################################################################################
