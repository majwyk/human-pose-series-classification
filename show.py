# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:49:36 2021

@author: nkliu
"""

import numpy as np
from tool.visualise import visualise
from tool.graph import Graph

sample_path = './data/test/000/P087S00G10B00H00UC072000LC021000A000R0_09201030.npy'
sample = np.load(sample_path)
print(sample.shape)
sample[:,1,:,:,:] = 0
visualise(sample, graph=Graph(), is_3d=True)