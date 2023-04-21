# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 09:24:42 2023

@author: battuejd
"""

import pandapower as pp
import load_usp_grid_simple_north as lugn
import pandas as pd


lugn
net = lugn.net
demand_profiles = lugn.demand_profiles


df1 = pd.read_csv('results_s2_north_1')
df2 = pd.read_csv('results_s2_north_2')
df3 = pd.read_csv('results_s2_north_3')
df4 = pd.read_csv('results_s2_north_4')


frames = [df1, df2, df3, df4]
df = pd.concat(frames)


df_final = df[df['max_line_loading'] > 100]
df_final.switches = df_final.switches.apply(eval)


totale_kwadratensom = 0
overbelastingsuren = 0
i = list(df_final.index)


def kwadrateren(x):
    x = x - 100
    x = x * x
    return x


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
    
    result = net.res_line[net.res_line['loading_percent'] > 100.000]
    print(result.loading_percent)
    
    totale_kwadratensom = totale_kwadratensom + sum(result.loading_percent.apply(kwadrateren))
    
    
    