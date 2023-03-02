# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:14:08 2023

@author: battuejd
"""

import pandas as pd
import pandapower as pp


#import load_usp_grid


demand_profiles = pd.DataFrame(pd.read_excel('Input Data/Overzicht lasten en generatie.xlsx', 'profielen_1_dag', index_col=('Uur:')))

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




###################################################################### veld 119 (Roze) ###############################################################




###   Busjes   ###

bus_1884 = pp.create_bus(net, vn_kv = 10., name = '1884', type = 'n')

bus_84474 = pp.create_bus(net, vn_kv = 10., name = '84474', type = 'n')

bus_2354 = pp.create_bus(net, vn_kv = 10., name = '2354', type = 'n')

bus_84446 = pp.create_bus(net, vn_kv = 10., name = '84446', type = 'n')

bus_84483 = pp.create_bus(net, vn_kv = 10., name = '84483', type = 'n')

bus_1834 = pp.create_bus(net, vn_kv = 10., name = '1834', type = 'n')

bus_3406 = pp.create_bus(net, vn_kv = 10., name = '3406', type = 'n')

bus_84499 = pp.create_bus(net, vn_kv = 10., name = '84499', type = 'n')




###   Lijnen   ###

line_sorbonne_1884 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_1884, length_km=0.3, name='sorbonne_1884',std_type="150_XLPE")

line_1884_84474 = pp.create_line(net, from_bus=bus_1884, to_bus=bus_84474, length_km=0.6, name='1884_84474',std_type="150_XLPE")

line_84474_2354 = pp.create_line(net, from_bus=bus_84474, to_bus=bus_2354, length_km=0.3, name='84474_2354',std_type="150_XLPE")

line_2354_84446 = pp.create_line(net, from_bus=bus_2354, to_bus=bus_84446, length_km=0.2, name='2354_84446',std_type="150_XLPE")

line_84446_84483 = pp.create_line(net, from_bus=bus_84446, to_bus=bus_84483, length_km=0.1, name='84446_84483',std_type="150_XLPE")

line_84483_1834 = pp.create_line(net, from_bus=bus_84483, to_bus=bus_1834, length_km=0.1, name='84483_1834',std_type="150_XLPE")

line_1834_3406 = pp.create_line(net, from_bus=bus_1834, to_bus=bus_3406, length_km=0.1, name='1834_3406',std_type="150_XLPE")

line_3406_84499 = pp.create_line(net, from_bus=bus_3406, to_bus=bus_84499, length_km=0.1, name='3406_84499',std_type="150_XLPE")




###   Schakelaars   ###

switch_1884_101_var = True
switch_1884_101 = pp.create_switch(net, bus_1884, line_sorbonne_1884, et='l', closed=switch_1884_101_var, type = 'LBS', name= '1884_101')

#switch_1884_102_var = True
#switch_1884_102 = pp.create_switch(net, bus_1884, line_1884_84474, et='l', closed=switch_1884_102_var, type = 'LBS', name= '1884_102')

switch_84474_102_var = True
switch_84474_102 = pp.create_switch(net, bus_84474, line_1884_84474, et='l', closed=switch_84474_102_var, type = 'LBS', name= '84474_102')

#switch_84474_101_var = True
#switch_84474_101 = pp.create_switch(net, bus_84474, line_84474_2354, et='l', closed=switch_84474_101_var, type = 'LBS', name= '84474_101')

switch_2354_102_var = True
switch_2354_102 = pp.create_switch(net, bus_2354, line_84474_2354, et='l', closed=switch_2354_102_var, type = 'LBS', name= '2354_102')

#switch_2354_101_var = True
#switch_2354_101 = pp.create_switch(net, bus_2354, line_2354_84446, et='l', closed=switch_2354_101_var, type = 'LBS', name= '2354_101')

switch_84446_101_var = True
switch_84446_101 = pp.create_switch(net, bus_84446, line_2354_84446, et='l', closed=switch_84446_101_var, type = 'LBS', name= '84446_101')

#switch_84446_102_var = True
#switch_84446_102 = pp.create_switch(net, bus_84446, line_84446_84483, et='l', closed=switch_84446_102_var, type = 'LBS', name= '84446_102')

switch_84483_101_var = True
switch_84483_101 = pp.create_switch(net, bus_84483, line_84446_84483, et='l', closed=switch_84483_101_var, type = 'LBS', name= '84483_101')

#switch_84483_102_var = True
#switch_84483_102 = pp.create_switch(net, bus_84483, line_84483_1834, et='l', closed=switch_84483_102_var, type = 'LBS', name= '84483_102')

switch_1834_101_var = True
switch_1834_101 = pp.create_switch(net, bus_1834, line_84483_1834, et='l', closed=switch_1834_101_var, type = 'LBS', name= '1834_101')

#switch_1834_102_var = True
#switch_1834_102 = pp.create_switch(net, bus_1834, line_1834_3406, et='l', closed=switch_1834_102_var, type = 'LBS', name= '1834_102')

switch_3406_101_var = True
switch_3406_101 = pp.create_switch(net, bus_3406, line_1834_3406, et='l', closed=switch_3406_101_var, type = 'LBS', name= '3406_101')

#switch_3406_102_var = True
#switch_3406_102 = pp.create_switch(net, bus_3406, line_3406_84499, et='l', closed=switch_3406_102_var, type = 'LBS', name= '3406_102')

switch_84499_102_var = True
switch_84499_102 = pp.create_switch(net, bus_84499, line_3406_84499, et='l', closed=switch_84499_102_var, type = 'LBS', name= '84499_102')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_1884, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_1884")

pp.create_load(net, bus=bus_84474, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84474")

pp.create_load(net, bus=bus_2354, p_mw=1.60*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_2354")

pp.create_load(net, bus=bus_84446, p_mw=0.16*demand_profiles.at[t, 'lab_oud'], name="Load_84446")     #Bijgebouwtje riooldienst ofzo, misschien iets beters verzinnen

pp.create_load(net, bus=bus_84483, p_mw=(demand_profiles.at[t, 'res_1']/14.5)*0.63, name="Load_84483")

pp.create_load(net, bus=bus_1834, p_mw=1.25*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_1834")

pp.create_load(net, bus=bus_3406, p_mw=1.60*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_3406")

pp.create_load(net, bus=bus_84499, p_mw=1.00*(demand_profiles.at[t, 'res_2']/14.5), name="Load_84499")


#bus_zonpv_rivmoost = pp.create_bus(net, vn_kv = 10., name = 'bus_zonpv_rivmoost', type = 'n')
#line_zonpv_rivmoost = pp.create_line(net, from_bus=bus_zonpv_rivmoost, to_bus=bus_sorbonne, length_km=0.3, name='lijn_zonpv_rivmoost',std_type="630_AL_XLPE")
pp.create_sgen(net, bus=bus_84474, p_mw=3.5*demand_profiles.at[t, 'pv_veld_1_MW'], name='zonpv_rivmoost') #1 deel van de 10.5ha 12.5mw nature inclusive pv fields (andere deel op oostelijke tolakkervelden)




################################################################################## veld 213 (Oranje) #########################################################################




###   Busjes   ###

bus_8258 = pp.create_bus(net, vn_kv = 10., name = '8528', type = 'b')

bus_84426 = pp.create_bus(net, vn_kv = 10., name = '84426', type = 'n')

bus_8246 = pp.create_bus(net, vn_kv = 10., name = '8246', type = 'n')

bus_84489 = pp.create_bus(net, vn_kv = 10., name = '84489', type = 'n')

bus_8431 = pp.create_bus(net, vn_kv = 10., name = '8431', type = 'n')

bus_2596 = pp.create_bus(net, vn_kv = 10., name = '2596', type = 'n')

bus_7978 = pp.create_bus(net, vn_kv = 10., name = '7978', type = 'n')




###   Lijnen   ###

line_sorbonne_8258 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_8258, length_km=1.5, name='sorbonne_8258',std_type="240_AL_XLPE")

line_8258_84426 = pp.create_line(net, from_bus=bus_8258, to_bus=bus_84426, length_km=0.1, name='8258_84426',std_type="150_AL_XLPE")

line_84426_8246 = pp.create_line(net, from_bus=bus_84426, to_bus=bus_8246, length_km=0.1, name='84426_8246',std_type="150_AL_XLPE")

#line_8246_84489 = pp.create_line(net, from_bus=bus_8246, to_bus=bus_84489, length_km=0.1, name='8246_84489',std_type="150_AL_XLPE")

line_84489_8258 = pp.create_line(net, from_bus=bus_84489, to_bus=bus_8258, length_km=0.1, name='84489_8258',std_type="150_AL_XLPE")

line_8258_8431 = pp.create_line(net, from_bus=bus_8258, to_bus=bus_8431, length_km=0.1, name='8258_8431',std_type="150_XLPE")

line_8431_2596 = pp.create_line(net, from_bus=bus_8431, to_bus=bus_2596, length_km=0.1, name='8431_2596',std_type="240_AL_XLPE")

line_2596_7978 = pp.create_line(net, from_bus=bus_2596, to_bus=bus_7978, length_km=0.6, name='2596_7978',std_type="150_XLPE")

line_7978_84499 = pp.create_line(net, from_bus=bus_7978, to_bus=bus_84499, length_km=0.2, name='7978_84499',std_type="240_AL_XLPE")




###   Schakelaars   ###

#switch_8258_102_var = True
#switch_8258_102 = pp.create_switch(net, bus_8258, line_sorbonne_8258, et='l', closed=switch_8258_102_var, type = 'LBS', name= '8258_102')

#switch_8258_104_var = True
#switch_8258_104 = pp.create_switch(net, bus_8258, line_8258_84426, et='l', closed=switch_8258_104_var, type = 'LBS', name= '8258_104')

#switch_84426_101_var = True
#switch_84426_101 = pp.create_switch(net, bus_84426, line_8258_84426, et='l', closed=switch_84426_101_var, type = 'LBS', name= '84426_101')

#switch_84426_102_var = True
#switch_84426_102 = pp.create_switch(net, bus_84426, line_84426_8246, et='l', closed=switch_84426_102_var, type = 'LBS', name= '84426_102')

#switch_8246_101_var = True
#switch_8246_101 = pp.create_switch(net, bus_8246, line_84426_8246, et='l', closed=switch_8246_101_var, type = 'LBS', name= '8246_101')

#switch_8246_102_var = True
#switch_8246_102 = pp.create_switch(net, bus_8246, line_8246_84489, et='l', closed=switch_8246_102_var, type = 'LBS', name= '8246_102')

#switch_84489_101_var = False  ##### Sectoropening?
#switch_84489_101 = pp.create_switch(net, bus_84489, line_8246_84489, et='l', closed=switch_84489_101_var, type = 'LBS', name= '84489_101')

#switch_84489_102_var = True
#switch_84489_102 = pp.create_switch(net, bus_84489, line_84489_8258, et='l', closed=switch_84489_102_var, type = 'LBS', name= '84489_102')

#switch_8258_105_var = True
#switch_8258_105 = pp.create_switch(net, bus_8258, line_84489_8258, et='l', closed=switch_8258_105_var, type = 'LBS', name= '8258_105')

#switch_8258_101_var = True
#switch_8258_101 = pp.create_switch(net, bus_8258, line_8258_8431, et='l', closed=switch_8258_101_var, type = 'LBS', name= '8258_101')

switch_8431_101_var = True
switch_8431_101 = pp.create_switch(net, bus_8431, line_8258_8431, et='l', closed=switch_8431_101_var, type = 'LBS', name= '8431_101')

#switch_8431_102_var = True
#switch_8431_102 = pp.create_switch(net, bus_8431, line_8431_2596, et='l', closed=switch_8431_102_var, type = 'LBS', name= '8431_102')

switch_2596_101_var = True
switch_2596_101 = pp.create_switch(net, bus_2596, line_8431_2596, et='l', closed=switch_2596_101_var, type = 'LBS', name= '2596_101')

#switch_2596_102_var = True
#switch_2596_102 = pp.create_switch(net, bus_2596, line_2596_7978, et='l', closed=switch_2596_102_var, type = 'LBS', name= '2596_102')

switch_7978_102_var = True
switch_7978_102 = pp.create_switch(net, bus_7978, line_2596_7978, et='l', closed=switch_7978_102_var, type = 'LBS', name= '7978_102')

switch_7978_101_var = False   ### sectoropening
switch_7978_101 = pp.create_switch(net, bus_7978, line_7978_84499, et='l', closed=switch_7978_101_var, type = 'LBS', name= '7978_101')

#switch_84499_101_var = True
#switch_84499_101 = pp.create_switch(net, bus_84499, line_7978_84499, et='l', closed=switch_84499_101_var, type = 'LBS', name= '84499_101')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84426, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84426")

pp.create_load(net, bus=bus_8246, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_8246")

pp.create_load(net, bus=bus_84489, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84489")

pp.create_load(net, bus=bus_84489, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84489_2")

pp.create_load(net, bus=bus_8431, p_mw=0.40*0.5, name="Load_8431")    #parkeergarage, ingesteld op constante afname op half vermogen

pp.create_load(net, bus=bus_2596, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], name="Load_2596")

pp.create_load(net, bus=bus_7978, p_mw=0.630*(demand_profiles.at[t, 'res_2']/14.5), name="Load_7978")




################################################################################## veld 109 (Geel) #########################################################################




###   Busjes   ###

bus_84437 = pp.create_bus(net, vn_kv = 10., name = '84437', type = 'n')

bus_84436_3 = pp.create_bus(net, vn_kv = 10., name = '84436_3', type = 'b')




###   Lijnen   ###

line_sorbonne_84437 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84437, length_km=0.7, name='sorbonne_84437',std_type="150_AL_XLPE")

line_84437_84436_3 = pp.create_line(net, from_bus=bus_84437, to_bus=bus_84436_3, length_km=0.1, name='84437_84436_3',std_type="95")




###   Schakelaars   ###

switch_84437_101_var = True
switch_84437_101 = pp.create_switch(net, bus_84437, line_sorbonne_84437, et='l', closed=switch_84437_101_var, type = 'LBS', name= '84437_101')

#switch_84437_102_var = True
#switch_84437_102 = pp.create_switch(net, bus_84437, line_84437_84436_3, et='l', closed=switch_84437_102_var, type = 'LBS', name= '84437_102')

switch_84436_304_var = True
switch_84436_304 = pp.create_switch(net, bus_84436_3, line_84437_84436_3, et='l', closed=switch_84436_304_var, type = 'LBS', name= '84436_304')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84437, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84437")

pp.create_load(net, bus=bus_84436_3, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84436_3")



#bus_zonpv_rivmnoord = pp.create_bus(net, vn_kv = 10., name = 'bus_zonpv_rivmnoord', type = 'n')
#line_zonpv_rivmnoord = pp.create_line(net, from_bus=bus_zonpv_rivmnoord, to_bus=bus_sorbonne, length_km=0.3, name='lijn_zonpv_rivmnoord',std_type="630_AL_XLPE")
pp.create_sgen(net, bus=bus_84437, p_mw=2.5*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_rivmnoord') #1 helft van de 4ha 5mw research pv fields (andere helft op schapenveld)



################################################################################## veld 114 (Paars) #########################################################################




###   Busjes   ###

bus_84421 = pp.create_bus(net, vn_kv = 10., name = '84421', type = 'n')

bus_84422_1 = pp.create_bus(net, vn_kv = 10., name = '84422_1', type = 'b')

bus_84422_2 = pp.create_bus(net, vn_kv = 10., name = '84422_2', type = 'b')

bus_8534 = pp.create_bus(net, vn_kv = 10., name = '8534', type = 'n')

bus_2536 = pp.create_bus(net, vn_kv = 10., name = '2536', type = 'n')

bus_84490 = pp.create_bus(net, vn_kv = 10., name = '84490', type = 'n')




###   Lijnen   ###

line_sorbonne_84421 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84421, length_km=0.8, name='sorbonne_84421',std_type="150_AL_XLPE")

line_84421_84422_1 = pp.create_line(net, from_bus=bus_84421, to_bus=bus_84422_1, length_km=0.1, name='84421_84422_1',std_type="95_XLPE")

line_84422_2_8534 = pp.create_line(net, from_bus=bus_84422_2, to_bus=bus_8534, length_km=0.1, name='84422_2_8534',std_type="95_XLPE")

line_8534_2536 = pp.create_line(net, from_bus=bus_8534, to_bus=bus_2536, length_km=0.1, name='8535_2536',std_type="95_AL_XLPE")

line_2536_84490 = pp.create_line(net, from_bus=bus_2536, to_bus=bus_84490, length_km=0.1, name='2536_84490',std_type="95_XLPE")




###   Schakelaars   ###

switch_84421_101_var = True
switch_84421_101 = pp.create_switch(net, bus_84421, line_sorbonne_84421, et='l', closed=switch_84421_101_var, type = 'LBS', name= '84421_101')

#switch_84421_102_var = True
#switch_84421_102 = pp.create_switch(net, bus_84421, line_84421_84422_1, et='l', closed=switch_84421_102_var, type = 'LBS', name= '84421_102')

switch_84422_101_var = True
switch_84422_101 = pp.create_switch(net, bus_84422_1, line_84421_84422_1, et='l', closed=switch_84422_101_var, type = 'LBS', name= '84422_101')

#switch_84422_202_var = True
#switch_84422_202 = pp.create_switch(net, bus_84422_2, line_84422_2_8534, et='l', closed=switch_84422_202_var, type = 'LBS', name= '84422_202')

switch_8534_101_var = True
switch_8534_101 = pp.create_switch(net, bus_8534, line_84422_2_8534, et='l', closed=switch_8534_101_var, type = 'LBS', name= '8534_101')

#switch_8534_102_var = True
#switch_8534_102 = pp.create_switch(net, bus_8534, line_8534_2536, et='l', closed=switch_8534_102_var, type = 'LBS', name= '8534_102')

switch_2536_101_var = True
switch_2536_101 = pp.create_switch(net, bus_2536, line_8534_2536, et='l', closed=switch_2536_101_var, type = 'LBS', name= '2536_101')

#switch_2536_102_var = True
#switch_2536_102 = pp.create_switch(net, bus_2536, line_2536_84490, et='l', closed=switch_2536_102_var, type = 'LBS', name= '2536_102')

switch_84490_101_var = True
switch_84490_101 = pp.create_switch(net, bus_84490, line_2536_84490, et='l', closed=switch_84490_101_var, type = 'LBS', name= '84490_101')



switch_84422_102_var = True
switch_84422_102 = pp.create_switch(net, bus_84422_1, bus_84422_2, et='b', closed=switch_84422_102_var, type = 'LBS', name= '84422_102')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84421, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84421_1")

pp.create_load(net, bus=bus_84421, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84421_2")

pp.create_load(net, bus=bus_84421, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84421_3")

pp.create_load(net, bus=bus_84421, p_mw=0.075*demand_profiles.at[t, 'lab_oud'], name="Load_84421_4")

pp.create_load(net, bus=bus_84422_1, p_mw=0.40*demand_profiles.at[t, 'lab_nieuw'], name="Load_84422_1_1")

pp.create_load(net, bus=bus_84422_1, p_mw=0.40*demand_profiles.at[t, 'lab_oud'], name="Load_84422_1_2")

pp.create_load(net, bus=bus_84422_2, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84422_2_1")

pp.create_load(net, bus=bus_84422_2, p_mw=0.25*demand_profiles.at[t, 'lab_oud'], name="Load_84422_2_2")

pp.create_load(net, bus=bus_8534, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], name="Load_8534")

pp.create_load(net, bus=bus_2536, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], name="Load_2536")

pp.create_load(net, bus=bus_84490, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84490_1")

pp.create_load(net, bus=bus_84490, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_84490_2")


pp.create_sgen(net, bus=bus_84421, p_mw=0.1323*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84421')  #C. Bleeker gebouw

pp.create_sgen(net, bus=bus_84490, p_mw=0.136*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84490')  #VMC (TNO)


pp.create_sgen(net, bus=bus_2536, p_mw=0.0405*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_2536') #pv earth simul lab




################################################################################## veld 113 (Grijs) #########################################################################




###   Busjes   ###

bus_84444 = pp.create_bus(net, vn_kv = 10., name = '84444', type = 'n')

bus_84440 = pp.create_bus(net, vn_kv = 10., name = '84440', type = 'b')

bus_84442_1 = pp.create_bus(net, vn_kv = 10., name = '84442_1', type = 'b')

bus_84442_3 = pp.create_bus(net, vn_kv = 10., name = '84442_3', type = 'b')

bus_84442_4 = pp.create_bus(net, vn_kv = 10., name = '84442_4', type = 'b')




###   Lijnen   ###

line_sorbonne_84444 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84444, length_km=1.0, name='sorbonne_84444',std_type="150_AL_XLPE")

line_84444_84440 = pp.create_line(net, from_bus=bus_84444, to_bus=bus_84440, length_km=0.2, name='84444_84440',std_type="150_AL_XLPE")

line_84440_84442_k3 = pp.create_line(net, from_bus=bus_84440, to_bus=bus_84442_1, length_km=0.1, name='84440_84442_k3',std_type="50")

line_84440_84442_k2 = pp.create_line(net, from_bus=bus_84440, to_bus=bus_84442_3, length_km=0.1, name='84440_84442_k2',std_type="50")

line_84440_84442_k1 = pp.create_line(net, from_bus=bus_84440, to_bus=bus_84442_4, length_km=0.1, name='84440_84442_k1',std_type="50")




###   Schakelaars   ###

switch_84444_101_var = True
switch_84444_101 = pp.create_switch(net, bus_84444, line_sorbonne_84444, et='l', closed=switch_84444_101_var, type = 'LBS', name= '84444_101')

#switch_84444_102_var = True
#switch_84444_102 = pp.create_switch(net, bus_84444, line_84444_84440, et='l', closed=switch_84444_102_var, type = 'LBS', name= '84444_102')

switch_84440_203_var = True
switch_84440_203 = pp.create_switch(net, bus_84440, line_84444_84440, et='l', closed=switch_84440_203_var, type = 'LBS', name= '84440_203')

#switch_84440_302_var = True
#switch_84440_302 = pp.create_switch(net, bus_84440, line_84440_84442_k3, et='l', closed=switch_84440_302_var, type = 'LBS', name= '84440_302')

#switch_84440_303_var = True
#switch_84440_303 = pp.create_switch(net, bus_84440, line_84440_84442_k2, et='l', closed=switch_84440_303_var, type = 'LBS', name= '84440_303')

#switch_84440_304_var = True
#switch_84440_304 = pp.create_switch(net, bus_84440, line_84440_84442_k1, et='l', closed=switch_84440_304_var, type = 'LBS', name= '84440_304')

switch_84442_101_var = True
switch_84442_101 = pp.create_switch(net, bus_84442_1, line_84440_84442_k3, et='l', closed=switch_84442_101_var, type = 'LBS', name= '84442_101')

switch_84442_103_var = True
switch_84442_103 = pp.create_switch(net, bus_84442_3, line_84440_84442_k2, et='l', closed=switch_84442_103_var, type = 'LBS', name= '84442_103')

#switch_84442_104_var = True
#switch_84442_104 = pp.create_switch(net, bus_84442_4, line_84440_84442_k1, et='l', closed=switch_84442_104_var, type = 'LBS', name= '84442_104')



#switch_84442_102_var = False   ### sectoropening
#switch_84442_102 = pp.create_switch(net, bus_84442_1, bus_84442_3, et='b', closed=switch_84442_102_var, type = 'LBS', name= '84442_102')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84444, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84444")

pp.create_load(net, bus=bus_84440, p_mw=0.40*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84440")

pp.create_load(net, bus=bus_84442_1, p_mw=0.40*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84442_1")

pp.create_load(net, bus=bus_84442_3, p_mw=0.25*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84442_3")

pp.create_load(net, bus=bus_84442_4, p_mw=0.25*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84442_4")



pp.create_sgen(net, bus=bus_84444, p_mw=0.0288*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_84444') #Langeveldgebouw




################################################################################## veld 206 (Lichtgroen) #########################################################################




###   Busjes   ###

bus_84407 = pp.create_bus(net, vn_kv = 10., name = '84407', type = 'n')

bus_84480 = pp.create_bus(net, vn_kv = 10., name = '84480', type = 'n')




###   Lijnen   ###

line_sorbonne_84407 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84407, length_km=1.5, name='sorbonne_84407',std_type="240_AL_XLPE")

line_84407_84480 = pp.create_line(net, from_bus=bus_84407, to_bus=bus_84480, length_km=0.7, name='84407_84480',std_type="95_XLPE")




###   Schakelaars   ###

switch_84407_101_var = True
switch_84407_101 = pp.create_switch(net, bus_84407, line_sorbonne_84407, et='l', closed=switch_84407_101_var, type = 'LBS', name= '84407_101')

#switch_84407_102_var = True
#switch_84407_102 = pp.create_switch(net, bus_84407, line_84407_84480, et='l', closed=switch_84407_102_var, type = 'LBS', name= '84407_102')

switch_84480_101_var = True
switch_84480_101 = pp.create_switch(net, bus_84480, line_84407_84480, et='l', closed=switch_84480_101_var, type = 'LBS', name= '84480_101')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84407, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], name="Load_84407_1")

pp.create_load(net, bus=bus_84407, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], name="Load_84407_2")

pp.create_load(net, bus=bus_84480, p_mw=0.25*0.5, name="Load_84480")    #parkeergarage




################################################################################## veld 116 (Lichtblauw) #########################################################################




###   Busjes   ###

bus_84468 = pp.create_bus(net, vn_kv = 10., name = '84468', type = 'n')

bus_4412 = pp.create_bus(net, vn_kv = 10., name = '4412', type = 'n')

bus_1661 = pp.create_bus(net, vn_kv = 10., name = '1661', type = 'n')

bus_1660 = pp.create_bus(net, vn_kv = 10., name = '1660', type = 'n')

bus_84470 = pp.create_bus(net, vn_kv = 10., name = '84470', type = 'n')



#bus_UMC = pp.create_bus(net, vn_kv = 10., name = 'UMC', type = 'b')




###   Lijnen   ###

line_sorbonne_84468 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_84468, length_km=1.0, name='sorbonne_84468',std_type="240_AL_XLPE")

line_84468_4412 = pp.create_line(net, from_bus=bus_84468, to_bus=bus_4412, length_km=0.4, name='84468_4412',std_type="240_AL_XLPE")

line_4412_1661 = pp.create_line(net, from_bus=bus_4412, to_bus=bus_1661, length_km=0.1, name='4412_1661',std_type="95_XLPE")

line_1661_1660 = pp.create_line(net, from_bus=bus_1661, to_bus=bus_1660, length_km=0.1, name='1661_1660',std_type="150_AL_XLPE")

line_1660_84470 = pp.create_line(net, from_bus=bus_1660, to_bus=bus_84470, length_km=0.6, name='1660_84470',std_type="95_XLPE")

line_84470_84480 = pp.create_line(net, from_bus=bus_84470, to_bus=bus_84480, length_km=0.1, name='84470_84480',std_type="95_XLPE")



#line_sorbonne_UMC_k1 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_UMC, length_km=1.3, name='sorbonne_UMC_k1',std_type="630_AL_XLPE")

#line_sorbonne_UMC_k2 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_UMC, length_km=1.3, name='sorbonne_UMC_k2',std_type="630_AL_XLPE")

#line_deBilt_UMC = pp.create_line(net, from_bus=bus_deBilt, to_bus=bus_UMC, length_km=2.3, name='deBilt_UMC',std_type="150_XLPE")

#line_84470_UMC = pp.create_line(net, from_bus=bus_84470, to_bus=bus_UMC, length_km=0.1, name='84470_UMC',std_type="240_AL_XLPE")  #Kabeltype is in dit geval een aanname




###   Schakelaars   ###

switch_84468_101_var = True
switch_84468_101 = pp.create_switch(net, bus_84468, line_sorbonne_84468, et='l', closed=switch_84468_101_var, type = 'LBS', name= '84468_101')

#switch_84468_102_var = True
#switch_84468_102 = pp.create_switch(net, bus_84468, line_84468_4412, et='l', closed=switch_84468_102_var, type = 'LBS', name= '84468_102')

switch_4412_101_var = True
switch_4412_101 = pp.create_switch(net, bus_4412, line_84468_4412, et='l', closed=switch_4412_101_var, type = 'LBS', name= '4412_101')

#switch_4412_102_var = True
#switch_4412_102 = pp.create_switch(net, bus_4412, line_4412_1661, et='l', closed=switch_4412_102_var, type = 'LBS', name= '4412_102')

switch_1661_101_var = True
switch_1661_101 = pp.create_switch(net, bus_1661, line_4412_1661, et='l', closed=switch_1661_101_var, type = 'LBS', name= '1661_101')

#switch_1661_102_var = True
#switch_1661_102 = pp.create_switch(net, bus_1661, line_1661_1660, et='l', closed=switch_1661_102_var, type = 'LBS', name= '1661_102')

switch_1660_101_var = True
switch_1660_101 = pp.create_switch(net, bus_1660, line_1661_1660, et='l', closed=switch_1660_101_var, type = 'LBS', name= '1660_101')

#switch_1660_102_var = True
#switch_1660_102 = pp.create_switch(net, bus_1660, line_1660_84470, et='l', closed=switch_1660_102_var, type = 'LBS', name= '1660_102')

switch_84470_101_var = True
switch_84470_101 = pp.create_switch(net, bus_84470, line_1660_84470, et='l', closed=switch_84470_101_var, type = 'LBS', name= '84470_101')

switch_84470_102_var = False   ### sectoropening
switch_84470_102 = pp.create_switch(net, bus_84470, line_84470_84480, et='l', closed=switch_84470_102_var, type = 'LBS', name= '84470_102')

#switch_84470_103_var = True
#switch_84470_103 = pp.create_switch(net, bus_84470, line_84470_UMC, et='l', closed=switch_84470_103_var, type = 'LBS', name= '84470_103')

#switch_84480_102_var = True
#switch_84480_102 = pp.create_switch(net, bus_84480, line_84470_84480, et='l', closed=switch_84480_102_var, type = 'LBS', name= '84480_102')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_84468, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84468")

pp.create_load(net, bus=bus_4412, p_mw=1.00*(demand_profiles.at[t, 'res_2']/14.5), name="Load_4412")

pp.create_load(net, bus=bus_1661, p_mw=0.63*(demand_profiles.at[t, 'res_2']/14.5), name="Load_1661")

pp.create_load(net, bus=bus_1660, p_mw=0.25*(demand_profiles.at[t, 'res_2']/14.5), name="Load_1660")



#pp.create_load(net, bus=bus_UMC, p_mw=2.00, name="Load_UMC")      #Gokje, en eigenlijk irrelevant




pp.create_sgen(net, bus=bus_4412, p_mw=0.12*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_4412') #pv pilot van 0.5 ha. voor nu even op veldje achter camelot gepland, meer data onduidelijk




################################################################################## veld 106 (Lichtblauw) #########################################################################




###   Busjes   ###

bus_1922 = pp.create_bus(net, vn_kv = 10., name = '1922', type = 'n')

bus_8533 = pp.create_bus(net, vn_kv = 10., name = '8533', type = 'n')

bus_6999 = pp.create_bus(net, vn_kv = 10., name = '6999', type = 'n')

bus_6577 = pp.create_bus(net, vn_kv = 10., name = '6577', type = 'n')

bus_84436_1 = pp.create_bus(net, vn_kv = 10., name = '84436_1', type = 'b')

bus_2453 = pp.create_bus(net, vn_kv = 10., name = '2453', type = 'n')

bus_8563 = pp.create_bus(net, vn_kv = 10., name = '8563', type = 'n')

bus_84419 = pp.create_bus(net, vn_kv = 10., name = '84419', type = 'n')

bus_8505 = pp.create_bus(net, vn_kv = 10., name = '8505', type = 'n')



bus_84436_2 = pp.create_bus(net, vn_kv = 10., name = '84436_2', type = 'b')

bus_84435 = pp.create_bus(net, vn_kv = 10., name = '84435', type = 'n')

bus_84439 = pp.create_bus(net, vn_kv = 10., name = '84439', type = 'n')

bus_84438 = pp.create_bus(net, vn_kv = 10., name = '84438', type = 'b')

bus_4129_1 = pp.create_bus(net, vn_kv = 10., name = '4129_1', type = 'b')

bus_4129_2 = pp.create_bus(net, vn_kv = 10., name = '4129_2', type = 'b')




###   Lijnen   ###

line_sorbonne_1922 = pp.create_line(net, from_bus=bus_sorbonne, to_bus=bus_1922, length_km=0.2, name='sorbonne_1922',std_type="150_XLPE")

line_1922_8533 = pp.create_line(net, from_bus=bus_1922, to_bus=bus_8533, length_km=0.6, name='1922_8533',std_type="95_XLPE")

line_8533_6999 = pp.create_line(net, from_bus=bus_8533, to_bus=bus_6999, length_km=0.1, name='8533_6999',std_type="150_AL_XLPE")

line_6999_6577 = pp.create_line(net, from_bus=bus_6999, to_bus=bus_6577, length_km=0.1, name='6999_6577',std_type="150_AL_XLPE")

line_6577_84436_1 = pp.create_line(net, from_bus=bus_6577, to_bus=bus_84436_1, length_km=0.3, name='6577_84436',std_type="95_XLPE")

line_84436_1_2453 = pp.create_line(net, from_bus=bus_84436_1, to_bus=bus_2453, length_km=0.4, name='84436_1_2453',std_type="95_XLPE")

#line_2453_84494_3 = pp.create_line(net, from_bus=bus_2453, to_bus=bus_84494_3, length_km=0.7, name='2453_84494_3',std_type="240_AL_XLPE")

line_2453_8563 = pp.create_line(net, from_bus=bus_2453, to_bus=bus_8563, length_km=0.1, name='2453_8563',std_type="150_AL_XLPE")

line_8563_84419 = pp.create_line(net, from_bus=bus_8563, to_bus=bus_84419, length_km=0.1, name='8563_84419',std_type="95_XLPE")

line_84419_8505 = pp.create_line(net, from_bus=bus_84419, to_bus=bus_8505, length_km=0.1, name='84419_8505',std_type="95_XLPE")

line_8505_84490 = pp.create_line(net, from_bus=bus_8505, to_bus=bus_84490, length_km=0.1, name='8505_84490',std_type="150_AL_XLPE")

line_84436_2_84435 = pp.create_line(net, from_bus=bus_84436_2, to_bus=bus_84435, length_km=0.1, name='84436_2_84435',std_type="50")

line_84436_2_84439 = pp.create_line(net, from_bus=bus_84436_2, to_bus=bus_84439, length_km=0.1, name='84436_2_84439',std_type="95")

line_84439_84438 = pp.create_line(net, from_bus=bus_84439, to_bus=bus_84438, length_km=0.1, name='84439_84438',std_type="95")

line_84438_4129_1 = pp.create_line(net, from_bus=bus_84438, to_bus=bus_4129_1, length_km=0.2, name='84438_4129_1',std_type="150_AL_XLPE")

line_4129_2_84440 = pp.create_line(net, from_bus=bus_4129_2, to_bus=bus_84440, length_km=0.1, name='4129_2_84440_2',std_type="95_XLPE")




###   Schakelaars   ###

switch_1922_101_var = True
switch_1922_101 = pp.create_switch(net, bus_1922, line_sorbonne_1922, et='l', closed=switch_1922_101_var, type = 'LBS', name= '1922_101')

#switch_1922_102_var = True
#switch_1922_102 = pp.create_switch(net, bus_1922, line_1922_8533, et='l', closed=switch_1922_102_var, type = 'LBS', name= '1922_102')

switch_8533_101_var = True
switch_8533_101 = pp.create_switch(net, bus_8533, line_1922_8533, et='l', closed=switch_8533_101_var, type = 'LBS', name= '8533_101')

#switch_8533_102_var = True
#switch_8533_102 = pp.create_switch(net, bus_8533, line_8533_6999, et='l', closed=switch_8533_102_var, type = 'LBS', name= '8533_102')

switch_6999_101_var = True
switch_6999_101 = pp.create_switch(net, bus_6999, line_8533_6999, et='l', closed=switch_6999_101_var, type = 'LBS', name= '6999_101')

#switch_6999_102_var = True
#switch_6999_102 = pp.create_switch(net, bus_6999, line_6999_6577, et='l', closed=switch_6999_102_var, type = 'LBS', name= '6999_102')

switch_6577_101_var = True
switch_6577_101 = pp.create_switch(net, bus_6577, line_6999_6577, et='l', closed=switch_6577_101_var, type = 'LBS', name= '6577_101')

#switch_6577_102_var = True
#switch_6577_102 = pp.create_switch(net, bus_6577, line_6577_84436_1, et='l', closed=switch_6577_102_var, type = 'LBS', name= '6577_102')

switch_84436_102_var = True
switch_84436_102 = pp.create_switch(net, bus_84436_1, line_6577_84436_1, et='l', closed=switch_84436_102_var, type = 'LBS', name= '84436_102')



#switch_84436_101_var = True
#switch_84436_101 = pp.create_switch(net, bus_84436_1, line_84436_1_2453, et='l', closed=switch_84436_101_var, type = 'LBS', name= '84436_101')

switch_2453_102_var = True
switch_2453_102 = pp.create_switch(net, bus_2453, line_84436_1_2453, et='l', closed=switch_2453_102_var, type = 'LBS', name= '2453_102')

#switch_2453_103_var = False   ### sectoropening
#switch_2453_103 = pp.create_switch(net, bus_2453, line_2453_84494_3, et='l', closed=switch_2453_103_var, type = 'LBS', name= '2453_103')

#switch_84494_302_var = True
#switch_84494_302 = pp.create_switch(net, bus_84494_3, line_2453_84494_3, et='l', closed=switch_84494_302_var, type = 'LBS', name= '84494_302')

#switch_2453_101_var = True
#switch_2453_101 = pp.create_switch(net, bus_2453, line_2453_8563, et='l', closed=switch_2453_101_var, type = 'LBS', name= '2453_101')

switch_8563_101_var = True
switch_8563_101 = pp.create_switch(net, bus_8563, line_2453_8563, et='l', closed=switch_8563_101_var, type = 'LBS', name= '8563_101')

#switch_8563_102_var = True
#switch_8563_102 = pp.create_switch(net, bus_8563, line_8563_84419, et='l', closed=switch_8563_102_var, type = 'LBS', name= '8563_102')

switch_84419_101_var = True
switch_84419_101 = pp.create_switch(net, bus_84419, line_8563_84419, et='l', closed=switch_84419_101_var, type = 'LBS', name= '84419_101')

#switch_84419_102_var = True
#switch_84419_102 = pp.create_switch(net, bus_84419, line_84419_8505, et='l', closed=switch_84419_102_var, type = 'LBS', name= '84419_102')

switch_8505_101_var = True
switch_8505_101 = pp.create_switch(net, bus_8505, line_84419_8505, et='l', closed=switch_8505_101_var, type = 'LBS', name= '8505_101')

switch_8505_102_var = False   ### sectoropening
switch_8505_102 = pp.create_switch(net, bus_8505, line_8505_84490, et='l', closed=switch_8505_102_var, type = 'LBS', name= '8505_102')

#switch_84490_102_var = True
#switch_84490_102 = pp.create_switch(net, bus_84490, line_8505_84490, et='l', closed=switch_84490_102_var, type = 'LBS', name= '84490_102')



#switch_84436_203_var = True
#switch_84436_203 = pp.create_switch(net, bus_84436_2, line_84436_2_84435, et='l', closed=switch_84436_203_var, type = 'LBS', name= '84436_203')

#switch_84436_204_var = True
#switch_84436_204 = pp.create_switch(net, bus_84436_2, line_84436_2_84439, et='l', closed=switch_84436_204_var, type = 'LBS', name= '84436_204')

switch_84439_101_var = True
switch_84439_101 = pp.create_switch(net, bus_84439, line_84436_2_84439, et='l', closed=switch_84439_101_var, type = 'LBS', name= '84439_101')

#switch_84439_102_var = True
#switch_84439_102 = pp.create_switch(net, bus_84439, line_84439_84438, et='l', closed=switch_84439_102_var, type = 'LBS', name= '84439_102')

switch_84438_102_var = True
switch_84438_102 = pp.create_switch(net, bus_84438, line_84439_84438, et='l', closed=switch_84438_102_var, type = 'LBS', name= '84438_102')

#switch_84438_101_var = True
#switch_84438_101 = pp.create_switch(net, bus_84438, line_84438_4129_1, et='l', closed=switch_84438_101_var, type = 'LBS', name= '84438_101')

switch_4129_101_var = True
switch_4129_101 = pp.create_switch(net, bus_4129_1, line_84438_4129_1, et='l', closed=switch_4129_101_var, type = 'LBS', name= '4129_101')

switch_4129_202_var = False   ### sectoropening
switch_4129_202 = pp.create_switch(net, bus_4129_2, line_4129_2_84440, et='l', closed=switch_4129_202_var, type = 'LBS', name= '4129_202')

#switch_84440_202_var = True
#switch_84440_202 = pp.create_switch(net, bus_84440, line_4129_2_84440, et='l', closed=switch_84440_202_var, type = 'LBS', name= '84440_202')



switch_84436_104_var = False   ### sectoropening
switch_84436_104 = pp.create_switch(net, bus_84436_1, bus_84436_3, et='b', closed=switch_84436_104_var, type = 'LBS', name= '84436_104')

switch_84436_103_var = True
switch_84436_103 = pp.create_switch(net, bus_84436_1, bus_84436_2, et='b', closed=switch_84436_103_var, type = 'LBS', name= '84436_103')

switch_4129_102_var = True
switch_4129_102 = pp.create_switch(net, bus_4129_1, bus_4129_2, et='b', closed=switch_4129_102_var, type = 'LBS', name= '4129_102')




###   Lasten en Productie   ###

pp.create_load(net, bus=bus_1922, p_mw=0.25*0.5, name="Load_1922")   #parkeerterrein

pp.create_load(net, bus=bus_8533, p_mw=0.40*demand_profiles.at[t, 'onderwijs_oud'], name="Load_8533")

pp.create_load(net, bus=bus_6999, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_6999")

pp.create_load(net, bus=bus_6577, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_6577_1")

pp.create_load(net, bus=bus_6577, p_mw=1.00*demand_profiles.at[t, 'onderwijs_oud'], name="Load_6577_2")

pp.create_load(net, bus=bus_2453, p_mw=1.00*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_2453")

pp.create_load(net, bus=bus_8563, p_mw=0.40*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_8563")

pp.create_load(net, bus=bus_84419, p_mw=0.20*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84419_1")

pp.create_load(net, bus=bus_84419, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_84419_2")

pp.create_load(net, bus=bus_8505, p_mw=0.63*demand_profiles.at[t, 'lab_nieuw'], name="Load_8505_1")

pp.create_load(net, bus=bus_8505, p_mw=1.00*demand_profiles.at[t, 'lab_nieuw'], name="Load_8505_2")

pp.create_load(net, bus=bus_84435, p_mw=0.40*demand_profiles.at[t, 'lab_oud'], name="Load_84435")

pp.create_load(net, bus=bus_84436_2, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84436_2")

pp.create_load(net, bus=bus_84439, p_mw=0.63*demand_profiles.at[t, 'lab_oud'], name="Load_84439_1")

pp.create_load(net, bus=bus_84439, p_mw=0.40*demand_profiles.at[t, 'lab_oud'], name="Load_84439_2")

pp.create_load(net, bus=bus_84438, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84438_1")

pp.create_load(net, bus=bus_84438, p_mw=0.63*demand_profiles.at[t, 'onderwijs_oud'], name="Load_84438_2")

pp.create_load(net, bus=bus_4129_1, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_4129_1")

pp.create_load(net, bus=bus_4129_2, p_mw=0.63*demand_profiles.at[t, 'onderwijs_nieuw'], name="Load_4129_2")



pp.create_load(net, bus=bus_1922, p_mw=0.4*demand_profiles.at[t, 'ev_simpel'], name="ev_1922")

pp.create_load(net, bus=bus_8563, p_mw=0.05*demand_profiles.at[t, 'ev_simpel'], name="ev_8563") #50 laadpalen, overige 200 die vereist zijn komen op Olympos



pp.create_sgen(net, bus=bus_6999, p_mw=0.034*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_6999')

pp.create_sgen(net, bus=bus_1922, p_mw=0.4*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_1922')

#bus_zonpv_schapenveld = pp.create_bus(net, vn_kv = 10., name = 'bus_zonpv_schapenveld', type = 'n')
#line_zonpv_schapenveld = pp.create_line(net, from_bus=bus_zonpv_schapenveld, to_bus=bus_sorbonne, length_km=0.5, name='lijn_zonpv_schapenveld',std_type="630_AL_XLPE")
pp.create_sgen(net, bus=bus_2453, p_mw=2.5*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_zonpv_schapenveld') #1 helft van de 4ha 5mw research pv fields (andere helft op veldje tussen leuvenlaan en weg tot de wetenschap in)

pp.create_sgen(net, bus=bus_8563, p_mw=0.3*demand_profiles.at[t, 'pv_veld_1_MW'], name='pv_8563') #Solar carports