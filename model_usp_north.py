# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:42:47 2023

@author: battuejd
"""

import pandas as pd
import pandapower as pp
from pandapower import plotting as plot
import load_usp_grid_simple_north as lugn



lugn
net = lugn.net
demand_profiles = lugn.demand_profiles
i = list(demand_profiles.index.values)
energiegebruik = 0
totale_kwadratensom = 0
overbelastingsuren = 0
results = dict()


############################################################################################################   for loop die een jaar simuleert   ###############################################################################



for t in i:
    

    net.load.iat[ 0 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 1 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 2 , 2] = 1.60*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 3 , 2] = 0.16*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 4 , 2] = (demand_profiles.at[t, 'res_1']/14.5)*0.63
    net.load.iat[ 5 , 2] = 1.25*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 6 , 2] = 1.60*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 7 , 2] = 1.00*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 8 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 9 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 10 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 11 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 12 , 2] = 0.40*0.5
    net.load.iat[ 13 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 14 , 2] = 0.630*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 15 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 16 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 17 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 18 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 19 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 20 , 2] = 0.075*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 21 , 2] = 0.40*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 22 , 2] = 0.40*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 23 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 24 , 2] = 0.25*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 25 , 2] = 1.00*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 26 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 27 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 28 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 29 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 30 , 2] = 0.40*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 31 , 2] = 0.40*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 32 , 2] = 0.25*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 33 , 2] = 0.25*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 34 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 35 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 36 , 2] = 0.25*0.5
    net.load.iat[ 37 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 38 , 2] = 1.00*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 39 , 2] = 0.63*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 40 , 2] = 0.25*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 41 , 2] = 0.25*0.5
    net.load.iat[ 42 , 2] = 0.40*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 43 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 44 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 45 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 46 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 47 , 2] = 0.40*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 48 , 2] = 0.20*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 49 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 50 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 51 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 52 , 2] = 0.40*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 53 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 54 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 55 , 2] = 0.40*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 56 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 57 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 58 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 59 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 60 , 2] = 0.4*demand_profiles.at[t, 'ev_simpel']
    net.load.iat[ 61 , 2] = 0.05*demand_profiles.at[t, 'ev_simpel']
    
    
    net.sgen.iat[ 0 , 2] = 3.5*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 1 , 2] = 2.5*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 2 , 2] = 0.1323*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 3 , 2] = 0.136*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 4 , 2] = 0.0405*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 5 , 2] = 0.0288*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 6 , 2] = 0.12*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 7 , 2] = 0.034*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 8 , 2] = 0.0413*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 9 , 2] = 2.5*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 10 , 2] = 0.3*demand_profiles.at[t, 'pv_veld_1_MW']
     
    pp.runpp(net, max_iteration=10000)
    
    
    
    
    #######################################################################   Diagnostiek   #######################################################
    
    
    results[t] = net.res_line.loading_percent.max()
    
    
    list_kabelbelastingen = net.res_line.loading_percent.values.tolist()
    list_kabelbelastingen_groterdan_100 = [item for item in list_kabelbelastingen if item > 100]
    list_kabelbelastingen_groterdan_100 = [i - 100 for i in list_kabelbelastingen_groterdan_100]
    
    
    kwadratensom = sum(i*i for i in list_kabelbelastingen_groterdan_100)
    totale_kwadratensom = totale_kwadratensom + kwadratensom
    
    
    if len(list_kabelbelastingen_groterdan_100) > 0:
        overbelastingsuren = overbelastingsuren + 1
    
    
    
    print(net.res_line.loading_percent.max())
    print(t)










##################################################################################################   Nuttige regeltjes code   ####################################################################################3


print(overbelastingsuren)
print(energiegebruik)
print(totale_kwadratensom)