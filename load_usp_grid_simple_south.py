# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:11:20 2023

@author: battuejd
"""


import pandas as pd

import pandapower as pp


#import load_usp_grid


demand_profiles = pd.DataFrame(pd.read_excel('Input Data/weekprofielen.xlsx', 'profielen_s3', index_col=('Uur:')))

t = 1




###   Niew net aanmaken en standaard kabeltypes ingeven   ###



net = pp.create_empty_network()
   


line_data_50_XLPE = {"c_nf_per_km": 260, "r_ohm_per_km": 0.387, "x_ohm_per_km": 0.138, "max_i_ka": 0.185, "type": "cs", "q_mm2": 50}
pp.create_std_type(net, line_data_50_XLPE, "50_XLPE", element='line')

line_data_50 = {"c_nf_per_km": 260, "r_ohm_per_km": 0.385, "x_ohm_per_km": 0.138, "max_i_ka": 0.185, "type": "cs", "q_mm2": 50}
pp.create_std_type(net, line_data_50, "50", element='line')

line_data_95 = {"c_nf_per_km": 330, "r_ohm_per_km" : 0.139, "x_ohm_per_km": 0.123, "max_i_ka": 0.270, "type": "cs", "q_mm2": 95}
pp.create_std_type(net, line_data_95, "95", element='line')

line_data_95_XLPE = {"c_nf_per_km": 330, "r_ohm_per_km" : 0.139, "x_ohm_per_km": 0.123, "max_i_ka": 0.270, "type": "cs", "q_mm2": 95}
pp.create_std_type(net, line_data_95, "95_XLPE", element='line')

line_data_95_AL_XLPE = {"c_nf_per_km": 310, "r_ohm_per_km": 0.320, "x_ohm_per_km": 0.134, "max_i_ka": 0.215, "type": "cs", "q_mm2": 95}
pp.create_std_type(net, line_data_95_AL_XLPE, "95_AL_XLPE", element='line')

line_data_150_XLPE = {"c_nf_per_km": 390, "r_ohm_per_km": 0.124, "x_ohm_per_km": 0.114, "max_i_ka": 0.335, "type": "cs", "q_mm2": 150}
pp.create_std_type(net, line_data_150_XLPE, "150_XLPE", element='line')

line_data_150_AL_XLPE = {"c_nf_per_km": 360, "r_ohm_per_km": 0.206, "x_ohm_per_km": 0.127, "max_i_ka": 0.280, "type": "cs", "q_mm2": 150}
pp.create_std_type(net, line_data_150_AL_XLPE, "150_AL_XLPE", element='line')

line_data_240_AL_XLPE = {"c_nf_per_km": 440, "r_ohm_per_km": 0.125, "x_ohm_per_km": 0.118, "max_i_ka": 0.360, "type": "cs", "q_mm2": 240}
pp.create_std_type(net, line_data_240_AL_XLPE, "240_AL_XLPE", element='line')

line_data_630_AL_XLPE = {"c_nf_per_km": 660, "r_ohm_per_km": 0.0469, "x_ohm_per_km": 0.103, "max_i_ka": 1.102, "type": "cs", "q_mm2": 630}
pp.create_std_type(net, line_data_630_AL_XLPE, "630_AL_XLPE", element='line')






################################################################## Sorbonne busrail en de Bilt busrail ####################################################################

bus_sorbonne = pp.create_bus(net, vn_kv = 10., name = 'sorbonnelaan', type = 'b')

pp.create_ext_grid(net, bus_sorbonne,)



bus_deBilt = pp.create_bus(net, vn_kv = 10., name = 'deBilt', type = 'b')

pp.create_ext_grid(net, bus_deBilt,)











# =============================================================================
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
# pp.create_load(net, bus=bus_4360, p_mw=10.0*demand_profiles.at[t, 'lab_nieuw'], name="Load_4360")
# 
# pp.create_load(net, bus=bus_4359, p_mw=10.0*demand_profiles.at[t, 'lab_nieuw'], name="Load_4359")
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
# pp.create_load(net, bus=bus_4665, p_mw=3.0*demand_profiles.at[t, 'lab_nieuw'], name="Load_4665")
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
# pp.create_load(net, bus=bus_8515, p_mw=3.0*demand_profiles.at[t, 'lab_nieuw'], name="Load_8515")
# 
# 
# 
# =============================================================================

################################################################### veld 104 & 107 & 130 (naar WKC) (Grijs) ###################################################################




###   Busjes   ###

bus_84460 = pp.create_bus(net, vn_kv = 10., name = '84460', type = 'b')

bus_84460_2 = pp.create_bus(net, vn_kv = 10., name = '84460_2', type = 'b')




###   Lijnen   ###

line_sorbonne_84460_k1 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84460, length_km=1.6, name='sorbonne_84460_k1',std_type="630_AL_XLPE")

line_sorbonne_84460_k2 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84460, length_km=1.6, name='sorbonne_84460_k2',std_type="630_AL_XLPE")

line_sorbonne_84460_k3 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84460, length_km=1.6, name='sorbonne_84460_k3',std_type="630_AL_XLPE")




# =============================================================================
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
# =============================================================================

switch_84460_2_var = True
switch_84460_2 = pp.create_switch(net, bus_84460, bus_84460_2, et='b', closed=switch_84460_2_var, type = 'LBS', name= '84460_2')



###   Lasten en Productie   ###






###################################################################### veld 84460_2 205 (Jenalaan WKC) (Lichtgroen) ###############################################################




###   Busjes   ###

bus_4516 = pp.create_bus(net, vn_kv = 10., name = '4516', type = 'n')

bus_4738 = pp.create_bus(net, vn_kv = 10., name = '4738', type = 'n')

bus_84432 = pp.create_bus(net, vn_kv = 10., name = '84432', type = 'n')



bus_zonpv_zuidoost = pp.create_bus(net, vn_kv = 10., name = 'zonpv_zuidoost', type = 'n')




###   Lijnen   ###

line_84460_2_4516 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_4516, length_km=0.1, name='84460_2_4516',std_type="95_AL_XLPE")

line_4516_4738 = pp.create_line(net, from_bus=bus_4516, to_bus=bus_4738, length_km=0.1, name='4516_4738',std_type="50_XLPE")

line_4738_84432 = pp.create_line(net, from_bus=bus_4738, to_bus=bus_84432, length_km=0.1, name='4738_84432',std_type="50_XLPE")



line_zonpv_zuidoost = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_zonpv_zuidoost, length_km=1.5, name='zonpv_zuidoost',std_type="630_AL_XLPE")




###   Schakelaars   ###

switch_84460_205_var = True
switch_84460_205 = pp.create_switch(net, bus_84460_2, line_84460_2_4516, et='l', closed=switch_84460_205_var, type = 'LBS', name= '84460_205')

#switch_4516_102_var = True
#switch_4516_102 = pp.create_switch(net, bus_4516, line_84460_2_4516, et='l', closed=switch_4516_102_var, type = 'LBS', name= '4516_102')

#switch_4516_101_var = True
#switch_4516_101 = pp.create_switch(net, bus_4516, line_4516_4738, et='l', closed=switch_4516_101_var, type = 'LBS', name= '4516_101')

switch_4738_101_var = True
switch_4738_101 = pp.create_switch(net, bus_4738, line_4516_4738, et='l', closed=switch_4738_101_var, type = 'LBS', name= '4738_101')

#switch_4738_102_var = True
#switch_4738_102 = pp.create_switch(net, bus_4738, line_4738_84432, et='l', closed=switch_4738_102_var, type = 'LBS', name= '4738_102')

switch_84432_101_var = True
switch_84432_101 = pp.create_switch(net, bus_84432, line_4738_84432, et='l', closed=switch_84432_101_var, type = 'LBS', name= '84432_101')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_4516, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_4516")

pp.create_load(net, bus=bus_4738, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_4738")

pp.create_load(net, bus=bus_84432, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84432")

pp.create_load(net, bus=bus_84432, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84432_2")




pp.create_load(net, bus=bus_84432, p_mw=0.60*demand_profiles.at[t, 'ev_simpel'], name="Load_ev_84432")




pp.create_sgen(net, bus=bus_4738, p_mw=0.1312*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_4738')  #tolakker jongveestal

pp.create_sgen(net, bus=bus_84432, p_mw=0.2862*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84432')  #dak Martinud g de bruingebouw

pp.create_sgen(net, bus=bus_84432, p_mw=0.0499*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84432_2')  #pv carport er naast

pp.create_sgen(net, bus=bus_zonpv_zuidoost, p_mw=2*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_dak+carports_zuidoost') #dakpv 1,3mw + een stuk solarcarports er naast (bij tolakker)

pp.create_sgen(net, bus=bus_4738, p_mw=0.1576*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_4738_2')  #tolakker rundveestal

pp.create_sgen(net, bus=bus_zonpv_zuidoost, p_mw=9*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_9mwweide_zuidoost') #1 deel van de 10.5ha 12.5mw nature inclusive pv fields (andere deel op veldje tussen cambridgeflat en rivm in)





###################################################################### veld 84460_2 204 (Jenalaan WKC) (Lichtblauw) ###############################################################




###   Busjes   ###

bus_84429_1 = pp.create_bus(net, vn_kv = 10., name = '84429_1', type = 'b')

bus_84429_2 = pp.create_bus(net, vn_kv = 10., name = '84429_2', type = 'b')

bus_84427 = pp.create_bus(net, vn_kv = 10., name = '84427', type = 'n')

bus_84428 = pp.create_bus(net, vn_kv = 10., name = '84428', type = 'n')

bus_84453_2 = pp.create_bus(net, vn_kv = 10., name = '84453_2', type = 'b')

bus_84453_1 = pp.create_bus(net, vn_kv = 10., name = '84453_1', type = 'b')

bus_84495 = pp.create_bus(net, vn_kv = 10., name = '84495', type = 'n')





###   Lijnen   ###

line_84460_2_84429_1 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_84429_1, length_km=0.1, name='84460_2_84429_1',std_type="95_AL_XLPE")

line_84429_1_84432 = pp.create_line(net, from_bus=bus_84429_1, to_bus=bus_84432, length_km=0.1, name='84429_1_84432',std_type="50_XLPE")

line_84429_2_84427 = pp.create_line(net, from_bus=bus_84429_2, to_bus=bus_84427, length_km=0.1, name='84429_2_84427',std_type="50_XLPE")

line_84427_84428 = pp.create_line(net, from_bus=bus_84427, to_bus=bus_84428, length_km=0.1, name='84427_84428',std_type="50")

line_84428_84453_2 = pp.create_line(net, from_bus=bus_84428, to_bus=bus_84453_2, length_km=0.1, name='84428_84453_2',std_type="150_AL_XLPE")

line_84453_1_84495 = pp.create_line(net, from_bus=bus_84453_1, to_bus=bus_84495, length_km=0.1, name='84453_1_84495',std_type="95_XLPE")




###   Schakelaars   ###

switch_84429_102_var = True
switch_84429_102 = pp.create_switch(net, bus_84429_1, line_84460_2_84429_1, et='l', closed=switch_84429_102_var, type = 'LBS', name= '84429_102')

switch_84429_101_var = False  ##### sectoropening?
switch_84429_101 = pp.create_switch(net, bus_84429_1, line_84429_1_84432, et='l', closed=switch_84429_101_var, type = 'LBS', name= '84429_101')

#switch_84432_102_var = True
#switch_84432_102 = pp.create_switch(net, bus_84432, line_84429_1_84432, et='l', closed=switch_84432_102_var, type = 'LBS', name= '84432_102')

#switch_84429_202_var = True
#switch_84429_202 = pp.create_switch(net, bus_84429_2, line_84429_2_84427, et='l', closed=switch_84429_202_var, type = 'LBS', name= '84429_202')

switch_84427_101_var = True
switch_84427_101 = pp.create_switch(net, bus_84427, line_84429_2_84427, et='l', closed=switch_84427_101_var, type = 'LBS', name= '84427_101')

#switch_84427_102_var = True
#switch_84427_102 = pp.create_switch(net, bus_84427, line_84427_84428, et='l', closed=switch_84427_102_var, type = 'LBS', name= '84427_102')

switch_84428_101_var = True
switch_84428_101 = pp.create_switch(net, bus_84428, line_84427_84428, et='l', closed=switch_84428_101_var, type = 'LBS', name= '84428_101')

switch_84428_102_var = True
switch_84428_102 = pp.create_switch(net, bus_84428, line_84428_84453_2, et='l', closed=switch_84428_102_var, type = 'LBS', name= '84428_102')

#switch_84453_101_var = True
#switch_84453_101 = pp.create_switch(net, bus_84453_1, line_84453_1_84495, et='l', closed=switch_84453_101_var, type = 'LBS', name= '84453_101')

switch_84495_101_var = True
switch_84495_101 = pp.create_switch(net, bus_84495, line_84453_1_84495, et='l', closed=switch_84495_101_var, type = 'LBS', name= '84495_101')



switch_84429_103_var = True
switch_84429_103 = pp.create_switch(net, bus_84429_1, bus_84429_2, et='b', closed=switch_84429_103_var, type = 'LBS', name= '84429_103')

switch_84453_102_var = True
switch_84453_102 = pp.create_switch(net, bus_84453_1, bus_84453_2, et='b', closed=switch_84453_102_var, type = 'LBS', name= '84453_102')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84429_2, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84429")

pp.create_load(net, bus=bus_84429_2, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84429_2")

pp.create_load(net, bus=bus_84427, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84427")

pp.create_load(net, bus=bus_84428, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84428")

pp.create_load(net, bus=bus_84428, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84428_2")

pp.create_load(net, bus=bus_84453_2, p_mw=1.00*demand_profiles.at[t, 'lab_oud'], name="Load_84453_2")

pp.create_load(net, bus=bus_84453_1, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84453_1")

pp.create_load(net, bus=bus_84453_1, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84453_1_2")

pp.create_load(net, bus=bus_84495, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84495")

pp.create_load(net, bus=bus_84495, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84495_2")




pp.create_sgen(net, bus=bus_84429_1, p_mw=0.2333*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84429_1')

pp.create_sgen(net, bus=bus_84427, p_mw=0.107*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84427')



###################################################################### veld 84460_2 202 (Jenalaan WKC) (Donkergroen) ###############################################################




###   Busjes   ###

bus_84434 = pp.create_bus(net, vn_kv = 10., name = '84434', type = 'n')

bus_84467 = pp.create_bus(net, vn_kv = 10., name = '84467', type = 'n')

bus_84498 = pp.create_bus(net, vn_kv = 10., name = '84498', type = 'n')




###   Lijnen   ###

line_84460_2_84434 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_84434, length_km=0.4, name='84460_2_84434',std_type="150_XLPE")

line_84434_84495 = pp.create_line(net, from_bus=bus_84434, to_bus=bus_84495, length_km=0.1, name='84434_84495',std_type="50_XLPE")

line_84434_84467 = pp.create_line(net, from_bus=bus_84434, to_bus=bus_84467, length_km=0.1, name='84434_84467',std_type="50_XLPE")

line_84467_84498 = pp.create_line(net, from_bus=bus_84467, to_bus=bus_84498, length_km=0.1, name='84467_84498',std_type="50_XLPE")




###   Schakelaars   ###

#switch_84460_202_var = True
#switch_84460_202 = pp.create_switch(net, bus_84460_2, line_84460_2_84434, et='l', closed=switch_84460_202_var, type = 'LBS', name= '84460_202')

switch_84434_103_var = True
switch_84434_103 = pp.create_switch(net, bus_84434, line_84460_2_84434, et='l', closed=switch_84434_103_var, type = 'LBS', name= '84434_103')

switch_84434_101_var = False   ### Sectoropening??
switch_84434_101 = pp.create_switch(net, bus_84434, line_84434_84495, et='l', closed=switch_84434_101_var, type = 'LBS', name= '84434_101')

#switch_84434_102_var = True
#switch_84434_102 = pp.create_switch(net, bus_84434, line_84434_84467, et='l', closed=switch_84434_102_var, type = 'LBS', name= '84434_102')

switch_84467_101_var = True
switch_84467_101 = pp.create_switch(net, bus_84467, line_84434_84467, et='l', closed=switch_84467_101_var, type = 'LBS', name= '84467_101')

#switch_84467_102_var = True
#switch_84467_102 = pp.create_switch(net, bus_84467, line_84467_84498, et='l', closed=switch_84467_102_var, type = 'LBS', name= '84467_102')

switch_84498_101_var = True
switch_84498_101 = pp.create_switch(net, bus_84498, line_84467_84498, et='l', closed=switch_84498_101_var, type = 'LBS', name= '84498_101')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84434, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84434")

pp.create_load(net, bus=bus_84434, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84434_2")

pp.create_load(net, bus=bus_84467, p_mw=1.00*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84467")

pp.create_load(net, bus=bus_84498, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84498")




###################################################################### veld 84460_2 203 (Jenalaan WKC) (Donkerblauw) ###############################################################




###   Busjes   ###

bus_84447 = pp.create_bus(net, vn_kv = 10., name = '84447', type = 'n')

bus_84443_1 = pp.create_bus(net, vn_kv = 10., name = '84443_1', type = 'b')

bus_84443_2 = pp.create_bus(net, vn_kv = 10., name = '84443_2', type = 'b')

bus_84417 = pp.create_bus(net, vn_kv = 10., name = '84417', type = 'n')

bus_4898 = pp.create_bus(net, vn_kv = 10., name = '4898', type = 'n')

bus_84481 = pp.create_bus(net, vn_kv = 10., name = '84481', type = 'n')




###   Lijnen   ###

line_84460_2_84447 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_84447, length_km=0.7, name='84460_2_84447',std_type="50_XLPE")

line_84447_84443_1 = pp.create_line(net, from_bus=bus_84447, to_bus=bus_84443_1, length_km=0.6, name='84447_84443_1',std_type="50_XLPE")

line_84443_2_84417 = pp.create_line(net, from_bus=bus_84443_2, to_bus=bus_84417, length_km=0.5, name='84443_2_84417',std_type="50")

line_84417_4898 = pp.create_line(net, from_bus=bus_84417, to_bus=bus_4898, length_km=0.1, name='84417_4898',std_type="50_XLPE")

line_4898_84481 = pp.create_line(net, from_bus=bus_4898, to_bus=bus_84481, length_km=0.1, name='4898_84481',std_type="50_XLPE")

line_84481_84498 = pp.create_line(net, from_bus=bus_84481, to_bus=bus_84498, length_km=0.9, name='84481_84498',std_type="50")




###   Schakelaars   ###

#switch_84460_203_var = True
#switch_84460_203 = pp.create_switch(net, bus_84460_2, line_84460_2_84447, et='l', closed=switch_84460_203_var, type = 'LBS', name= '84460_203')

switch_84447_101_var = True
switch_84447_101 = pp.create_switch(net, bus_84447, line_84460_2_84447, et='l', closed=switch_84447_101_var, type = 'LBS', name= '84447_101')

#switch_84447_102_var = True
#switch_84447_102 = pp.create_switch(net, bus_84447, line_84447_84443_1, et='l', closed=switch_84447_102_var, type = 'LBS', name= '84447_102')

switch_84443_101_var = True
switch_84443_101 = pp.create_switch(net, bus_84443_1, line_84447_84443_1, et='l', closed=switch_84443_101_var, type = 'LBS', name= '84443_101')

#switch_84443_203_var = True
#switch_84443_203 = pp.create_switch(net, bus_84443_2, line_84443_2_84417, et='l', closed=switch_84443_203_var, type = 'LBS', name= '84443_203')

switch_84417_101_var = True
switch_84417_101 = pp.create_switch(net, bus_84417, line_84443_2_84417, et='l', closed=switch_84417_101_var, type = 'LBS', name= '84417_101')

#switch_84417_102_var = True
#switch_84417_102 = pp.create_switch(net, bus_84417, line_84417_4898, et='l', closed=switch_84417_102_var, type = 'LBS', name= '84417_102')

switch_4898_101_var = True
switch_4898_101 = pp.create_switch(net, bus_4898, line_84417_4898, et='l', closed=switch_4898_101_var, type = 'LBS', name= '4898_101')

#switch_4898_102_var = True
#switch_4898_102 = pp.create_switch(net, bus_4898, line_4898_84481, et='l', closed=switch_4898_102_var, type = 'LBS', name= '4898_102')

switch_84481_101_var = True
switch_84481_101 = pp.create_switch(net, bus_84481, line_4898_84481, et='l', closed=switch_84481_101_var, type = 'LBS', name= '84481_101')

switch_84481_102_var = False   ### sectoropening?
switch_84481_102 = pp.create_switch(net, bus_84481, line_84481_84498, et='l', closed=switch_84481_102_var, type = 'LBS', name= '84481_102')



switch_84443_102_var = True
switch_84443_102 = pp.create_switch(net, bus_84443_1, bus_84443_2, et='b', closed=switch_84443_102_var, type = 'LBS', name= '84443_102')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84447, p_mw=0.10*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84447")

pp.create_load(net, bus=bus_84443_1, p_mw=0.60*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84443_1")

pp.create_load(net, bus=bus_84443_1, p_mw=0.30*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84443_1_2")

pp.create_load(net, bus=bus_84417, p_mw=0.315*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84417")  #achterin de botu, windmolens kunne ook aan 84481

pp.create_load(net, bus=bus_4898, p_mw=1.00*0.5, name="Load_4898")    #Parkeergarage, aangenomen constante vermogensvraag op halve capaciteit.

pp.create_load(net, bus=bus_84481, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84481")



pp.create_load(net, bus=bus_4898, p_mw=0.2*demand_profiles.at[t, 'ev_simpel'], name="ev_4898") #200 laadpalen


#bus_wind = pp.create_bus(net, vn_kv = 10., name = 'bus_wind', type = 'n')
#line_wind = pp.create_line(net, from_bus=bus_wind, to_bus=bus_sorbonne, length_km=0.9, name='lijn_wind',std_type="630_AL_XLPE")
pp.create_sgen(net, bus=bus_84417, p_mw=demand_profiles.at[t, 'windmolen_3_MW'], name='windmolen_1')
pp.create_sgen(net, bus=bus_84417, p_mw=demand_profiles.at[t, 'windmolen_3_MW'], name='windmolen_2')

pp.create_sgen(net, bus=bus_84443_1, p_mw=0.2113*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84443_1')  #dak Ruppert

pp.create_sgen(net, bus=bus_4898, p_mw=0.3368*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_4898') #parkeergarage olympos





###################################################################### veld 84460_2 206 (Jenalaan WKC) (Rood) ###############################################################




###   Busjes   ###

bus_8193 = pp.create_bus(net, vn_kv = 10., name = '8193', type = 'n')

bus_8194 = pp.create_bus(net, vn_kv = 10., name = '8194', type = 'n')

bus_8195 = pp.create_bus(net, vn_kv = 10., name = '8195', type = 'n')

bus_84494_3 = pp.create_bus(net, vn_kv = 10., name = '84494_3', type = 'b')

bus_84494_2 = pp.create_bus(net, vn_kv = 10., name = '84494_2', type = 'b')

bus_84494_1 = pp.create_bus(net, vn_kv = 10., name = '84494_1', type = 'b')




###   Lijnen   ###

line_84460_2_8193 = pp.create_line(net, from_bus=bus_84460_2, to_bus=bus_8193, length_km=1.0, name='84460_2_8193',std_type="240_AL_XLPE")

line_8193_8194 = pp.create_line(net, from_bus=bus_8193, to_bus=bus_8194, length_km=0.1, name='8193_8194',std_type="240_AL_XLPE")

line_8194_8195 = pp.create_line(net, from_bus=bus_8194, to_bus=bus_8195, length_km=0.1, name='8194_8195',std_type="240_AL_XLPE")

line_8195_84494_3 = pp.create_line(net, from_bus=bus_8195, to_bus=bus_84494_3, length_km=0.4, name='8195_84494_3',std_type="240_AL_XLPE")

line_84494_1_84443_2 = pp.create_line(net, from_bus=bus_84494_1, to_bus=bus_84443_2, length_km=0.3, name='84494_1_84443_2',std_type="50_XLPE")




###   Schakelaars   ###

#switch_84460_206_var = True
#switch_84460_206 = pp.create_switch(net, bus_84460_2, line_84460_2_8193, et='l', closed=switch_84460_206_var, type = 'LBS', name= '84460_206')

switch_8193_101_var = True
switch_8193_101 = pp.create_switch(net, bus_8193, line_84460_2_8193, et='l', closed=switch_8193_101_var, type = 'LBS', name= '8193_101')

#switch_8193_102_var = True
#switch_8193_102 = pp.create_switch(net, bus_8193, line_8193_8194, et='l', closed=switch_8193_102_var, type = 'LBS', name= '8193_102')

switch_8194_101_var = True
switch_8194_101 = pp.create_switch(net, bus_8194, line_8193_8194, et='l', closed=switch_8194_101_var, type = 'LBS', name= '8194_101')

#switch_8194_102_var = True
#switch_8194_102 = pp.create_switch(net, bus_8194, line_8194_8195, et='l', closed=switch_8194_102_var, type = 'LBS', name= '8194_102')

switch_8195_101_var = True
switch_8195_101 = pp.create_switch(net, bus_8195, line_8194_8195, et='l', closed=switch_8195_101_var, type = 'LBS', name= '8195_101')

#switch_8195_102_var = True
#switch_8195_102 = pp.create_switch(net, bus_8195, line_8195_84494_3, et='l', closed=switch_8195_102_var, type = 'LBS', name= '8195_102')

switch_84494_301_var = True
switch_84494_301 = pp.create_switch(net, bus_84494_3, line_8195_84494_3, et='l', closed=switch_84494_301_var, type = 'LBS', name= '84494_301')

#switch_84494_101_var = True
#switch_84494_101 = pp.create_switch(net, bus_84494_1, line_84494_1_84443_2, et='l', closed=switch_84494_101_var, type = 'LBS', name= '84494_101')

switch_84443_202_var = False   ### sectoropening
switch_84443_202 = pp.create_switch(net, bus_84443_2, line_84494_1_84443_2, et='l', closed=switch_84443_202_var, type = 'LBS', name= '84443_202')



switch_84494_201_var = True
switch_84494_201 = pp.create_switch(net, bus_84494_2, bus_84494_3, et='b', closed=switch_84494_201_var, type = 'LBS', name= '84494_201')

switch_84494_102_var = True
switch_84494_102 = pp.create_switch(net, bus_84494_1, bus_84494_2, et='b', closed=switch_84494_102_var, type = 'LBS', name= '84494_102')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_8193, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_8193")

pp.create_load(net, bus=bus_8194, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_8194")

pp.create_load(net, bus=bus_8195, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_8195")

pp.create_load(net, bus=bus_84494_2, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84494_2")

pp.create_load(net, bus=bus_84494_2, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84494_2_2")

pp.create_load(net, bus=bus_84494_1, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84494_1")




pp.create_sgen(net, bus=bus_8193, p_mw=0.1231*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_8193')

pp.create_sgen(net, bus=bus_84494_1, p_mw=0.2322*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84494_1')