# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:02:31 2023

@author: battuejd
"""

import pandapower as pp
import pandapower.plotting as plot
import pandapower.topology as top
import load_usp_grid_simple_south as lugs
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
import matplotlib as mpl
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['font.size'] = 18
mpl.rcParams['legend.fontsize'] = 14


lugs

net = lugs.net
sw = pd.read_csv('sw_south.csv')
demand_profiles = lugs.demand_profiles

sw_valid = sw[sw.valid]
sw_valid = sw_valid.reset_index()
sw_valid = sw_valid.switches


def test_switching_state(par):
    net.switch.closed = True
    net.switch.closed.loc[par] = False
    print(net.switch.closed)
    pp.runpp(net)
    line_loading_valid = (net.res_line.loading_percent < 50).all()
    
    return pd.Series({"switches": par, "max_line_loading": net.res_line.loading_percent.max(), "is_valid": line_loading_valid})
    

def simulate_timestep(net, sw_valid):
    results = sw_valid.apply(test_switching_state)
    valid_results = results[results.is_valid]
    
    return valid_results.iloc[valid_results.max_line_loading.idxmin()]

# moet line loadings zijn






def run_timeseries(net, sw, demand_profiles):   
    results = dict()
    for t, step in demand_profiles.iterrows():
        print("Timestep %s" % t)
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
        results[t] = simulate_timestep(net, sw)
        print(t, ' uit 99 volbracht')
    return pd.DataFrame(results).T


results = run_timeseries(net, sw, demand_profiles)


results.head()
