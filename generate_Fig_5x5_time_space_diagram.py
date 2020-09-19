# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:21:50 2020

@author: Qin Lei
"""

from util.ACECA import ACECA, getInitState
from util.ECA import ECA
import numpy as np
import matplotlib.pyplot as plt

rule_list1 = [90, 73, 18, 26, 152]


n_cell = 100
run_num = 100
def space2ndarray(space, ndspace):
    for i, row in enumerate(space):
        ndspace[i,:] = list(row)


cmap = plt.get_cmap("Greys")
fig, ax_list = plt.subplots(5,5, sharey="all",figsize=(100,100))
title_list = ["ECA 90","ECA 73","ECA 18","ECA 26","ECA 152"]
title_list2 = ["(a)","(b)","(c)","(d)","(e)"]

init_state = getInitState(n_cell, 0.5)

for i, rule in enumerate(rule_list1):
    
    
    
    eca1 = ECA(rule, init_state=init_state, run_num=run_num, alpha=1)
    
    eca2 = ECA(rule, init_state=init_state, run_num=run_num, alpha=0.5)
    
    aceca2 = ACECA(rule, init_state=init_state, run_num=run_num, alpha=0.8)
    aceca3 = ACECA(rule, init_state=init_state, run_num=run_num, alpha=0.5)
    aceca4 = ACECA(rule, init_state=init_state, run_num=run_num, alpha=0.3)
    
    ca_list = [eca1, eca2, aceca2, aceca3, aceca4]
    
    for j,ca in enumerate(ca_list):
        ca.run(isPrint=False)
        
        ndsp = np.zeros([run_num, n_cell])
        
        space2ndarray(ca.space, ndsp)
        ax_list[i][0].set_ylabel(title_list[i])
        ax_list[0][j].set_title(title_list2[j])
        ax_list[i][j].imshow(ndsp, interpolation='none', cmap=cmap)
        ax_list[i][j].set_xticks([])
        ax_list[i][j].set_yticks([])
        
plt.show()
