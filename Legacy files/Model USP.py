# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:42:41 2022

@author: battuejd
"""

import pandas as pd
import pandapower as pp
from pandapower import plotting as plot
import load_usp_grid as lug




### Data Inladen ###

demand_profiles = pd.DataFrame(pd.read_excel('Input Data/Overzicht lasten en generatie.xlsx', 'profielen_1_dag', index_col=('Uur:')))

i = list(demand_profiles.index.values)

t = 1

energiegebruik = 0
totale_kwadratensom = 0
overbelastingsuren = 0

lug
net = lug.net


###   Niew net en model aanmaken en standaard kabeltypes ingeven   ###

# =============================================================================
# 
# 
# net = pp.create_empty_network()
# 
# 
# line_data_50_XLPE = {"c_nf_per_km": 260, "r_ohm_per_km": 0.387, "x_ohm_per_km": 0.138, "max_i_ka": 0.185, "type": "cs", "q_mm2": 50}
# pp.create_std_type(net, line_data_50_XLPE, "50_XLPE", element='line')
# 
# line_data_50 = {"c_nf_per_km": 260, "r_ohm_per_km": 0.385, "x_ohm_per_km": 0.138, "max_i_ka": 0.185, "type": "cs", "q_mm2": 50}
# pp.create_std_type(net, line_data_50, "50", element='line')
# 
# line_data_95 = {"c_nf_per_km": 330, "r_ohm_per_km" : 0.139, "x_ohm_per_km": 0.123, "max_i_ka": 0.270, "type": "cs", "q_mm2": 95}
# pp.create_std_type(net, line_data_95, "95", element='line')
# 
# line_data_95_XLPE = {"c_nf_per_km": 330, "r_ohm_per_km" : 0.139, "x_ohm_per_km": 0.123, "max_i_ka": 0.270, "type": "cs", "q_mm2": 95}
# pp.create_std_type(net, line_data_95, "95_XLPE", element='line')
# 
# line_data_95_AL_XLPE = {"c_nf_per_km": 310, "r_ohm_per_km": 0.320, "x_ohm_per_km": 0.134, "max_i_ka": 0.215, "type": "cs", "q_mm2": 95}
# pp.create_std_type(net, line_data_95_AL_XLPE, "95_AL_XLPE", element='line')
# 
# line_data_150_XLPE = {"c_nf_per_km": 390, "r_ohm_per_km": 0.124, "x_ohm_per_km": 0.114, "max_i_ka": 0.335, "type": "cs", "q_mm2": 150}
# pp.create_std_type(net, line_data_150_XLPE, "150_XLPE", element='line')
# 
# line_data_150_AL_XLPE = {"c_nf_per_km": 360, "r_ohm_per_km": 0.206, "x_ohm_per_km": 0.127, "max_i_ka": 0.280, "type": "cs", "q_mm2": 150}
# pp.create_std_type(net, line_data_150_AL_XLPE, "150_AL_XLPE", element='line')
# 
# line_data_240_AL_XLPE = {"c_nf_per_km": 440, "r_ohm_per_km": 0.125, "x_ohm_per_km": 0.118, "max_i_ka": 0.360, "type": "cs", "q_mm2": 240}
# pp.create_std_type(net, line_data_240_AL_XLPE, "240_AL_XLPE", element='line')
# 
# line_data_630_AL_XLPE = {"c_nf_per_km": 660, "r_ohm_per_km": 0.0469, "x_ohm_per_km": 0.103, "max_i_ka": 1.102, "type": "cs", "q_mm2": 630}
# pp.create_std_type(net, line_data_630_AL_XLPE, "630_AL_XLPE", element='line')
# 
# 
# 
# 
# 
# 
# ################################################################## Sorbonne busrail en de Bilt busrail ####################################################################
# 
# bus_sorbonne = pp.create_bus(net, vn_kv = 10., name = 'sorbonnelaan', type = 'b')
# 
# pp.create_ext_grid(net, bus_sorbonne,)
# 
# 
# 
# bus_deBilt = pp.create_bus(net, vn_kv = 10., name = 'deBilt', type = 'b')
# 
# pp.create_ext_grid(net, bus_deBilt,)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ############################################################### veld 208 & 217 (Oranje) ###########################################################################
# 
# 
# 
# 
# ###   BUSJES   ###
# 
# bus_4360 = pp.create_bus(net, vn_kv = 10., name = '4360', type = 'n')
# 
# bus_4359 = pp.create_bus(net, vn_kv = 10., name = '4359', type = 'n')
# 
# 
# 
# 
# ###   LIJNEN   ###
# 
# line_sorbonne_4360 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_4360, length_km=0.7, name='sorbonne_4360',std_type="630_AL_XLPE")
# 
# line_4360_4359 = pp.create_line(net, from_bus=bus_4360, to_bus=bus_4359, length_km=0.1, name='4359_4360',std_type="630_AL_XLPE")
# 
# line_4359_sorbonne = pp.create_line(net, from_bus=bus_4359, to_bus=bus_sorbonne, length_km=0.7, name='4359_sorbonne',std_type="630_AL_XLPE")
# 
# 
# 
# 
# ###   SCHAKELAARS   ###
# 
# switch_4360_101_var = True
# switch_4360_101 = pp.create_switch(net, bus_4360, line_sorbonne_4360, et='l', closed=switch_4360_101_var, type = 'LBS', name= '4360_101')
# 
# switch_4360_102_var = True
# switch_4360_102 = pp.create_switch(net, bus_4360, line_4360_4359, et='l', closed=switch_4360_102_var, type = 'LBS', name= '4360_102')
# 
# switch_4359_101_var = True
# switch_4359_101 = pp.create_switch(net, bus_4359, line_4360_4359, et='l', closed=switch_4359_101_var, type = 'LBS', name= '4359_101')
# 
# switch_4359_102_var = True
# switch_4359_102 = pp.create_switch(net, bus_4359, line_4359_sorbonne, et='l', closed=switch_4359_102_var, type = 'LBS', name= '4359_102')
# 
# 
# 
# 
# ###   LASTEN EN PRODUCTIE   ###
# 
# pp.create_load(net, bus=bus_4360, p_mw=10.0*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_4360")
# 
# pp.create_load(net, bus=bus_4359, p_mw=10.0*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_4359")
# 
# 
# 
# 
# ###################################################################### veld 211 & 222 (Geel) ########################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_4665 = pp.create_bus(net, vn_kv = 10., name = '4665', type = 'n')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_4665_k1 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_4665, length_km=1.6, name='sorbonne_4665_k1',std_type="240_AL_XLPE")
# 
# line_sorbonne_4665_k2 = pp.create_line(net, from_bus=bus_4665, to_bus=bus_sorbonne, length_km=1.6, name='sorbonne_4665_k2',std_type="240_AL_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_4665_101_var = True
# switch_4665_101 = pp.create_switch(net, bus_4665, line_sorbonne_4665_k1, et='l', closed=switch_4665_101_var, type = 'LBS', name= '4665_101')
# 
# switch_4665_102_var = True
# switch_4665_102 = pp.create_switch(net, bus_4665, line_sorbonne_4665_k2, et='l', closed=switch_4665_102_var, type = 'LBS', name= '4665_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_4665, p_mw=3.0*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_4665")
# 
# 
# 
# 
# ############################################################################ veld 122 & 214 (Paars) ####################################################################
# 
# 
# 
# ###   Busjes   ###
# 
# bus_8515 = pp.create_bus(net, vn_kv = 10., name = '8515', type = 'b')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_8515_k1 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_8515, length_km=1.7, name='sorbonne_8515_k1',std_type="240_AL_XLPE")
# 
# line_sorbonne_8515_k2 = pp.create_line(net, from_bus=bus_8515, to_bus=bus_sorbonne, length_km=1.7, name='sorbonne_8515_k2',std_type="240_AL_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_8515_101_var = True
# switch_8515_101 = pp.create_switch(net, bus_8515, line_sorbonne_8515_k1, et='l', closed=switch_8515_101_var, type = 'LBS', name= '8515_101')
# 
# switch_8515_102_var = True
# switch_8515_102 = pp.create_switch(net, bus_8515, line_sorbonne_8515_k2, et='l', closed=switch_8515_102_var, type = 'LBS', name= '8515_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_8515, p_mw=3.0*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_8515")
# 
# 
# 
# 
# ################################################################### veld 104 & 107 & 130 (naar WKC) (Grijs) ###################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84460 = pp.create_bus(net, vn_kv = 10., name = '84460', type = 'b')
# 
# bus_84460_2 = pp.create_bus(net, vn_kv = 10., name = '84460_2', type = 'b')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_84460_k1 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84460, length_km=1.6, name='sorbonne_84460_k1',std_type="630_AL_XLPE")
# 
# line_sorbonne_84460_k2 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84460, length_km=1.6, name='sorbonne_84460_k2',std_type="630_AL_XLPE")
# 
# line_sorbonne_84460_k3 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84460, length_km=1.6, name='sorbonne_84460_k3',std_type="630_AL_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84460_111_var = True
# switch_84460_111 = pp.create_switch(net, bus_84460, line_sorbonne_84460_k1, et='l', closed=switch_84460_111_var, type = 'LBS', name= '84460_111')
# 
# switch_84460_110_var = True
# switch_84460_110 = pp.create_switch(net, bus_84460, line_sorbonne_84460_k2, et='l', closed=switch_84460_110_var, type = 'LBS', name= '84460_110')
# 
# switch_84460_109_var = True
# switch_84460_109 = pp.create_switch(net, bus_84460, line_sorbonne_84460_k3, et='l', closed=switch_84460_109_var, type = 'LBS', name= '84460_109')
# 
# 
# 
# switch_84460_2_var = True
# switch_84460_2 = pp.create_switch(net, bus_84460, bus_84460_2, et='b', closed=switch_84460_2_var, type = 'LBS', name= '84460_2')
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# 
# 
# 
# 
# 
# ###################################################################### veld 84460_2 205 (Jenalaan WKC) (Lichtgroen) ###############################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_4516 = pp.create_bus(net, vn_kv = 10., name = '4516', type = 'n')
# 
# bus_4738 = pp.create_bus(net, vn_kv = 10., name = '4738', type = 'n')
# 
# bus_84432 = pp.create_bus(net, vn_kv = 10., name = '84432', type = 'n')
# 
# 
# 
# bus_zonpv_zuidoost = pp.create_bus(net, vn_kv = 10., name = 'zonpv_zuidoost', type = 'n')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_84460_2_4516 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_4516, length_km=0.1, name='84460_2_4516',std_type="95_AL_XLPE")
# 
# line_4516_4738 = pp.create_line(net, from_bus=bus_4516, to_bus=bus_4738, length_km=0.1, name='4516_4738',std_type="50_XLPE")
# 
# line_4738_84432 = pp.create_line(net, from_bus=bus_4738, to_bus=bus_84432, length_km=0.1, name='4738_84432',std_type="50_XLPE")
# 
# 
# 
# line_zonpv_zuidoost = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_zonpv_zuidoost, length_km=1.5, name='zonpv_zuidoost',std_type="630_AL_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84460_205_var = True
# switch_84460_205 = pp.create_switch(net, bus_84460_2, line_84460_2_4516, et='l', closed=switch_84460_205_var, type = 'LBS', name= '84460_205')
# 
# switch_4516_102_var = True
# switch_4516_102 = pp.create_switch(net, bus_4516, line_84460_2_4516, et='l', closed=switch_84460_110_var, type = 'LBS', name= '4516_102')
# 
# switch_4516_101_var = True
# switch_4516_101 = pp.create_switch(net, bus_4516, line_4516_4738, et='l', closed=switch_4516_101_var, type = 'LBS', name= '4516_101')
# 
# switch_4738_101_var = True
# switch_4738_101 = pp.create_switch(net, bus_4738, line_4516_4738, et='l', closed=switch_4738_101_var, type = 'LBS', name= '4738_101')
# 
# switch_4738_102_var = True
# switch_4738_102 = pp.create_switch(net, bus_4738, line_4738_84432, et='l', closed=switch_4738_102_var, type = 'LBS', name= '4738_102')
# 
# switch_84432_101_var = True
# switch_84432_101 = pp.create_switch(net, bus_84432, line_4738_84432, et='l', closed=switch_84432_101_var, type = 'LBS', name= '84432_101')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_4516, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_4516")
# 
# pp.create_load(net, bus=bus_4738, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_4738")
# 
# pp.create_load(net, bus=bus_84432, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84432")
# 
# pp.create_load(net, bus=bus_84432, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84432_2")
# 
# 
# 
# 
# pp.create_load(net, bus=bus_84432, p_mw=0.60*demand_profiles.at[t, 'ev_simpel'], q_mvar=0.05, name="Load_ev_84432")
# 
# 
# 
# 
# pp.create_gen(net, bus=bus_4738, p_mw=0.1312*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_4738', vm_pu=1.0, controllable=False)  #tolakker jongveestal
# 
# pp.create_gen(net, bus=bus_84432, p_mw=0.2862*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84432', vm_pu=1.0, controllable=False)  #dak Martinud g de bruingebouw
# 
# pp.create_gen(net, bus=bus_84432, p_mw=0.0499*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84432_2', vm_pu=1.0, controllable=False)  #pv carport er naast
# 
# pp.create_gen(net, bus=bus_zonpv_zuidoost, p_mw=2*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_dak+carports_zuidoost', vm_pu=1.0, controllable=False) #dakpv 1,3mw + een stuk solarcarports er naast (bij tolakker)
# 
# pp.create_gen(net, bus=bus_4738, p_mw=0.1576*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_4738_2', vm_pu=1.0, controllable=False)  #tolakker rundveestal
# 
# pp.create_gen(net, bus=bus_zonpv_zuidoost, p_mw=9*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_9mwweide_zuidoost', vm_pu=1.0, controllable=False) #1 deel van de 10.5ha 12.5mw nature inclusive pv fields (andere deel op veldje tussen cambridgeflat en rivm in)
# 
# 
# 
# 
# 
# ###################################################################### veld 84460_2 204 (Jenalaan WKC) (Lichtblauw) ###############################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84429_1 = pp.create_bus(net, vn_kv = 10., name = '84429_1', type = 'b')
# 
# bus_84429_2 = pp.create_bus(net, vn_kv = 10., name = '84429_2', type = 'b')
# 
# bus_84427 = pp.create_bus(net, vn_kv = 10., name = '84427', type = 'n')
# 
# bus_84428 = pp.create_bus(net, vn_kv = 10., name = '84428', type = 'n')
# 
# bus_84453_2 = pp.create_bus(net, vn_kv = 10., name = '84453_2', type = 'b')
# 
# bus_84453_1 = pp.create_bus(net, vn_kv = 10., name = '84453_1', type = 'b')
# 
# bus_84495 = pp.create_bus(net, vn_kv = 10., name = '84495', type = 'n')
# 
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_84460_2_84429_1 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_84429_1, length_km=0.1, name='84460_2_84429_1',std_type="95_AL_XLPE")
# 
# line_84429_1_84432 = pp.create_line(net, from_bus=bus_84429_1, to_bus=bus_84432, length_km=0.1, name='84429_1_84432',std_type="50_XLPE")
# 
# line_84429_2_84427 = pp.create_line(net, from_bus=bus_84429_2, to_bus=bus_84427, length_km=0.1, name='84429_2_84427',std_type="50_XLPE")
# 
# line_84427_84428 = pp.create_line(net, from_bus=bus_84427, to_bus=bus_84428, length_km=0.1, name='84427_84428',std_type="50")
# 
# line_84428_84453_2 = pp.create_line(net, from_bus=bus_84428, to_bus=bus_84453_2, length_km=0.1, name='84428_84453_2',std_type="150_AL_XLPE")
# 
# line_84453_1_84495 = pp.create_line(net, from_bus=bus_84453_1, to_bus=bus_84495, length_km=0.1, name='84453_1_84495',std_type="95_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84429_102_var = True
# switch_84429_102 = pp.create_switch(net, bus_84429_1, line_84460_2_84429_1, et='l', closed=switch_84429_102_var, type = 'LBS', name= '84429_102')
# 
# switch_84429_101_var = True  ##### sectoropening?
# switch_84429_101 = pp.create_switch(net, bus_84429_1, line_84429_1_84432, et='l', closed=switch_84429_101_var, type = 'LBS', name= '84429_101')
# 
# switch_84432_102_var = True
# switch_84432_102 = pp.create_switch(net, bus_84432, line_84429_1_84432, et='l', closed=switch_84432_102_var, type = 'LBS', name= '84432_102')
# 
# switch_84429_202_var = True
# switch_84429_202 = pp.create_switch(net, bus_84429_2, line_84429_2_84427, et='l', closed=switch_84429_202_var, type = 'LBS', name= '84429_202')
# 
# switch_84427_101_var = True
# switch_84427_101 = pp.create_switch(net, bus_84427, line_84429_2_84427, et='l', closed=switch_84427_101_var, type = 'LBS', name= '84427_101')
# 
# switch_84427_102_var = True
# switch_84427_102 = pp.create_switch(net, bus_84427, line_84427_84428, et='l', closed=switch_84427_102_var, type = 'LBS', name= '84427_102')
# 
# switch_84428_101_var = True
# switch_84428_101 = pp.create_switch(net, bus_84428, line_84427_84428, et='l', closed=switch_84428_101_var, type = 'LBS', name= '84428_101')
# 
# switch_84428_102_var = True
# switch_84428_102 = pp.create_switch(net, bus_84428, line_84428_84453_2, et='l', closed=switch_84428_102_var, type = 'LBS', name= '84428_102')
# 
# switch_84453_101_var = True
# switch_84453_101 = pp.create_switch(net, bus_84453_1, line_84453_1_84495, et='l', closed=switch_84453_101_var, type = 'LBS', name= '84453_101')
# 
# switch_84495_101_var = True
# switch_84495_101 = pp.create_switch(net, bus_84495, line_84453_1_84495, et='l', closed=switch_84495_101_var, type = 'LBS', name= '84495_101')
# 
# 
# 
# switch_84429_103_var = True
# switch_84429_103 = pp.create_switch(net, bus_84429_1, bus_84429_2, et='b', closed=switch_84429_103_var, type = 'LBS', name= '84429_103')
# 
# switch_84453_102_var = True
# switch_84453_102 = pp.create_switch(net, bus_84453_1, bus_84453_2, et='b', closed=switch_84453_102_var, type = 'LBS', name= '84453_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84429_2, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84429")
# 
# pp.create_load(net, bus=bus_84429_2, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84429_2")
# 
# pp.create_load(net, bus=bus_84427, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84427")
# 
# pp.create_load(net, bus=bus_84428, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84428")
# 
# pp.create_load(net, bus=bus_84428, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84428_2")
# 
# pp.create_load(net, bus=bus_84453_2, p_mw=1.00*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84453_2")
# 
# pp.create_load(net, bus=bus_84453_1, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84453_1")
# 
# pp.create_load(net, bus=bus_84453_1, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84453_1_2")
# 
# pp.create_load(net, bus=bus_84495, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84495")
# 
# pp.create_load(net, bus=bus_84495, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84495_2")
# 
# 
# 
# 
# pp.create_gen(net, bus=bus_84429_1, p_mw=0.2333*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84429_1', vm_pu=1.0, controllable=False)
# 
# pp.create_gen(net, bus=bus_84427, p_mw=0.107*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84427', vm_pu=1.0, controllable=False)
# 
# 
# 
# ###################################################################### veld 84460_2 202 (Jenalaan WKC) (Donkergroen) ###############################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84434 = pp.create_bus(net, vn_kv = 10., name = '84434', type = 'n')
# 
# bus_84467 = pp.create_bus(net, vn_kv = 10., name = '84467', type = 'n')
# 
# bus_84498 = pp.create_bus(net, vn_kv = 10., name = '84498', type = 'n')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_84460_2_84434 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_84434, length_km=0.4, name='84460_2_84434',std_type="150_XLPE")
# 
# line_84434_84495 = pp.create_line(net, from_bus=bus_84434, to_bus=bus_84495, length_km=0.1, name='84434_84495',std_type="50_XLPE")
# 
# line_84434_84467 = pp.create_line(net, from_bus=bus_84434, to_bus=bus_84467, length_km=0.1, name='84434_84467',std_type="50_XLPE")
# 
# line_84467_84498 = pp.create_line(net, from_bus=bus_84467, to_bus=bus_84498, length_km=0.1, name='84467_84498',std_type="50_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84460_202_var = True
# switch_84460_202 = pp.create_switch(net, bus_84460_2, line_84460_2_84434, et='l', closed=switch_84460_202_var, type = 'LBS', name= '84460_202')
# 
# switch_84434_103_var = True
# switch_84434_103 = pp.create_switch(net, bus_84434, line_84460_2_84434, et='l', closed=switch_84434_103_var, type = 'LBS', name= '84434_103')
# 
# switch_84434_101_var = True   ### Sectoropening??
# switch_84434_101 = pp.create_switch(net, bus_84434, line_84434_84495, et='l', closed=switch_84434_101_var, type = 'LBS', name= '84434_101')
# 
# switch_84434_102_var = True
# switch_84434_102 = pp.create_switch(net, bus_84434, line_84434_84467, et='l', closed=switch_84434_102_var, type = 'LBS', name= '84434_102')
# 
# switch_84467_101_var = True
# switch_84467_101 = pp.create_switch(net, bus_84467, line_84434_84467, et='l', closed=switch_84467_101_var, type = 'LBS', name= '84467_101')
# 
# switch_84467_102_var = True
# switch_84467_102 = pp.create_switch(net, bus_84467, line_84467_84498, et='l', closed=switch_84467_102_var, type = 'LBS', name= '84467_102')
# 
# switch_84498_101_var = True
# switch_84498_101 = pp.create_switch(net, bus_84498, line_84467_84498, et='l', closed=switch_84498_101_var, type = 'LBS', name= '84498_101')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84434, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84434")
# 
# pp.create_load(net, bus=bus_84434, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84434_2")
# 
# pp.create_load(net, bus=bus_84467, p_mw=1.00*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84467")
# 
# pp.create_load(net, bus=bus_84498, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84498")
# 
# 
# 
# 
# ###################################################################### veld 84460_2 203 (Jenalaan WKC) (Donkerblauw) ###############################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84447 = pp.create_bus(net, vn_kv = 10., name = '84447', type = 'n')
# 
# bus_84443_1 = pp.create_bus(net, vn_kv = 10., name = '84443_1', type = 'b')
# 
# bus_84443_2 = pp.create_bus(net, vn_kv = 10., name = '84443_2', type = 'b')
# 
# bus_84417 = pp.create_bus(net, vn_kv = 10., name = '84417', type = 'n')
# 
# bus_4898 = pp.create_bus(net, vn_kv = 10., name = '4898', type = 'n')
# 
# bus_84481 = pp.create_bus(net, vn_kv = 10., name = '84481', type = 'n')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_84460_2_84447 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_84447, length_km=0.7, name='84460_2_84447',std_type="50_XLPE")
# 
# line_84447_84443_1 = pp.create_line(net, from_bus=bus_84447, to_bus=bus_84443_1, length_km=0.6, name='84447_84443_1',std_type="50_XLPE")
# 
# line_84443_2_84417 = pp.create_line(net, from_bus=bus_84443_2, to_bus=bus_84417, length_km=0.5, name='84443_2_84417',std_type="50")
# 
# line_84417_4898 = pp.create_line(net, from_bus=bus_84417, to_bus=bus_4898, length_km=0.1, name='84417_4898',std_type="50_XLPE")
# 
# line_4898_84481 = pp.create_line(net, from_bus=bus_4898, to_bus=bus_84481, length_km=0.1, name='4898_84481',std_type="50_XLPE")
# 
# line_84481_84498 = pp.create_line(net, from_bus=bus_84481, to_bus=bus_84498, length_km=0.9, name='84481_84498',std_type="50")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84460_203_var = True
# switch_84460_203 = pp.create_switch(net, bus_84460_2, line_84460_2_84447, et='l', closed=switch_84460_203_var, type = 'LBS', name= '84460_203')
# 
# switch_84447_101_var = True
# switch_84447_101 = pp.create_switch(net, bus_84447, line_84460_2_84447, et='l', closed=switch_84447_101_var, type = 'LBS', name= '84447_101')
# 
# switch_84447_102_var = True
# switch_84447_102 = pp.create_switch(net, bus_84447, line_84447_84443_1, et='l', closed=switch_84447_102_var, type = 'LBS', name= '84447_102')
# 
# switch_84443_101_var = True
# switch_84443_101 = pp.create_switch(net, bus_84443_1, line_84447_84443_1, et='l', closed=switch_84443_101_var, type = 'LBS', name= '84443_101')
# 
# switch_84443_203_var = True
# switch_84443_203 = pp.create_switch(net, bus_84443_2, line_84443_2_84417, et='l', closed=switch_84443_203_var, type = 'LBS', name= '84443_203')
# 
# switch_84417_101_var = True
# switch_84417_101 = pp.create_switch(net, bus_84417, line_84443_2_84417, et='l', closed=switch_84417_101_var, type = 'LBS', name= '84417_101')
# 
# switch_84417_102_var = True
# switch_84417_102 = pp.create_switch(net, bus_84417, line_84417_4898, et='l', closed=switch_84417_102_var, type = 'LBS', name= '84417_102')
# 
# switch_4898_101_var = True
# switch_4898_101 = pp.create_switch(net, bus_4898, line_84417_4898, et='l', closed=switch_4898_101_var, type = 'LBS', name= '4898_101')
# 
# switch_4898_102_var = True
# switch_4898_102 = pp.create_switch(net, bus_4898, line_4898_84481, et='l', closed=switch_4898_102_var, type = 'LBS', name= '4898_102')
# 
# switch_84481_101_var = True
# switch_84481_101 = pp.create_switch(net, bus_84481, line_4898_84481, et='l', closed=switch_84481_101_var, type = 'LBS', name= '84481_101')
# 
# switch_84481_102_var = True   ### sectoropening?
# switch_84481_102 = pp.create_switch(net, bus_84481, line_84481_84498, et='l', closed=switch_84481_102_var, type = 'LBS', name= '84481_102')
# 
# 
# 
# switch_84443_102_var = True
# switch_84443_102 = pp.create_switch(net, bus_84443_1, bus_84443_2, et='b', closed=switch_84443_102_var, type = 'LBS', name= '84443_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84447, p_mw=0.10*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84447")
# 
# pp.create_load(net, bus=bus_84443_1, p_mw=0.60*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84443_1")
# 
# pp.create_load(net, bus=bus_84443_1, p_mw=0.30*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84443_1_2")
# 
# pp.create_load(net, bus=bus_84417, p_mw=0.315*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84417")  #achterin de botu, windmolens kunne ook aan 84481
# 
# pp.create_load(net, bus=bus_4898, p_mw=1.00*0.5, q_mvar=0.05, name="Load_4898")    #Parkeergarage, aangenomen constante vermogensvraag op halve capaciteit.
# 
# pp.create_load(net, bus=bus_84481, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84481")
# 
# 
# 
# pp.create_load(net, bus=bus_4898, p_mw=0.2*demand_profiles.at[t, 'ev_simpel'], q_mvar=0.05, name="ev_4898") #200 laadpalen
# 
# 
# bus_wind = pp.create_bus(net, vn_kv = 10., name = 'bus_wind', type = 'n')
# line_wind = pp.create_line(net, from_bus=bus_wind, to_bus=bus_sorbonne, length_km=0.9, name='lijn_wind',std_type="630_AL_XLPE")
# pp.create_gen(net, bus=bus_wind, p_mw=demand_profiles.at[t, 'windmolen_3_MW'], name='windmolen_1', vm_pu=1.0, controllable=False)
# pp.create_gen(net, bus=bus_wind, p_mw=demand_profiles.at[t, 'windmolen_3_MW'], name='windmolen_2', vm_pu=1.0, controllable=False)
# 
# pp.create_gen(net, bus=bus_84443_1, p_mw=0.2113*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84443_1', vm_pu=1.0, controllable=False)  #dak Ruppert
# 
# pp.create_gen(net, bus=bus_4898, p_mw=0.3368*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_4898', vm_pu=1.0, controllable=False) #parkeergarage olympos
# 
# 
# 
# 
# 
# ###################################################################### veld 84460_2 206 (Jenalaan WKC) (Rood) ###############################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_8193 = pp.create_bus(net, vn_kv = 10., name = '8193', type = 'n')
# 
# bus_8194 = pp.create_bus(net, vn_kv = 10., name = '8194', type = 'n')
# 
# bus_8195 = pp.create_bus(net, vn_kv = 10., name = '8195', type = 'n')
# 
# bus_84494_3 = pp.create_bus(net, vn_kv = 10., name = '84494_3', type = 'b')
# 
# bus_84494_2 = pp.create_bus(net, vn_kv = 10., name = '84494_2', type = 'b')
# 
# bus_84494_1 = pp.create_bus(net, vn_kv = 10., name = '84494_1', type = 'b')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_84460_2_8193 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_8193, length_km=1.0, name='84460_2_8193',std_type="240_AL_XLPE")
# 
# line_8193_8194 = pp.create_line(net, from_bus=bus_8193, to_bus=bus_8194, length_km=0.1, name='8193_8194',std_type="240_AL_XLPE")
# 
# line_8194_8195 = pp.create_line(net, from_bus=bus_8194, to_bus=bus_8195, length_km=0.1, name='8194_8195',std_type="240_AL_XLPE")
# 
# line_8195_84494_3 = pp.create_line(net, from_bus=bus_8195, to_bus=bus_84494_3, length_km=0.4, name='8195_84494_3',std_type="240_AL_XLPE")
# 
# line_84494_1_84443_2 = pp.create_line(net, from_bus=bus_84494_1, to_bus=bus_84443_2, length_km=0.3, name='84494_1_84443_2',std_type="50_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84460_206_var = True
# switch_84460_206 = pp.create_switch(net, bus_84460_2, line_84460_2_8193, et='l', closed=switch_84460_206_var, type = 'LBS', name= '84460_206')
# 
# switch_8193_101_var = True
# switch_8193_101 = pp.create_switch(net, bus_8193, line_84460_2_8193, et='l', closed=switch_8193_101_var, type = 'LBS', name= '8193_101')
# 
# switch_8193_102_var = True
# switch_8193_102 = pp.create_switch(net, bus_8193, line_8193_8194, et='l', closed=switch_8193_102_var, type = 'LBS', name= '8193_102')
# 
# switch_8194_101_var = True
# switch_8194_101 = pp.create_switch(net, bus_8194, line_8193_8194, et='l', closed=switch_8194_101_var, type = 'LBS', name= '8194_101')
# 
# switch_8194_102_var = True
# switch_8194_102 = pp.create_switch(net, bus_8194, line_8194_8195, et='l', closed=switch_8194_102_var, type = 'LBS', name= '8194_102')
# 
# switch_8195_101_var = True
# switch_8195_101 = pp.create_switch(net, bus_8195, line_8194_8195, et='l', closed=switch_8195_101_var, type = 'LBS', name= '8195_101')
# 
# switch_8195_102_var = True
# switch_8195_102 = pp.create_switch(net, bus_8195, line_8195_84494_3, et='l', closed=switch_8195_102_var, type = 'LBS', name= '8195_102')
# 
# switch_84494_301_var = True
# switch_84494_301 = pp.create_switch(net, bus_84494_3, line_8195_84494_3, et='l', closed=switch_84494_301_var, type = 'LBS', name= '84494_301')
# 
# switch_84494_101_var = True
# switch_84494_101 = pp.create_switch(net, bus_84494_1, line_84494_1_84443_2, et='l', closed=switch_84494_101_var, type = 'LBS', name= '84494_101')
# 
# switch_84443_202_var = True   ### sectoropening
# switch_84443_202 = pp.create_switch(net, bus_84443_2, line_84494_1_84443_2, et='l', closed=switch_84443_202_var, type = 'LBS', name= '84443_202')
# 
# 
# 
# switch_84494_201_var = True
# switch_84494_201 = pp.create_switch(net, bus_84494_2, bus_84494_3, et='b', closed=switch_84494_201_var, type = 'LBS', name= '84494_201')
# 
# switch_84494_102_var = True
# switch_84494_102 = pp.create_switch(net, bus_84494_1, bus_84494_2, et='b', closed=switch_84494_102_var, type = 'LBS', name= '84494_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_8193, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_8193")
# 
# pp.create_load(net, bus=bus_8194, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_8194")
# 
# pp.create_load(net, bus=bus_8195, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_8195")
# 
# pp.create_load(net, bus=bus_84494_2, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84494_2")
# 
# pp.create_load(net, bus=bus_84494_2, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84494_2_2")
# 
# pp.create_load(net, bus=bus_84494_1, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84494_1")
# 
# 
# 
# 
# pp.create_gen(net, bus=bus_8193, p_mw=0.1231*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_8193', vm_pu=1.0, controllable=False)
# 
# pp.create_gen(net, bus=bus_84494_1, p_mw=0.2322*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84494_1', vm_pu=1.0, controllable=False)
# 
# 
# 
# 
# ###################################################################### veld 119 (Roze) ###############################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_1884 = pp.create_bus(net, vn_kv = 10., name = '1884', type = 'n')
# 
# bus_84474 = pp.create_bus(net, vn_kv = 10., name = '84474', type = 'n')
# 
# bus_2354 = pp.create_bus(net, vn_kv = 10., name = '2354', type = 'n')
# 
# bus_84446 = pp.create_bus(net, vn_kv = 10., name = '84446', type = 'n')
# 
# bus_84483 = pp.create_bus(net, vn_kv = 10., name = '84483', type = 'n')
# 
# bus_1834 = pp.create_bus(net, vn_kv = 10., name = '1834', type = 'n')
# 
# bus_3406 = pp.create_bus(net, vn_kv = 10., name = '3406', type = 'n')
# 
# bus_84499 = pp.create_bus(net, vn_kv = 10., name = '84499', type = 'n')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_1884 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_1884, length_km=0.3, name='sorbonne_1884',std_type="150_XLPE")
# 
# line_1884_84474 = pp.create_line(net, from_bus=bus_1884, to_bus=bus_84474, length_km=0.6, name='1884_84474',std_type="150_XLPE")
# 
# line_84474_2354 = pp.create_line(net, from_bus=bus_84474, to_bus=bus_2354, length_km=0.3, name='84474_2354',std_type="150_XLPE")
# 
# line_2354_84446 = pp.create_line(net, from_bus=bus_2354, to_bus=bus_84446, length_km=0.2, name='2354_84446',std_type="150_XLPE")
# 
# line_84446_84483 = pp.create_line(net, from_bus=bus_84446, to_bus=bus_84483, length_km=0.1, name='84446_84483',std_type="150_XLPE")
# 
# line_84483_1834 = pp.create_line(net, from_bus=bus_84483, to_bus=bus_1834, length_km=0.1, name='84483_1834',std_type="150_XLPE")
# 
# line_1834_3406 = pp.create_line(net, from_bus=bus_1834, to_bus=bus_3406, length_km=0.1, name='1834_3406',std_type="150_XLPE")
# 
# line_3406_84499 = pp.create_line(net, from_bus=bus_3406, to_bus=bus_84499, length_km=0.1, name='3406_84499',std_type="150_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_1884_101_var = True
# switch_1884_101 = pp.create_switch(net, bus_1884, line_sorbonne_1884, et='l', closed=switch_1884_101_var, type = 'LBS', name= '1884_101')
# 
# switch_1884_102_var = True
# switch_1884_102 = pp.create_switch(net, bus_1884, line_1884_84474, et='l', closed=switch_1884_102_var, type = 'LBS', name= '1884_102')
# 
# switch_84474_102_var = True
# switch_84474_102 = pp.create_switch(net, bus_84474, line_1884_84474, et='l', closed=switch_84474_102_var, type = 'LBS', name= '84474_102')
# 
# switch_84474_101_var = True
# switch_84474_101 = pp.create_switch(net, bus_84474, line_84474_2354, et='l', closed=switch_84474_101_var, type = 'LBS', name= '84474_101')
# 
# switch_2354_102_var = True
# switch_2354_102 = pp.create_switch(net, bus_2354, line_84474_2354, et='l', closed=switch_2354_102_var, type = 'LBS', name= '2354_102')
# 
# switch_2354_101_var = True
# switch_2354_101 = pp.create_switch(net, bus_2354, line_2354_84446, et='l', closed=switch_2354_101_var, type = 'LBS', name= '2354_101')
# 
# switch_84446_101_var = True
# switch_84446_101 = pp.create_switch(net, bus_84446, line_2354_84446, et='l', closed=switch_84446_101_var, type = 'LBS', name= '84446_101')
# 
# switch_84446_102_var = True
# switch_84446_102 = pp.create_switch(net, bus_84446, line_84446_84483, et='l', closed=switch_84446_102_var, type = 'LBS', name= '84446_102')
# 
# switch_84483_101_var = True
# switch_84483_101 = pp.create_switch(net, bus_84483, line_84446_84483, et='l', closed=switch_84483_101_var, type = 'LBS', name= '84483_101')
# 
# switch_84483_102_var = True
# switch_84483_102 = pp.create_switch(net, bus_84483, line_84483_1834, et='l', closed=switch_84483_102_var, type = 'LBS', name= '84483_102')
# 
# switch_1834_101_var = True
# switch_1834_101 = pp.create_switch(net, bus_1834, line_84483_1834, et='l', closed=switch_1834_101_var, type = 'LBS', name= '1834_101')
# 
# switch_1834_102_var = True
# switch_1834_102 = pp.create_switch(net, bus_1834, line_1834_3406, et='l', closed=switch_1834_102_var, type = 'LBS', name= '1834_102')
# 
# switch_3406_101_var = True
# switch_3406_101 = pp.create_switch(net, bus_3406, line_1834_3406, et='l', closed=switch_3406_101_var, type = 'LBS', name= '3406_101')
# 
# switch_3406_102_var = True
# switch_3406_102 = pp.create_switch(net, bus_3406, line_3406_84499, et='l', closed=switch_3406_102_var, type = 'LBS', name= '3406_102')
# 
# switch_84499_102_var = True
# switch_84499_102 = pp.create_switch(net, bus_84499, line_3406_84499, et='l', closed=switch_84499_102_var, type = 'LBS', name= '84499_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_1884, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_1884")
# 
# pp.create_load(net, bus=bus_84474, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84474")
# 
# pp.create_load(net, bus=bus_2354, p_mw=1.60*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_2354")
# 
# pp.create_load(net, bus=bus_84446, p_mw=0.16*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84446")     #Bijgebouwtje riooldienst ofzo, misschien iets beters verzinnen
# 
# pp.create_load(net, bus=bus_84483, p_mw=(demand_profiles.at[t, 'res_1']/14.5)*0.63, q_mvar=0.05, name="Load_84483")
# 
# pp.create_load(net, bus=bus_1834, p_mw=1.25*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_1834")
# 
# pp.create_load(net, bus=bus_3406, p_mw=1.60*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_3406")
# 
# pp.create_load(net, bus=bus_84499, p_mw=1.00*(demand_profiles.at[t, 'res_2']/14.5), q_mvar=0.05, name="Load_84499")
# 
# 
# bus_zonpv_rivmoost = pp.create_bus(net, vn_kv = 10., name = 'bus_zonpv_rivmoost', type = 'n')
# line_zonpv_rivmoost = pp.create_line(net, from_bus=bus_zonpv_rivmoost, to_bus=bus_sorbonne, length_km=0.3, name='lijn_zonpv_rivmoost',std_type="630_AL_XLPE")
# pp.create_gen(net, bus=bus_zonpv_rivmoost, p_mw=3.5*demand_profiles.at[t, 'pv_veld_1_MW'], name='zonpv_rivmoost', vm_pu=1.0, controllable=False) #1 deel van de 10.5ha 12.5mw nature inclusive pv fields (andere deel op oostelijke tolakkervelden)
# 
# 
# 
# 
# ################################################################################## veld 213 (Oranje) #########################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_8258 = pp.create_bus(net, vn_kv = 10., name = '8528', type = 'b')
# 
# bus_84426 = pp.create_bus(net, vn_kv = 10., name = '84426', type = 'n')
# 
# bus_8246 = pp.create_bus(net, vn_kv = 10., name = '8246', type = 'n')
# 
# bus_84489 = pp.create_bus(net, vn_kv = 10., name = '84489', type = 'n')
# 
# bus_8431 = pp.create_bus(net, vn_kv = 10., name = '8431', type = 'n')
# 
# bus_2596 = pp.create_bus(net, vn_kv = 10., name = '2596', type = 'n')
# 
# bus_7978 = pp.create_bus(net, vn_kv = 10., name = '7978', type = 'n')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_8258 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_8258, length_km=1.5, name='sorbonne_8258',std_type="240_AL_XLPE")
# 
# line_8258_84426 = pp.create_line(net, from_bus=bus_8258, to_bus=bus_84426, length_km=0.1, name='8258_84426',std_type="150_AL_XLPE")
# 
# line_84426_8246 = pp.create_line(net, from_bus=bus_84426, to_bus=bus_8246, length_km=0.1, name='84426_8246',std_type="150_AL_XLPE")
# 
# line_8246_84489 = pp.create_line(net, from_bus=bus_8246, to_bus=bus_84489, length_km=0.1, name='8246_84489',std_type="150_AL_XLPE")
# 
# line_84489_8258 = pp.create_line(net, from_bus=bus_84489, to_bus=bus_8258, length_km=0.1, name='84489_8258',std_type="150_AL_XLPE")
# 
# line_8258_8431 = pp.create_line(net, from_bus=bus_8258, to_bus=bus_8431, length_km=0.1, name='8258_8431',std_type="150_XLPE")
# 
# line_8431_2596 = pp.create_line(net, from_bus=bus_8431, to_bus=bus_2596, length_km=0.1, name='8431_2596',std_type="240_AL_XLPE")
# 
# line_2596_7978 = pp.create_line(net, from_bus=bus_2596, to_bus=bus_7978, length_km=0.6, name='2596_7978',std_type="150_XLPE")
# 
# line_7978_84499 = pp.create_line(net, from_bus=bus_7978, to_bus=bus_84499, length_km=0.2, name='7978_84499',std_type="240_AL_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_8258_102_var = True
# switch_8258_102 = pp.create_switch(net, bus_8258, line_sorbonne_8258, et='l', closed=switch_8258_102_var, type = 'LBS', name= '8258_102')
# 
# switch_8258_104_var = True
# switch_8258_104 = pp.create_switch(net, bus_8258, line_8258_84426, et='l', closed=switch_8258_104_var, type = 'LBS', name= '8258_104')
# 
# switch_84426_101_var = True
# switch_84426_101 = pp.create_switch(net, bus_84426, line_8258_84426, et='l', closed=switch_84426_101_var, type = 'LBS', name= '84426_101')
# 
# switch_84426_102_var = True
# switch_84426_102 = pp.create_switch(net, bus_84426, line_84426_8246, et='l', closed=switch_84426_102_var, type = 'LBS', name= '84426_102')
# 
# switch_8246_101_var = True
# switch_8246_101 = pp.create_switch(net, bus_8246, line_84426_8246, et='l', closed=switch_8246_101_var, type = 'LBS', name= '8246_101')
# 
# switch_8246_102_var = True
# switch_8246_102 = pp.create_switch(net, bus_8246, line_8246_84489, et='l', closed=switch_8246_102_var, type = 'LBS', name= '8246_102')
# 
# switch_84489_101_var = True  ##### Sectoropening?
# switch_84489_101 = pp.create_switch(net, bus_84489, line_8246_84489, et='l', closed=switch_84489_101_var, type = 'LBS', name= '84489_101')
# 
# switch_84489_102_var = True
# switch_84489_102 = pp.create_switch(net, bus_84489, line_84489_8258, et='l', closed=switch_84489_102_var, type = 'LBS', name= '84489_102')
# 
# switch_8258_105_var = True
# switch_8258_105 = pp.create_switch(net, bus_8258, line_84489_8258, et='l', closed=switch_8258_105_var, type = 'LBS', name= '8258_105')
# 
# switch_8258_101_var = True
# switch_8258_101 = pp.create_switch(net, bus_8258, line_8258_8431, et='l', closed=switch_8258_101_var, type = 'LBS', name= '8258_101')
# 
# switch_8431_101_var = True
# switch_8431_101 = pp.create_switch(net, bus_8431, line_8258_8431, et='l', closed=switch_8431_101_var, type = 'LBS', name= '8431_101')
# 
# switch_8431_102_var = True
# switch_8431_102 = pp.create_switch(net, bus_8431, line_8431_2596, et='l', closed=switch_8431_102_var, type = 'LBS', name= '8431_102')
# 
# switch_2596_101_var = True
# switch_2596_101 = pp.create_switch(net, bus_2596, line_8431_2596, et='l', closed=switch_2596_101_var, type = 'LBS', name= '2596_101')
# 
# switch_2596_102_var = True
# switch_2596_102 = pp.create_switch(net, bus_2596, line_2596_7978, et='l', closed=switch_2596_102_var, type = 'LBS', name= '2596_102')
# 
# switch_7978_102_var = True
# switch_7978_102 = pp.create_switch(net, bus_7978, line_2596_7978, et='l', closed=switch_7978_102_var, type = 'LBS', name= '7978_102')
# 
# switch_7978_101_var = True   ### sectoropening
# switch_7978_101 = pp.create_switch(net, bus_7978, line_7978_84499, et='l', closed=switch_7978_101_var, type = 'LBS', name= '7978_101')
# 
# switch_84499_101_var = True
# switch_84499_101 = pp.create_switch(net, bus_84499, line_7978_84499, et='l', closed=switch_84499_101_var, type = 'LBS', name= '84499_101')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84426, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84426")
# 
# pp.create_load(net, bus=bus_8246, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_8246")
# 
# pp.create_load(net, bus=bus_84489, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84489")
# 
# pp.create_load(net, bus=bus_84489, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84489_2")
# 
# pp.create_load(net, bus=bus_8431, p_mw=0.40*0.5, q_mvar=0.05, name="Load_8431")    #parkeergarage, ingesteld op constante afname op half vermogen
# 
# pp.create_load(net, bus=bus_2596, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_2596")
# 
# pp.create_load(net, bus=bus_7978, p_mw=0.630*(demand_profiles.at[t, 'res_2']/14.5), q_mvar=0.05, name="Load_7978")
# 
# 
# 
# 
# ################################################################################## veld 109 (Geel) #########################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84437 = pp.create_bus(net, vn_kv = 10., name = '84437', type = 'n')
# 
# bus_84436_3 = pp.create_bus(net, vn_kv = 10., name = '84436_3', type = 'b')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_84437 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84437, length_km=0.7, name='sorbonne_84437',std_type="150_AL_XLPE")
# 
# line_84437_84436_3 = pp.create_line(net, from_bus=bus_84437, to_bus=bus_84436_3, length_km=0.1, name='84437_84436_3',std_type="95")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84437_101_var = True
# switch_84437_101 = pp.create_switch(net, bus_84437, line_sorbonne_84437, et='l', closed=switch_84437_101_var, type = 'LBS', name= '84437_101')
# 
# switch_84437_102_var = True
# switch_84437_102 = pp.create_switch(net, bus_84437, line_84437_84436_3, et='l', closed=switch_84437_102_var, type = 'LBS', name= '84437_102')
# 
# switch_84436_304_var = True
# switch_84436_304 = pp.create_switch(net, bus_84436_3, line_84437_84436_3, et='l', closed=switch_84436_304_var, type = 'LBS', name= '84436_304')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84437, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84437")
# 
# pp.create_load(net, bus=bus_84436_3, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84436_3")
# 
# 
# 
# bus_zonpv_rivmnoord = pp.create_bus(net, vn_kv = 10., name = 'bus_zonpv_rivmnoord', type = 'n')
# line_zonpv_rivmnoord = pp.create_line(net, from_bus=bus_zonpv_rivmnoord, to_bus=bus_sorbonne, length_km=0.3, name='lijn_zonpv_rivmnoord',std_type="630_AL_XLPE")
# pp.create_gen(net, bus=bus_zonpv_rivmnoord, p_mw=2.5*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_rivmnoord', vm_pu=1.0, controllable=False) #1 helft van de 4ha 5mw research pv fields (andere helft op schapenveld)
# 
# 
# 
# ################################################################################## veld 114 (Paars) #########################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84421 = pp.create_bus(net, vn_kv = 10., name = '84421', type = 'n')
# 
# bus_84422_1 = pp.create_bus(net, vn_kv = 10., name = '84422_1', type = 'b')
# 
# bus_84422_2 = pp.create_bus(net, vn_kv = 10., name = '84422_2', type = 'b')
# 
# bus_8534 = pp.create_bus(net, vn_kv = 10., name = '8534', type = 'n')
# 
# bus_2536 = pp.create_bus(net, vn_kv = 10., name = '2536', type = 'n')
# 
# bus_84490 = pp.create_bus(net, vn_kv = 10., name = '84490', type = 'n')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_84421 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84421, length_km=0.8, name='sorbonne_84421',std_type="150_AL_XLPE")
# 
# line_84421_84422_1 = pp.create_line(net, from_bus=bus_84421, to_bus=bus_84422_1, length_km=0.1, name='84421_84422_1',std_type="95_XLPE")
# 
# line_84422_2_8534 = pp.create_line(net, from_bus=bus_84422_2, to_bus=bus_8534, length_km=0.1, name='84422_2_8534',std_type="95_XLPE")
# 
# line_8534_2536 = pp.create_line(net, from_bus=bus_8534, to_bus=bus_2536, length_km=0.1, name='8535_2536',std_type="95_AL_XLPE")
# 
# line_2536_84490 = pp.create_line(net, from_bus=bus_2536, to_bus=bus_84490, length_km=0.1, name='2536_84490',std_type="95_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84421_101_var = True
# switch_84421_101 = pp.create_switch(net, bus_84421, line_sorbonne_84421, et='l', closed=switch_84421_101_var, type = 'LBS', name= '84421_101')
# 
# switch_84421_102_var = True
# switch_84421_102 = pp.create_switch(net, bus_84421, line_84421_84422_1, et='l', closed=switch_84421_102_var, type = 'LBS', name= '84421_102')
# 
# switch_84422_101_var = True
# switch_84422_101 = pp.create_switch(net, bus_84422_1, line_84421_84422_1, et='l', closed=switch_84422_101_var, type = 'LBS', name= '84422_101')
# 
# switch_84422_202_var = True
# switch_84422_202 = pp.create_switch(net, bus_84422_2, line_84422_2_8534, et='l', closed=switch_84422_202_var, type = 'LBS', name= '84422_202')
# 
# switch_8534_101_var = True
# switch_8534_101 = pp.create_switch(net, bus_8534, line_84422_2_8534, et='l', closed=switch_8534_101_var, type = 'LBS', name= '8534_101')
# 
# switch_8534_102_var = True
# switch_8534_102 = pp.create_switch(net, bus_8534, line_8534_2536, et='l', closed=switch_8534_102_var, type = 'LBS', name= '8534_102')
# 
# switch_2536_101_var = True
# switch_2536_101 = pp.create_switch(net, bus_2536, line_8534_2536, et='l', closed=switch_2536_101_var, type = 'LBS', name= '2536_101')
# 
# switch_2536_102_var = True
# switch_2536_102 = pp.create_switch(net, bus_2536, line_2536_84490, et='l', closed=switch_2536_102_var, type = 'LBS', name= '2536_102')
# 
# switch_84490_101_var = True
# switch_84490_101 = pp.create_switch(net, bus_84490, line_2536_84490, et='l', closed=switch_84490_101_var, type = 'LBS', name= '84490_101')
# 
# 
# 
# switch_84422_102_var = True
# switch_84422_102 = pp.create_switch(net, bus_84422_1, bus_84422_2, et='b', closed=switch_84422_102_var, type = 'LBS', name= '84422_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84421, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84421_1")
# 
# pp.create_load(net, bus=bus_84421, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84421_2")
# 
# pp.create_load(net, bus=bus_84421, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84421_3")
# 
# pp.create_load(net, bus=bus_84421, p_mw=0.075*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84421_4")
# 
# pp.create_load(net, bus=bus_84422_1, p_mw=0.40*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84422_1_1")
# 
# pp.create_load(net, bus=bus_84422_1, p_mw=0.40*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84422_1_2")
# 
# pp.create_load(net, bus=bus_84422_2, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84422_2_1")
# 
# pp.create_load(net, bus=bus_84422_2, p_mw=0.25*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84422_2_2")
# 
# pp.create_load(net, bus=bus_8534, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_8534")
# 
# pp.create_load(net, bus=bus_2536, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_2536")
# 
# pp.create_load(net, bus=bus_84490, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84490_1")
# 
# pp.create_load(net, bus=bus_84490, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84490_2")
# 
# 
# pp.create_gen(net, bus=bus_84421, p_mw=0.1323*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84421', vm_pu=1.0, controllable=False)  #C. Bleeker gebouw
# 
# pp.create_gen(net, bus=bus_84490, p_mw=0.136*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84490', vm_pu=1.0, controllable=False)  #VMC (TNO)
# 
# 
# pp.create_gen(net, bus=bus_2536, p_mw=0.0405*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_2536', vm_pu=1.0, controllable=False) #pv earth simul lab
# 
# 
# 
# 
# ################################################################################## veld 113 (Grijs) #########################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84444 = pp.create_bus(net, vn_kv = 10., name = '84444', type = 'n')
# 
# bus_84440 = pp.create_bus(net, vn_kv = 10., name = '84440', type = 'b')
# 
# bus_84442_1 = pp.create_bus(net, vn_kv = 10., name = '84442_1', type = 'b')
# 
# bus_84442_3 = pp.create_bus(net, vn_kv = 10., name = '84442_3', type = 'b')
# 
# bus_84442_4 = pp.create_bus(net, vn_kv = 10., name = '84442_4', type = 'b')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_84444 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84444, length_km=1.0, name='sorbonne_84444',std_type="150_AL_XLPE")
# 
# line_84444_84440 = pp.create_line(net, from_bus=bus_84444, to_bus=bus_84440, length_km=0.2, name='84444_84440',std_type="150_AL_XLPE")
# 
# line_84440_84442_k3 = pp.create_line(net, from_bus=bus_84440, to_bus=bus_84442_1, length_km=0.1, name='84440_84442_k3',std_type="50")
# 
# line_84440_84442_k2 = pp.create_line(net, from_bus=bus_84440, to_bus=bus_84442_3, length_km=0.1, name='84440_84442_k2',std_type="50")
# 
# line_84440_84442_k1 = pp.create_line(net, from_bus=bus_84440, to_bus=bus_84442_4, length_km=0.1, name='84440_84442_k1',std_type="50")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84444_101_var = True
# switch_84444_101 = pp.create_switch(net, bus_84444, line_sorbonne_84444, et='l', closed=switch_84444_101_var, type = 'LBS', name= '84444_101')
# 
# switch_84444_102_var = True
# switch_84444_102 = pp.create_switch(net, bus_84444, line_84444_84440, et='l', closed=switch_84444_102_var, type = 'LBS', name= '84444_102')
# 
# switch_84440_203_var = True
# switch_84440_203 = pp.create_switch(net, bus_84440, line_84444_84440, et='l', closed=switch_84440_203_var, type = 'LBS', name= '84440_203')
# 
# switch_84440_302_var = True
# switch_84440_302 = pp.create_switch(net, bus_84440, line_84440_84442_k3, et='l', closed=switch_84440_302_var, type = 'LBS', name= '84440_302')
# 
# switch_84440_303_var = True
# switch_84440_303 = pp.create_switch(net, bus_84440, line_84440_84442_k2, et='l', closed=switch_84440_303_var, type = 'LBS', name= '84440_303')
# 
# switch_84440_304_var = True
# switch_84440_304 = pp.create_switch(net, bus_84440, line_84440_84442_k1, et='l', closed=switch_84440_304_var, type = 'LBS', name= '84440_304')
# 
# switch_84442_101_var = True
# switch_84442_101 = pp.create_switch(net, bus_84442_1, line_84440_84442_k3, et='l', closed=switch_84442_101_var, type = 'LBS', name= '84442_101')
# 
# switch_84442_103_var = True
# switch_84442_103 = pp.create_switch(net, bus_84442_3, line_84440_84442_k2, et='l', closed=switch_84442_103_var, type = 'LBS', name= '84442_103')
# 
# switch_84442_104_var = True
# switch_84442_104 = pp.create_switch(net, bus_84442_4, line_84440_84442_k1, et='l', closed=switch_84442_104_var, type = 'LBS', name= '84442_104')
# 
# 
# 
# switch_84442_102_var = True   ### sectoropening
# switch_84442_102 = pp.create_switch(net, bus_84442_1, bus_84442_3, et='b', closed=switch_84442_102_var, type = 'LBS', name= '84442_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84444, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84444")
# 
# pp.create_load(net, bus=bus_84440, p_mw=0.40*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84440")
# 
# pp.create_load(net, bus=bus_84442_1, p_mw=0.40*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84442_1")
# 
# pp.create_load(net, bus=bus_84442_3, p_mw=0.25*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84442_3")
# 
# pp.create_load(net, bus=bus_84442_4, p_mw=0.25*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84442_4")
# 
# 
# 
# pp.create_gen(net, bus=bus_84444, p_mw=0.0288*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84444', vm_pu=1.0, controllable=False) #Langeveldgebouw
# 
# 
# 
# 
# ################################################################################## veld 206 (Lichtgroen) #########################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84407 = pp.create_bus(net, vn_kv = 10., name = '84407', type = 'n')
# 
# bus_84480 = pp.create_bus(net, vn_kv = 10., name = '84480', type = 'n')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_84407 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84407, length_km=1.5, name='sorbonne_84407',std_type="240_AL_XLPE")
# 
# line_84407_84480 = pp.create_line(net, from_bus=bus_84407, to_bus=bus_84480, length_km=0.7, name='84407_84480',std_type="95_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84407_101_var = True
# switch_84407_101 = pp.create_switch(net, bus_84407, line_sorbonne_84407, et='l', closed=switch_84407_101_var, type = 'LBS', name= '84407_101')
# 
# switch_84407_102_var = True
# switch_84407_102 = pp.create_switch(net, bus_84407, line_84407_84480, et='l', closed=switch_84407_102_var, type = 'LBS', name= '84407_102')
# 
# switch_84480_101_var = True
# switch_84480_101 = pp.create_switch(net, bus_84480, line_84407_84480, et='l', closed=switch_84480_101_var, type = 'LBS', name= '84480_101')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84407, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84407_1")
# 
# pp.create_load(net, bus=bus_84407, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_84407_2")
# 
# pp.create_load(net, bus=bus_84480, p_mw=0.25*0.5, q_mvar=0.05, name="Load_84480")    #parkeergarage
# 
# 
# 
# 
# ################################################################################## veld 116 (Lichtblauw) #########################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_84468 = pp.create_bus(net, vn_kv = 10., name = '84468', type = 'n')
# 
# bus_4412 = pp.create_bus(net, vn_kv = 10., name = '4412', type = 'n')
# 
# bus_1661 = pp.create_bus(net, vn_kv = 10., name = '1661', type = 'n')
# 
# bus_1660 = pp.create_bus(net, vn_kv = 10., name = '1660', type = 'n')
# 
# bus_84470 = pp.create_bus(net, vn_kv = 10., name = '84470', type = 'n')
# 
# 
# 
# bus_UMC = pp.create_bus(net, vn_kv = 10., name = 'UMC', type = 'b')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_84468 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84468, length_km=1.0, name='sorbonne_84468',std_type="240_AL_XLPE")
# 
# line_84468_4412 = pp.create_line(net, from_bus=bus_84468, to_bus=bus_4412, length_km=0.4, name='84468_4412',std_type="240_AL_XLPE")
# 
# line_4412_1661 = pp.create_line(net, from_bus=bus_4412, to_bus=bus_1661, length_km=0.1, name='4412_1661',std_type="95_XLPE")
# 
# line_1661_1660 = pp.create_line(net, from_bus=bus_1661, to_bus=bus_1660, length_km=0.1, name='1661_1660',std_type="150_AL_XLPE")
# 
# line_1660_84470 = pp.create_line(net, from_bus=bus_1660, to_bus=bus_84470, length_km=0.6, name='1660_84470',std_type="95_XLPE")
# 
# line_84470_84480 = pp.create_line(net, from_bus=bus_84470, to_bus=bus_84480, length_km=0.1, name='84470_84480',std_type="95_XLPE")
# 
# 
# 
# line_sorbonne_UMC_k1 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_UMC, length_km=1.3, name='sorbonne_UMC_k1',std_type="630_AL_XLPE")
# 
# line_sorbonne_UMC_k2 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_UMC, length_km=1.3, name='sorbonne_UMC_k2',std_type="630_AL_XLPE")
# 
# line_deBilt_UMC = pp.create_line(net, from_bus=bus_deBilt, to_bus=bus_UMC, length_km=2.3, name='deBilt_UMC',std_type="150_XLPE")
# 
# line_84470_UMC = pp.create_line(net, from_bus=bus_84470, to_bus=bus_UMC, length_km=0.1, name='84470_UMC',std_type="240_AL_XLPE")  #Kabeltype is in dit geval een aanname
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_84468_101_var = True
# switch_84468_101 = pp.create_switch(net, bus_84468, line_sorbonne_84468, et='l', closed=switch_84468_101_var, type = 'LBS', name= '84468_101')
# 
# switch_84468_102_var = True
# switch_84468_102 = pp.create_switch(net, bus_84468, line_84468_4412, et='l', closed=switch_84468_102_var, type = 'LBS', name= '84468_102')
# 
# switch_4412_101_var = True
# switch_4412_101 = pp.create_switch(net, bus_4412, line_84468_4412, et='l', closed=switch_4412_101_var, type = 'LBS', name= '4412_101')
# 
# switch_4412_102_var = True
# switch_4412_102 = pp.create_switch(net, bus_4412, line_4412_1661, et='l', closed=switch_4412_102_var, type = 'LBS', name= '4412_102')
# 
# switch_1661_101_var = True
# switch_1661_101 = pp.create_switch(net, bus_1661, line_4412_1661, et='l', closed=switch_1661_101_var, type = 'LBS', name= '1661_101')
# 
# switch_1661_102_var = True
# switch_1661_102 = pp.create_switch(net, bus_1661, line_1661_1660, et='l', closed=switch_1661_102_var, type = 'LBS', name= '1661_102')
# 
# switch_1660_101_var = True
# switch_1660_101 = pp.create_switch(net, bus_1660, line_1661_1660, et='l', closed=switch_1660_101_var, type = 'LBS', name= '1660_101')
# 
# switch_1660_102_var = True
# switch_1660_102 = pp.create_switch(net, bus_1660, line_1660_84470, et='l', closed=switch_1660_102_var, type = 'LBS', name= '1660_102')
# 
# switch_84470_101_var = True
# switch_84470_101 = pp.create_switch(net, bus_84470, line_1660_84470, et='l', closed=switch_84470_101_var, type = 'LBS', name= '84470_101')
# 
# switch_84470_102_var = True   ### sectoropening
# switch_84470_102 = pp.create_switch(net, bus_84470, line_84470_84480, et='l', closed=switch_84470_102_var, type = 'LBS', name= '84470_102')
# 
# switch_84470_103_var = True
# switch_84470_103 = pp.create_switch(net, bus_84470, line_84470_UMC, et='l', closed=switch_84470_103_var, type = 'LBS', name= '84470_103')
# 
# switch_84480_102_var = True
# switch_84480_102 = pp.create_switch(net, bus_84480, line_84470_84480, et='l', closed=switch_84480_102_var, type = 'LBS', name= '84480_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_84468, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84468")
# 
# pp.create_load(net, bus=bus_4412, p_mw=1.00*(demand_profiles.at[t, 'res_2']/14.5), q_mvar=0.05, name="Load_4412")
# 
# pp.create_load(net, bus=bus_1661, p_mw=0.63*(demand_profiles.at[t, 'res_2']/14.5), q_mvar=0.05, name="Load_1661")
# 
# pp.create_load(net, bus=bus_1660, p_mw=0.25*(demand_profiles.at[t, 'res_2']/14.5), q_mvar=0.05, name="Load_1660")
# 
# 
# 
# pp.create_load(net, bus=bus_UMC, p_mw=2.00, q_mvar=0.05, name="Load_UMC")      #Gokje, en eigenlijk irrelevant
# 
# 
# 
# 
# pp.create_gen(net, bus=bus_4412, p_mw=0.12*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_4412', vm_pu=1.0, controllable=False) #pv pilot van 0.5 ha. voor nu even op veldje achter camelot gepland, meer data onduidelijk
# 
# 
# 
# 
# ################################################################################## veld 106 (Lichtblauw) #########################################################################
# 
# 
# 
# 
# ###   Busjes   ###
# 
# bus_1922 = pp.create_bus(net, vn_kv = 10., name = '1922', type = 'n')
# 
# bus_8533 = pp.create_bus(net, vn_kv = 10., name = '8533', type = 'n')
# 
# bus_6999 = pp.create_bus(net, vn_kv = 10., name = '6999', type = 'n')
# 
# bus_6577 = pp.create_bus(net, vn_kv = 10., name = '6577', type = 'n')
# 
# bus_84436_1 = pp.create_bus(net, vn_kv = 10., name = '84436_1', type = 'b')
# 
# bus_2453 = pp.create_bus(net, vn_kv = 10., name = '2453', type = 'n')
# 
# bus_8563 = pp.create_bus(net, vn_kv = 10., name = '8563', type = 'n')
# 
# bus_84419 = pp.create_bus(net, vn_kv = 10., name = '84419', type = 'n')
# 
# bus_8505 = pp.create_bus(net, vn_kv = 10., name = '8505', type = 'n')
# 
# 
# 
# bus_84436_2 = pp.create_bus(net, vn_kv = 10., name = '84436_2', type = 'b')
# 
# bus_84435 = pp.create_bus(net, vn_kv = 10., name = '84435', type = 'n')
# 
# bus_84439 = pp.create_bus(net, vn_kv = 10., name = '84439', type = 'n')
# 
# bus_84438 = pp.create_bus(net, vn_kv = 10., name = '84438', type = 'b')
# 
# bus_4129_1 = pp.create_bus(net, vn_kv = 10., name = '4129_1', type = 'b')
# 
# bus_4129_2 = pp.create_bus(net, vn_kv = 10., name = '4129_2', type = 'b')
# 
# 
# 
# 
# ###   Lijnen   ###
# 
# line_sorbonne_1922 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_1922, length_km=0.2, name='sorbonne_1922',std_type="150_XLPE")
# 
# line_1922_8533 = pp.create_line(net, from_bus=bus_1922, to_bus=bus_8533, length_km=0.6, name='1922_8533',std_type="95_XLPE")
# 
# line_8533_6999 = pp.create_line(net, from_bus=bus_8533, to_bus=bus_6999, length_km=0.1, name='8533_6999',std_type="150_AL_XLPE")
# 
# line_6999_6577 = pp.create_line(net, from_bus=bus_6999, to_bus=bus_6577, length_km=0.1, name='6999_6577',std_type="150_AL_XLPE")
# 
# line_6577_84436_1 = pp.create_line(net, from_bus=bus_6577, to_bus=bus_84436_1, length_km=0.3, name='6577_84436',std_type="95_XLPE")
# 
# line_84436_1_2453 = pp.create_line(net, from_bus=bus_84436_1, to_bus=bus_2453, length_km=0.4, name='84436_1_2453',std_type="95_XLPE")
# 
# line_2453_84494_3 = pp.create_line(net, from_bus=bus_2453, to_bus=bus_84494_3, length_km=0.7, name='2453_84494_3',std_type="240_AL_XLPE")
# 
# line_2453_8563 = pp.create_line(net, from_bus=bus_2453, to_bus=bus_8563, length_km=0.1, name='2453_8563',std_type="150_AL_XLPE")
# 
# line_8563_84419 = pp.create_line(net, from_bus=bus_8563, to_bus=bus_84419, length_km=0.1, name='8563_84419',std_type="95_XLPE")
# 
# line_84419_8505 = pp.create_line(net, from_bus=bus_84419, to_bus=bus_8505, length_km=0.1, name='84419_8505',std_type="95_XLPE")
# 
# line_8505_84490 = pp.create_line(net, from_bus=bus_8505, to_bus=bus_84490, length_km=0.1, name='8505_84490',std_type="150_AL_XLPE")
# 
# line_84436_2_84435 = pp.create_line(net, from_bus=bus_84436_2, to_bus=bus_84435, length_km=0.1, name='84436_2_84435',std_type="50")
# 
# line_84436_2_84439 = pp.create_line(net, from_bus=bus_84436_2, to_bus=bus_84439, length_km=0.1, name='84436_2_84439',std_type="95")
# 
# line_84439_84438 = pp.create_line(net, from_bus=bus_84439, to_bus=bus_84438, length_km=0.1, name='84439_84438',std_type="95")
# 
# line_84438_4129_1 = pp.create_line(net, from_bus=bus_84438, to_bus=bus_4129_1, length_km=0.2, name='84438_4129_1',std_type="150_AL_XLPE")
# 
# line_4129_2_84440 = pp.create_line(net, from_bus=bus_4129_2, to_bus=bus_84440, length_km=0.1, name='4129_2_84440_2',std_type="95_XLPE")
# 
# 
# 
# 
# ###   Schakelaars   ###
# 
# switch_1922_101_var = True
# switch_1922_101 = pp.create_switch(net, bus_1922, line_sorbonne_1922, et='l', closed=switch_1922_101_var, type = 'LBS', name= '1922_101')
# 
# switch_1922_102_var = True
# switch_1922_102 = pp.create_switch(net, bus_1922, line_1922_8533, et='l', closed=switch_1922_102_var, type = 'LBS', name= '1922_102')
# 
# switch_8533_101_var = True
# switch_8533_101 = pp.create_switch(net, bus_8533, line_1922_8533, et='l', closed=switch_8533_101_var, type = 'LBS', name= '8533_101')
# 
# switch_8533_102_var = True
# switch_8533_102 = pp.create_switch(net, bus_8533, line_8533_6999, et='l', closed=switch_8533_102_var, type = 'LBS', name= '8533_102')
# 
# switch_6999_101_var = True
# switch_6999_101 = pp.create_switch(net, bus_6999, line_8533_6999, et='l', closed=switch_6999_101_var, type = 'LBS', name= '6999_101')
# 
# switch_6999_102_var = True
# switch_6999_102 = pp.create_switch(net, bus_6999, line_6999_6577, et='l', closed=switch_6999_102_var, type = 'LBS', name= '6999_102')
# 
# switch_6577_101_var = True
# switch_6577_101 = pp.create_switch(net, bus_6577, line_6999_6577, et='l', closed=switch_6577_101_var, type = 'LBS', name= '6577_101')
# 
# switch_6577_102_var = True
# switch_6577_102 = pp.create_switch(net, bus_6577, line_6577_84436_1, et='l', closed=switch_6577_102_var, type = 'LBS', name= '6577_102')
# 
# switch_84436_102_var = True
# switch_84436_102 = pp.create_switch(net, bus_84436_1, line_6577_84436_1, et='l', closed=switch_84436_102_var, type = 'LBS', name= '84436_102')
# 
# 
# 
# switch_84436_101_var = True
# switch_84436_101 = pp.create_switch(net, bus_84436_1, line_84436_1_2453, et='l', closed=switch_84436_101_var, type = 'LBS', name= '84436_101')
# 
# switch_2453_102_var = True
# switch_2453_102 = pp.create_switch(net, bus_2453, line_84436_1_2453, et='l', closed=switch_2453_102_var, type = 'LBS', name= '2453_102')
# 
# switch_2453_103_var = True   ### sectoropening
# switch_2453_103 = pp.create_switch(net, bus_2453, line_2453_84494_3, et='l', closed=switch_2453_103_var, type = 'LBS', name= '2453_103')
# 
# switch_84494_302_var = True
# switch_84494_302 = pp.create_switch(net, bus_84494_3, line_2453_84494_3, et='l', closed=switch_84494_302_var, type = 'LBS', name= '84494_302')
# 
# switch_2453_101_var = True
# switch_2453_101 = pp.create_switch(net, bus_2453, line_2453_8563, et='l', closed=switch_2453_101_var, type = 'LBS', name= '2453_101')
# 
# switch_8563_101_var = True
# switch_8563_101 = pp.create_switch(net, bus_8563, line_2453_8563, et='l', closed=switch_8563_101_var, type = 'LBS', name= '8563_101')
# 
# switch_8563_102_var = True
# switch_8563_102 = pp.create_switch(net, bus_8563, line_8563_84419, et='l', closed=switch_8563_102_var, type = 'LBS', name= '8563_102')
# 
# switch_84419_101_var = True
# switch_84419_101 = pp.create_switch(net, bus_84419, line_8563_84419, et='l', closed=switch_84419_101_var, type = 'LBS', name= '84419_101')
# 
# switch_84419_102_var = True
# switch_84419_102 = pp.create_switch(net, bus_84419, line_84419_8505, et='l', closed=switch_84419_102_var, type = 'LBS', name= '84419_102')
# 
# switch_8505_101_var = True
# switch_8505_101 = pp.create_switch(net, bus_8505, line_84419_8505, et='l', closed=switch_8505_101_var, type = 'LBS', name= '8505_101')
# 
# switch_8505_102_var = True   ### sectoropening
# switch_8505_102 = pp.create_switch(net, bus_8505, line_8505_84490, et='l', closed=switch_8505_102_var, type = 'LBS', name= '8505_102')
# 
# switch_84490_102_var = True
# switch_84490_102 = pp.create_switch(net, bus_84490, line_8505_84490, et='l', closed=switch_84490_102_var, type = 'LBS', name= '84490_102')
# 
# 
# 
# switch_84436_203_var = True
# switch_84436_203 = pp.create_switch(net, bus_84436_2, line_84436_2_84435, et='l', closed=switch_84436_203_var, type = 'LBS', name= '84436_203')
# 
# switch_84436_204_var = True
# switch_84436_204 = pp.create_switch(net, bus_84436_2, line_84436_2_84439, et='l', closed=switch_84436_204_var, type = 'LBS', name= '84436_204')
# 
# switch_84439_101_var = True
# switch_84439_101 = pp.create_switch(net, bus_84439, line_84436_2_84439, et='l', closed=switch_84439_101_var, type = 'LBS', name= '84439_101')
# 
# switch_84439_102_var = True
# switch_84439_102 = pp.create_switch(net, bus_84439, line_84439_84438, et='l', closed=switch_84439_102_var, type = 'LBS', name= '84439_102')
# 
# switch_84438_102_var = True
# switch_84438_102 = pp.create_switch(net, bus_84438, line_84439_84438, et='l', closed=switch_84438_102_var, type = 'LBS', name= '84438_102')
# 
# switch_84438_101_var = True
# switch_84438_101 = pp.create_switch(net, bus_84438, line_84438_4129_1, et='l', closed=switch_84438_101_var, type = 'LBS', name= '84438_101')
# 
# switch_4129_101_var = True
# switch_4129_101 = pp.create_switch(net, bus_4129_1, line_84438_4129_1, et='l', closed=switch_4129_101_var, type = 'LBS', name= '4129_101')
# 
# switch_4129_202_var = True   ### sectoropening
# switch_4129_202 = pp.create_switch(net, bus_4129_2, line_4129_2_84440, et='l', closed=switch_4129_202_var, type = 'LBS', name= '4129_202')
# 
# switch_84440_202_var = True
# switch_84440_202 = pp.create_switch(net, bus_84440, line_4129_2_84440, et='l', closed=switch_84440_202_var, type = 'LBS', name= '84440_202')
# 
# 
# 
# switch_84436_104_var = True   ### sectoropening
# switch_84436_104 = pp.create_switch(net, bus_84436_1, bus_84436_3, et='b', closed=switch_84436_104_var, type = 'LBS', name= '84436_104')
# 
# switch_84436_103_var = True
# switch_84436_103 = pp.create_switch(net, bus_84436_1, bus_84436_2, et='b', closed=switch_84436_103_var, type = 'LBS', name= '84436_103')
# 
# switch_4129_102_var = True
# switch_4129_102 = pp.create_switch(net, bus_4129_1, bus_4129_2, et='b', closed=switch_4129_102_var, type = 'LBS', name= '4129_102')
# 
# 
# 
# 
# ###   Lasten en Productie   ###
# 
# pp.create_load(net, bus=bus_1922, p_mw=0.25*0.5, q_mvar=0.05, name="Load_1922")   #parkeerterrein
# 
# pp.create_load(net, bus=bus_8533, p_mw=0.40*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_8533")
# 
# pp.create_load(net, bus=bus_6999, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_6999")
# 
# pp.create_load(net, bus=bus_6577, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_6577_1")
# 
# pp.create_load(net, bus=bus_6577, p_mw=1.00*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_6577_2")
# 
# pp.create_load(net, bus=bus_2453, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_2453")
# 
# pp.create_load(net, bus=bus_8563, p_mw=0.40*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_8563")
# 
# pp.create_load(net, bus=bus_84419, p_mw=0.20*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84419_1")
# 
# pp.create_load(net, bus=bus_84419, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_84419_2")
# 
# pp.create_load(net, bus=bus_8505, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_8505_1")
# 
# pp.create_load(net, bus=bus_8505, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], q_mvar=0.05, name="Load_8505_2")
# 
# pp.create_load(net, bus=bus_84435, p_mw=0.40*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84435")
# 
# pp.create_load(net, bus=bus_84436_2, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84436_2")
# 
# pp.create_load(net, bus=bus_84439, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84439_1")
# 
# pp.create_load(net, bus=bus_84439, p_mw=0.40*demand_profiles.at[t, 'lab_oud'], q_mvar=0.05, name="Load_84439_2")
# 
# pp.create_load(net, bus=bus_84438, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84438_1")
# 
# pp.create_load(net, bus=bus_84438, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], q_mvar=0.05, name="Load_84438_2")
# 
# pp.create_load(net, bus=bus_4129_1, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_4129_1")
# 
# pp.create_load(net, bus=bus_4129_2, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], q_mvar=0.05, name="Load_4129_2")
# 
# 
# 
# pp.create_load(net, bus=bus_1922, p_mw=0.4*demand_profiles.at[t, 'ev_simpel'], q_mvar=0.05, name="ev_1922")
# 
# pp.create_load(net, bus=bus_8563, p_mw=0.05*demand_profiles.at[t, 'ev_simpel'], q_mvar=0.05, name="ev_8563") #50 laadpalen, overige 200 die vereist zijn komen op Olympos
# 
# 
# 
# pp.create_gen(net, bus=bus_6999, p_mw=0.034*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_6999', vm_pu=1.0, controllable=False)
# 
# pp.create_gen(net, bus=bus_1922, p_mw=0.4*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_1922', vm_pu=1.0, controllable=False)
# 
# bus_zonpv_schapenveld = pp.create_bus(net, vn_kv = 10., name = 'bus_zonpv_schapenveld', type = 'n')
# line_zonpv_schapenveld = pp.create_line(net, from_bus=bus_zonpv_schapenveld, to_bus=bus_sorbonne, length_km=0.5, name='lijn_zonpv_schapenveld',std_type="630_AL_XLPE")
# pp.create_gen(net, bus=bus_zonpv_schapenveld, p_mw=2.5*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_zonpv_schapenveld', vm_pu=1.0, controllable=False) #1 helft van de 4ha 5mw research pv fields (andere helft op veldje tussen leuvenlaan en weg tot de wetenschap in)
# 
# pp.create_gen(net, bus=bus_8563, p_mw=0.3*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_8563', vm_pu=1.0, controllable=False) #Solar carports
# 
# 
# 
# 
# 
#    
# 
# 
# 
# 
# 
# ============================================================================



results = dict()


############################################################################################################   for loop die een jaar simuleert   ###############################################################################



for t in i:
    

    net.load.iat[ 0 , 2] = 10.0*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 1 , 2] = 10.0*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 2 , 2] = 3.0*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 3 , 2] = 3.0*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 4 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 5 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 6 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 7 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 8 , 2] = 0.60*demand_profiles.at[t, 'ev_simpel']
    net.load.iat[ 9 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 10 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 11 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 12 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 13 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 14 , 2] = 1.00*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 15 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 16 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 17 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 18 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 19 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 20 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 21 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 22 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 23 , 2] = 0.10*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 24 , 2] = 0.60*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 25 , 2] = 0.30*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 26 , 2] = 0.315*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 27 , 2] = 1.00*0.5
    net.load.iat[ 28 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 29 , 2] = 0.2*demand_profiles.at[t, 'ev_simpel']
    net.load.iat[ 30 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 31 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 32 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 33 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 34 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 35 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 36 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 37 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 38 , 2] = 1.60*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 39 , 2] = 0.16*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 40 , 2] = (demand_profiles.at[t, 'res_1']/14.5)*0.63
    net.load.iat[ 41 , 2] = 1.25*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 42 , 2] = 1.60*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 43 , 2] = 1.00*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 44 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 45 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 46 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 47 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 48 , 2] = 0.40*0.5
    net.load.iat[ 49 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 50 , 2] = 0.630*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 51 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 52 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 53 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 54 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 55 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 56 , 2] = 0.075*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 57 , 2] = 0.40*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 58 , 2] = 0.40*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 59 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 60 , 2] = 0.25*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 61 , 2] = 1.00*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 62 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 63 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 64 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 65 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 66 , 2] = 0.40*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 67 , 2] = 0.40*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 68 , 2] = 0.25*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 69 , 2] = 0.25*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 70 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 71 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 72 , 2] = 0.25*0.5
    net.load.iat[ 73 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 74 , 2] = 1.00*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 75 , 2] = 0.63*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 76 , 2] = 0.25*(demand_profiles.at[t, 'res_2']/14.5)
    net.load.iat[ 77 , 2] = 2.00
    net.load.iat[ 78 , 2] = 0.25*0.5
    net.load.iat[ 79 , 2] = 0.40*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 80 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 81 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 82 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 83 , 2] = 1.00*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 84 , 2] = 0.40*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 85 , 2] = 0.20*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 86 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 87 , 2] = 0.63*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 88 , 2] = 1.00*demand_profiles.at[t, 'lab_nieuw']
    net.load.iat[ 89 , 2] = 0.40*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 90 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 91 , 2] = 0.63*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 92 , 2] = 0.40*demand_profiles.at[t, 'lab_oud']
    net.load.iat[ 93 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 94 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_oud']
    net.load.iat[ 95 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 96 , 2] = 0.63*demand_profiles.at[t, 'onderwijs_nieuw']
    net.load.iat[ 97 , 2] = 0.4*demand_profiles.at[t, 'ev_simpel']
    net.load.iat[ 98 , 2] = 0.05*demand_profiles.at[t, 'ev_simpel']
    
    
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
    net.sgen.iat[ 14 , 2] = 3.5*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 15 , 2] = 2.5*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 16 , 2] = 0.1323*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 17 , 2] = 0.136*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 18 , 2] = 0.0405*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 19 , 2] = 0.0288*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 20 , 2] = 0.12*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 21 , 2] = 0.034*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 22 , 2] = 0.0413*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 23 , 2] = 2.5*demand_profiles.at[t, 'pv_veld_1_MW']
    net.sgen.iat[ 24 , 2] = 0.3*demand_profiles.at[t, 'pv_veld_1_MW']
    
    pp.runpp(net, max_iteration=10000)
    
    
    
    
    #######################################################################   Diagnostiek   #######################################################
    
    energiegebruik = energiegebruik + net.res_load['p_mw'].sum()      ### voor het berekenen ven het totale energiegebruik, somt alle lasten.
    
    results[t] = net.res_line.loading_percent.max()
    
    
    list_kabelbelastingen = net.res_line.loading_percent.values.tolist()
    list_kabelbelastingen_groterdan_50 = [item for item in list_kabelbelastingen if item > 50]
    list_kabelbelastingen_groterdan_50 = [i - 50 for i in list_kabelbelastingen_groterdan_50]
    
    
    kwadratensom = sum(i*i for i in list_kabelbelastingen_groterdan_50)
    totale_kwadratensom = totale_kwadratensom + kwadratensom
    
    
    if len(list_kabelbelastingen_groterdan_50) > 0:
        overbelastingsuren = overbelastingsuren + 1
    
    
    
    print(net.res_line.loading_percent.max())
    print(t)










##################################################################################################   Nuttige regeltjes code   ####################################################################################3


print(overbelastingsuren)
print(energiegebruik)
print (totale_kwadratensom)
#plot.simple_plotly(net)
#pp.runpp(net)lalalalala

#pp.diagnostic(net, report_style='detailed')





