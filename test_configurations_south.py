# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:55:44 2023

@author: battuejd
"""


import itertools
import pandas as pd
import networkx as nx
import pandapower.topology as top
import load_usp_grid_simple_south as lugs


net = lugs.net





def is_supplied(net):
    return len(top.unsupplied_buses(net)) == 0


is_supplied(net)




def is_radial(net):
    mg = top.create_nxgraph(net, multi=False)
    mg.add_edge(0, 1)
    for cycle in nx.cycle_basis(mg):
        if any([mg[b1][b2]["type"] == "l" for b1, b2 in zip(cycle, cycle[1:]) if "type" in mg[b1][b2]]):
            return False
    return True



is_radial(net)



def analyze_switch_positions(net):
    switch_positions = {}
    count = 0
    geldig = 0
    for i, (s1, s2, s3, s4) in enumerate(itertools.combinations(net.switch.index, 4)):
        net.switch.closed.loc[[s1, s2, s3, s4]] = False
        supplied = is_supplied(net)
        radial = is_radial(net)
        valid = supplied and radial
        if valid == True:
            geldig = geldig + 1
        switch_positions[i] = {"supplied": supplied, "radial": radial, 
                               "valid": valid, "switches": [s1, s2, s3, s4]}
        net.switch.closed = True
        count = count + 1
        print(count, ' van 27405 met ', geldig, ' geldig')
    return pd.DataFrame.from_dict(switch_positions).T




sw = analyze_switch_positions(net)

sw.to_csv('sw_south.csv', index=False)


