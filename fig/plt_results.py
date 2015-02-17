# -*- coding: utf-8 -*-
"""
rp_cfmeans.py

Compares the mean curvatures across two runs.

@author: josh
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *

# Read in the results.
restbl = np.loadtxt("results.dat");

l_pressure = restbl[:,0];
l_bfield = restbl[:,1];
l_eff80 = restbl[:,2];
l_eff90 = restbl[:,3]

# Prepare the plotted quantities.
bvals_p5 = []; eff80_p5 = []; eff90_p5 = [];
bvals_p10 = []; eff80_p10 = []; eff90_p10 = [];
bvals_p15 = []; eff80_p15 = []; eff90_p15 = [];
for pr,bfield,eff80,eff90 in zip(l_pressure,l_bfield,l_eff80,l_eff90):
    if(pr == 5):
        bvals_p5.append(bfield);
        eff80_p5.append(eff80);
        eff90_p5.append(eff90);
    elif(pr == 10):
        bvals_p10.append(bfield);
        eff80_p10.append(eff80); 
        eff90_p10.append(eff90);
    elif(pr == 15):
        bvals_p15.append(bfield);
        eff80_p15.append(eff80);
        eff90_p15.append(eff90);
    else:
        print "WARNING: unexpected pressure = {0}".format(pr);

# Create the plot. 
fig = plt.figure(1);
fig.set_figheight(5.0);
fig.set_figwidth(7.5);
plt.plot(bvals_p5, eff80_p5, '-', color='blue', label='5 atm');
plt.plot(bvals_p5, eff80_p5, '.', color='blue');
plt.plot(bvals_p5, eff90_p5, '-.', color='blue');
plt.plot(bvals_p5, eff90_p5, '.', color='blue');

plt.plot(bvals_p10, eff80_p10, '-', color='green', label='10 atm');
plt.plot(bvals_p10, eff80_p10, '.', color='green');
plt.plot(bvals_p10, eff90_p10, '-.', color='green');
plt.plot(bvals_p10, eff90_p10, '.', color='green');

plt.plot(bvals_p15, eff80_p15, '-', color='red', label='15 atm');
plt.plot(bvals_p15, eff80_p15, '.', color='red');
plt.plot(bvals_p15, eff90_p15, '-.', color='red');
plt.plot(bvals_p15, eff90_p15, '.', color='red');

lnd = plt.legend(loc=4,frameon=False,handletextpad=0);
plt.xlabel("Magnetic Field (T)");
plt.ylabel("Signal Efficiency");

# Print the plot.
fn_plt = "eff_vs_b.pdf";
plt.savefig(fn_plt, bbox_inches='tight');
plt.close();
