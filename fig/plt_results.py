# -*- coding: utf-8 -*-
"""
plt_results.py

Creates summary plots from magnetic field analysis.

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
l_eff90 = restbl[:,3];
l_eff80_fixed = restbl[:,4];
l_eff90_fixed = restbl[:,5];

s_restbl = np.loadtxt("results_SeF6.dat");
l_spressure = s_restbl[:,0];
l_sbfield = s_restbl[:,1];
l_seff80 = s_restbl[:,2];
l_seff90 = s_restbl[:,3];
l_seff80_fixed = s_restbl[:,4];
l_seff90_fixed = s_restbl[:,5];

sevsbtbl1 = np.loadtxt("sevsb_tbl1.dat");
l_sevsb1_se = sevsbtbl1[:,3];
l_sevsb1_bb0 = sevsbtbl1[:,5];
l_sevsb1_bb = [];
for fbb in l_sevsb1_bb0: l_sevsb1_bb.append(1-fbb);

sevsbtbl2 = np.loadtxt("sevsb_tbl2.dat");
l_sevsb2_se = sevsbtbl2[:,3];
l_sevsb2_bb0 = sevsbtbl2[:,5];
l_sevsb2_bb = [];
for fbb in l_sevsb2_bb0: l_sevsb2_bb.append(1-fbb);

sevsbtbl3 = np.loadtxt("sevsb_tbl3.dat");
l_sevsb3_se = sevsbtbl3[:,3];
l_sevsb3_bb0 = sevsbtbl3[:,5];
l_sevsb3_bb = [];
for fbb in l_sevsb3_bb0: l_sevsb3_bb.append(1-fbb);
    
# Prepare the plotted quantities.
bvals_p5 = []; eff80_p5 = []; eff90_p5 = []; eff80_fp5 = []; eff90_fp5 = [];
bvals_p10 = []; eff80_p10 = []; eff90_p10 = []; eff80_fp10 = []; eff90_fp10 = [];
bvals_p15 = []; eff80_p15 = []; eff90_p15 = []; eff80_fp15 = []; eff90_fp15 = [];
for pr,bfield,eff80,eff90,eff80_fixed,eff90_fixed in zip(l_pressure,l_bfield,l_eff80,l_eff90,l_eff80_fixed,l_eff90_fixed):
    if(pr == 5):
        bvals_p5.append(bfield);
        eff80_p5.append(eff80);
        eff90_p5.append(eff90);
        eff80_fp5.append(eff80_fixed);
        eff90_fp5.append(eff90_fixed);
    elif(pr == 10):
        bvals_p10.append(bfield);
        eff80_p10.append(eff80); 
        eff90_p10.append(eff90);
        eff80_fp10.append(eff80_fixed);
        eff90_fp10.append(eff90_fixed);
    elif(pr == 15):
        bvals_p15.append(bfield);
        eff80_p15.append(eff80);
        eff90_p15.append(eff90);
        eff80_fp15.append(eff80_fixed);
        eff90_fp15.append(eff90_fixed);
    else:
        print "WARNING: unexpected pressure = {0}".format(pr);

# Prepare the plotted quantities.
bvals_sp5 = []; eff80_sp5 = []; eff90_sp5 = []; eff80_fsp5 = []; eff90_fsp5 = [];
bvals_sp10 = []; eff80_sp10 = []; eff90_sp10 = []; eff80_fsp10 = []; eff90_fsp10 = [];
bvals_sp15 = []; eff80_sp15 = []; eff90_sp15 = []; eff80_fsp15 = []; eff90_fsp15 = [];
for pr,bfield,eff80,eff90,eff80_fixed,eff90_fixed in zip(l_spressure,l_sbfield,l_seff80,l_seff90,l_seff80_fixed,l_seff90_fixed):
    if(pr == 5):
        bvals_sp5.append(bfield);
        eff80_sp5.append(eff80);
        eff90_sp5.append(eff90);
        eff80_fsp5.append(eff80_fixed);
        eff90_fsp5.append(eff90_fixed);
    elif(pr == 10):
        bvals_sp10.append(bfield);
        eff80_sp10.append(eff80);
        eff90_sp10.append(eff90);
        eff80_fsp10.append(eff80_fixed);
        eff90_fsp10.append(eff90_fixed);
    elif(pr == 15):
        bvals_sp15.append(bfield);
        eff80_sp15.append(eff80);
        eff90_sp15.append(eff90);
        eff80_fsp15.append(eff80_fixed);
        eff90_fsp15.append(eff90_fixed);
    else:
        print "WARNING: unexpected pressure = {0}".format(pr);

# Create the plot. 
fig = plt.figure(1);
fig.set_figheight(5.0);
fig.set_figwidth(7.5);
plt.plot(bvals_p5, eff80_p5, '-', color='blue', label='Xe, 5 atm');
plt.plot(bvals_p5, eff80_p5, '.', color='blue');
plt.plot(bvals_p5, eff80_fp5, '-.', color='blue');
plt.plot(bvals_p5, eff80_fp5, '.', color='blue');


plt.plot(bvals_p10, eff80_p10, '-', color='green', label='Xe, 10 atm');
plt.plot(bvals_p10, eff80_p10, '.', color='green');
plt.plot(bvals_p10, eff80_fp10, '-.', color='green');
plt.plot(bvals_p10, eff80_fp10, '.', color='green');

plt.plot(bvals_sp10, eff80_sp10, '-', color='orange', label='SeF$_6$, 10 atm');
plt.plot(bvals_sp10, eff80_sp10, '.', color='orange');
plt.plot(bvals_sp10, eff80_fsp10, '-.', color='orange');
plt.plot(bvals_sp10, eff80_fsp10, '.', color='orange');

plt.plot(bvals_p15, eff80_p15, '-', color='red', label='Xe, 15 atm');
plt.plot(bvals_p15, eff80_p15, '.', color='red');
plt.plot(bvals_p15, eff80_fp15, '-.', color='red');
plt.plot(bvals_p15, eff80_fp15, '.', color='red');

lnd = plt.legend(loc=4,frameon=False,handletextpad=0);
plt.xlabel("Magnetic Field (T)");
plt.ylabel("Signal efficiency (s)");
plt.title("~ 80% Background Rejection");

# Print the plot.
fn_plt = "eff_vs_b_80.pdf";
plt.savefig(fn_plt, bbox_inches='tight');
plt.close();

# Create the plot.
fig = plt.figure(2);
fig.set_figheight(5.0);
fig.set_figwidth(7.5);
plt.plot(bvals_p5, eff90_p5, '-', color='blue', label='Xe, 5 atm');
plt.plot(bvals_p5, eff90_p5, '.', color='blue');
plt.plot(bvals_p5, eff90_fp5, '-.', color='blue');
plt.plot(bvals_p5, eff90_fp5, '.', color='blue');

plt.plot(bvals_p10, eff90_p10, '-', color='green', label='Xe, 10 atm');
plt.plot(bvals_p10, eff90_p10, '.', color='green');
plt.plot(bvals_p10, eff90_fp10, '-.', color='green');
plt.plot(bvals_p10, eff90_fp10, '.', color='green');

plt.plot(bvals_sp10, eff90_sp10, '-', color='orange', label='SeF$_6$, 10 atm');
plt.plot(bvals_sp10, eff90_sp10, '.', color='orange');
plt.plot(bvals_sp10, eff90_fsp10, '-.', color='orange');
plt.plot(bvals_sp10, eff90_fsp10, '.', color='orange');

plt.plot(bvals_p15, eff90_p15, '-', color='red', label='Xe, 15 atm');
plt.plot(bvals_p15, eff90_p15, '.', color='red');
plt.plot(bvals_p15, eff90_fp15, '-.', color='red');
plt.plot(bvals_p15, eff90_fp15, '.', color='red');

lnd = plt.legend(loc=4,frameon=False,handletextpad=0);
plt.xlabel("Magnetic Field (T)");
plt.ylabel("Signal efficiency (s)");
plt.title("~ 90% Background Rejection");

# Print the plot.
fn_plt = "eff_vs_b_90.pdf";
plt.savefig(fn_plt, bbox_inches='tight');
plt.close();

# Create the plot.
fig = plt.figure(3);
fig.set_figheight(5.0);
fig.set_figwidth(7.5);
plt.plot(l_sevsb1_se, l_sevsb1_bb, '-', color='blue', label='$\sigma_{s} = 1$ mm, $N_{s} = 1$');
plt.plot(l_sevsb2_se, l_sevsb2_bb, '-', color='green', label='$\sigma_{s} = 2$ mm, $N_{s} = 2$');
plt.plot(l_sevsb3_se, l_sevsb3_bb, '-', color='red', label='$\sigma_{s} = 3$ mm, $N_{s} = 3$');

lnd = plt.legend(loc=3,frameon=False,handletextpad=0);
plt.xlabel("Background rejection (1-b)");
plt.ylabel("Signal efficiency (s)");

# Print the plot.
fn_plt = "10atm_05T_sigvsb_all.pdf";
plt.savefig(fn_plt, bbox_inches='tight');
plt.close();
