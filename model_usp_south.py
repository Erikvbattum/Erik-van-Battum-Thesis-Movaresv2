# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:43:35 2023

@author: battuejd
"""

import pandas as pd
import pandapower as pp
from pandapower import plotting as plot
import load_usp_grid_simple_south as lugs



lugs
net = lugs.net
demand_profiles = lugs.demand_profiles
i = list(demand_profiles.index.values)
energiegebruik = 0
totale_kwadratensom = 0
overbelastingsuren = 0
results = dict()


############################################################################################################   for loop die een jaar simuleert   ###############################################################################



for t in i:
    

    net.load.iat[ 0 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 1 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 2 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 3 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 4 , 2] = 0.60*demand_profiles.at[t, 'ev_simpel']
    net.load.iat[ 5 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 6 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 7 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 8 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 9 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 10 , 2] = 1.00*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 11 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 12 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 13 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 14 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 15 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 16 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 17 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 18 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 19 , 2] = 0.10*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 20 , 2] = 0.60*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 21 , 2] = 0.30*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 22 , 2] = 0.315*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 23 , 2] = 1.00*0.5
    net.load.iat[ 24 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 25 , 2] = 0.2*demand_profiles.at[t, 'ev_simpel']
    net.load.iat[ 26 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 27 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 28 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 29 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 30 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 31 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
   
   
    net.sgen.iat[ 0 , 2] = 0.1312*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 1 , 2] = 0.2862*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 2 , 2] = 0.0499*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 3 , 2] = 2*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 4 , 2] = 0.1576*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 5 , 2] = 9*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 6 , 2] = 0.2333*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 7 , 2] = 0.107*demand_profiles.at[t, 'pv_veld_1_MW']
    
    net.sgen.iat[ 8 , 2] = demand_profiles.at[t, 'windmolen_3_MW']
    net.sgen.iat[ 9 , 2] = demand_profiles.at[t, 'windmolen_3_MW']
   
    net.sgen.iat[ 10 , 2] = 0.2113*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 11 , 2] = 0.3368*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 12 , 2] = 0.1231*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 13 , 2] = 0.2322*demand_profiles.at[t, 'pv_veld_1_MW']
     
    pp.runpp(net, max_iteration=10000)
    
    
    
    
    #######################################################################   Diagnostiek   #######################################################
    
    #energiegebruik = energiegebruik + net.res_load['p_mw'].sum()      ### voor het berekenen ven het totale energiegebruik, somt alle lasten.
    
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
print (totale_kwadratensom)