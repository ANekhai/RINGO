#!/usr/bin/env python2

import matplotlib
matplotlib.use('Agg')  # Force matplotlib to not use any Xwindows backend.
import matplotlib.pyplot as plt

n = 32
data = {"dcj": [], "ml": [], "est":[]}
step_range = range(4, 37, 4)
for step in step_range:

    ml_rep_data = []
    dcj_rep_data = []
    est_rep_data = []
    for rep in range(1, 11):
        with open("rw.n%d.step%d.rep%d/genomes.txt.ml" % (n, step, rep)) as f:
            l = f.readline()
            dcj, ml, est = map(float, f.readline().strip().split())
            dcj_rep_data.append(dcj)
            ml_rep_data.append(ml)
            est_rep_data.append(est)
    data["dcj"].append(dcj_rep_data)
    data["ml"].append(ml_rep_data)
    data["est"].append(est_rep_data)

for t in ["ml", "dcj", "est"]:
    plt.clf()
    plt.cla()
    plt.boxplot(data[t])
    #
    plt.plot([x / 4 for x in step_range], step_range)
    plt.xticks(range(1, len(step_range) + 1), step_range)
    # plt.ylim([0,step_range[-1]+24])

    plt.savefig('%s_vs_real.pdf' % t, bbox_inches='tight')
