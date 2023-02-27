# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 13:52:31 2023

@author: battuejd
"""

import pandapower as pp
import pandapower.plotting as plot
import pandapower.topology as top
import load_usp_grid_simple_north as lugn
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
import matplotlib as mpl
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['font.size'] = 18
mpl.rcParams['legend.fontsize'] = 14


lugn

net = lugn.net
sw = pd.read_csv('sw_north.csv')
demand_profiles = lugn.demand_profiles


def test_switching_state(par):
    net.switch.closed = True
    net.switch.closed.loc[par.switches] = False
    pp.runpp(net)
    line_loading_valid = (net.res_line.loading_percent < 50).all()
    
    return pd.Series({"switches": par.switches, "max_line_loading": net.res_line.loading_percent.max(), "is_valid": line_loading_valid})


def simulate_timestep(net, sw):
    results = sw[sw.valid].apply(test_switching_state, axis=1)
    results = results.reset_index()
    valid_results = results[results.is_valid]
    
    return valid_results.iloc[valid_results.max_line_loading.idxmin()]





def run_timeseries(net, sw, demand_profiles):   
    results = dict()
    for t, step in demand_profiles.iterrows():
        print("Timestep %s" % t)
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
        results[t] = simulate_timestep(net, sw)
        print(t, ' uit 8760 volbracht')
    return pd.DataFrame(results).T


results = run_timeseries(net, sw, demand_profiles)


results.head()
