import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

import logisticmap

if __name__ == "__main__":

    list_float = [1025758974, 8388607, 5368707, 3019900, 2684354, 2684353, 1677723, 1342177, 1342176, 1342178, 1342177, 1342176, 1006635, 671088, 671088, 671089, 671088, 671088, 671090, 671088, 671088, 671089, 671088, 671088, 671101, 335534, 335544, 335544, 335544, 335544, 335544, 335545, 335544, 335544, 335544, 335544, 335544, 335546, 335544, 335544, 335544, 335544, 335544, 335545, 335544, 335544, 335544, 335544, 335544, 335557, 167762, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167773, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167784, 167762, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167773, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167772, 167785]
    list_bereiche = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0]

    i = 10000
    r = r_start = r_stop = 4
    s = 0.1
    start_step = 0.01
    r_step = 0.01

    list_logisticmap = logisticmap.logistischeAbbildung_s_counting(i, r, start_step)

    fig, host = plt.subplots(figsize=(8, 5), layout='constrained')

    ax2 = host.twinx()

    host.set_xlim(0, 1)
    #host.set_ylim(0, 10^9)
    #ax2.set_ylim(0, 100)
    ax2.set_ylabel("Prozentualer Anteil")


    ax2.hist(list_logisticmap, 100, weights=np.ones(len(list_logisticmap)) / len(list_logisticmap), histtype=u'step', label ="Logistische Abbildung mit r =4" )
    host.plot(list_bereiche, list_float, color='red', label="Floats")
    # plt.xlim([9950, 10000])
    # plt.ylim([0, 1])
    host.set_yscale('log')
    #ax2.set_title("Histogramm Floats \n Zahlenbereich 0 bis 1 in {} Klassen".format(100))
    host.set_xlabel("Wertebereich Logistische Abbildung")
    host.set_ylabel('Anzahl')

    #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    host.set_title("Histogramm Logistische Abbildung mit r = {} \n und Histogramm der darstellbaren Floats mit 32 Bit nach IEEE 754".format(round(r, 2)))
    host.legend(loc="upper left")
    ax2.legend(loc="upper right")
    # plt.xlim([9950, 10000])
    #plt.ylim([0, 0.1])
    #plt.xlabel('x-Wertebereich')
    #plt.ylabel('Prozentualer Anteil')
    plt.show()

