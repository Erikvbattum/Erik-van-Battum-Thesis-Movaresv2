# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 14:15:47 2023

@author: battuejd
"""

import load_usp_grid_simple_south as lugs
import load_usp_grid_simple_north as lugn

from pandapower import plotting as plot


lugs
lugn


net = lugs.net


plot.simple_plotly(net)