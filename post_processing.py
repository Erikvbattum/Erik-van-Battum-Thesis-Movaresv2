# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:23:18 2023

@author: battuejd
"""


import pandapower as pp
import load_usp_grid_simple_south as lugs
import pandas as pd


lugs
net = lugs.net
demand_profiles = lugs.demand_profiles


df1 = pd.read_csv('results_s2_south_1')
df2 = pd.read_csv('results_s2_south_2')


frames = [df1, df2]
df = pd.concat(frames)


df_final = df[df['max_line_loading'] > 100]
df_final.switches = df_final.switches.apply(eval)


totale_kwadratensom = 0
overbelastingsuren = 0
i = list(df_final.index)


for t in i:

    
    t = t + 1

    
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
    
    
    
    net.switch.closed = True
    net.switch.closed[df_final.loc[(t-1), 'switches']] = False
    pp.runpp(net)
    
    result = net.res_line[net.res_line['loading_percent'] > 100]
    print(result.loading_percent)
    
    
    
    
    
    
    
    
    